#!/usr/bin/env python3
"""
LLM-as-Judge Evaluation for Deep Research Reports
Uses Gemini 3 Pro Preview to compare GREP-V2 vs competitors
"""

import os
import sys
import json
import asyncio
import random
import warnings
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from google import genai
from google.genai import types

# Unbuffered output
sys.stdout.reconfigure(line_buffering=True)

# Suppress warnings
warnings.filterwarnings("ignore")

# Configuration
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = "gemini-3-pro-preview"  # Gemini 3 Pro Preview

# Improved evaluation prompt - sharper and more discriminating than RACE
EXPERT_JUDGE_PROMPT = """You are a PhD-level research quality assessor with expertise in evaluating deep research reports. Your task is to compare two research reports on the same topic and determine which one demonstrates superior research quality.

## Research Task
<task>
{task}
</task>

## Report A (GREP-V2)
<report_a>
{report_a}
</report_a>

## Report B ({competitor_name})
<report_b>
{report_b}
</report_b>

## Evaluation Framework

Evaluate both reports on these 5 dimensions, scoring each 1-10:

### 1. ANALYTICAL DEPTH (Weight: 25%)
- Does the report explain WHY things happen, not just WHAT happened?
- Are there explicit causal reasoning chains (e.g., "X happened BECAUSE Y, which matters BECAUSE Z")?
- Does it identify root causes vs just symptoms?
- Does it provide quantitative thresholds and specific data points?

### 2. STRUCTURAL SOPHISTICATION (Weight: 20%)
- Is there a clear hierarchical organization (sections, subsections)?
- Does the structure guide the reader through a logical argument?
- Are complex topics broken down into digestible components?
- Is there an executive summary or key findings section?

### 3. INSIGHT DENSITY (Weight: 25%)
- Does the report surface non-obvious insights a domain expert would find valuable?
- Are there named concepts, frameworks, or models introduced?
- Does it go beyond what's easily found in a Google search?
- Are counterintuitive findings highlighted and explained?

### 4. EVIDENCE QUALITY (Weight: 20%)
- Are claims backed by specific citations, data, or examples?
- Is there appropriate use of quantitative data vs qualitative assertions?
- Are sources authoritative and recent?
- Is conflicting evidence acknowledged and reconciled?

### 5. ACTIONABILITY (Weight: 10%)
- Does the report provide practical implications?
- Could a decision-maker use this to inform real choices?
- Are recommendations specific rather than generic?

## Output Format

Provide your evaluation as JSON:
```json
{{
    "dimension_scores": {{
        "analytical_depth": {{"report_a": X, "report_b": Y, "reasoning": "..."}},
        "structural_sophistication": {{"report_a": X, "report_b": Y, "reasoning": "..."}},
        "insight_density": {{"report_a": X, "report_b": Y, "reasoning": "..."}},
        "evidence_quality": {{"report_a": X, "report_b": Y, "reasoning": "..."}},
        "actionability": {{"report_a": X, "report_b": Y, "reasoning": "..."}}
    }},
    "weighted_total": {{"report_a": X.XX, "report_b": Y.YY}},
    "winner": "A" or "B" or "TIE",
    "confidence": "HIGH" or "MEDIUM" or "LOW",
    "key_differentiators": ["list of 3 most important differences"],
    "summary": "2-3 sentence summary of why one report is better"
}}
```

Be rigorous and discriminating. A score of 5 is average, 7+ requires clear excellence, 9+ requires exceptional quality. Do not default to similar scores unless the reports are genuinely comparable."""


@dataclass
class EvalResult:
    query_id: int
    task: str
    competitor: str
    scores_a: Dict[str, float]
    scores_b: Dict[str, float]
    weighted_a: float
    weighted_b: float
    winner: str
    confidence: str
    key_differentiators: List[str]
    summary: str
    raw_response: str


class GeminiJudge:
    def __init__(self, api_key: str = GEMINI_API_KEY):
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set")
        self.client = genai.Client(api_key=api_key, http_options={'timeout': 600000})
        self.model = MODEL

    async def evaluate(self, task: str, report_a: str, report_b: str,
                       competitor_name: str) -> Optional[Dict]:
        """Evaluate two reports using Gemini as judge"""

        prompt = EXPERT_JUDGE_PROMPT.format(
            task=task,
            report_a=report_a[:150000],  # Truncate if too long
            report_b=report_b[:150000],
            competitor_name=competitor_name
        )

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=[{"role": "user", "parts": [{"text": prompt}]}],
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    thinking_config=types.ThinkingConfig(thinking_budget=16000)
                )
            )

            # Extract JSON from response
            text = response.text
            json_start = text.find('{')
            json_end = text.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                json_str = text[json_start:json_end]
                return json.loads(json_str)
            return None

        except Exception as e:
            print(f"Error in evaluation: {e}")
            return None


def load_reports(jsonl_path: str) -> Dict[int, Dict]:
    """Load reports from JSONL file, keyed by ID"""
    reports = {}
    with open(jsonl_path, 'r') as f:
        for line in f:
            data = json.loads(line)
            reports[data['id']] = data
    return reports


def load_queries(query_path: str) -> Dict[int, Dict]:
    """Load queries from JSONL file"""
    queries = {}
    with open(query_path, 'r') as f:
        for line in f:
            data = json.loads(line)
            queries[data['id']] = data
    return queries


async def run_evaluation(sample_size: int = 10, competitors: List[str] = None):
    """Run head-to-head evaluation on a sample of queries"""

    # Update this path to your local deep_research_bench directory
    base_path = os.environ.get("DEEPRESEARCH_BENCH_PATH", "./deep_research_bench")

    # Load GREP-V2 reports
    grep_reports = load_reports(f"{base_path}/data/test_data/cleaned_data/grep-v2.jsonl")

    # Load queries for task prompts
    queries = load_queries(f"{base_path}/data/prompt_data/query.jsonl")

    # Default competitors
    if competitors is None:
        competitors = [
            ("openai-deepresearch", "OpenAI DeepResearch"),
            ("gemini-2.5-pro-deepresearch", "Gemini 2.5 Pro DeepResearch"),
            ("perplexity-Research", "Perplexity Research"),
            ("grok-deeper-search", "Grok Deeper Search"),
        ]

    # Load competitor reports
    competitor_reports = {}
    for filename, name in competitors:
        path = f"{base_path}/competitor_reports/generated_reports/{filename}.jsonl"
        if os.path.exists(path):
            competitor_reports[name] = load_reports(path)
            print(f"Loaded {len(competitor_reports[name])} reports from {name}")

    # Select sample of English queries (IDs 1-50)
    english_ids = [i for i in range(1, 51) if i in grep_reports]
    sample_ids = random.sample(english_ids, min(sample_size, len(english_ids)))

    print(f"\nEvaluating {len(sample_ids)} queries against {len(competitor_reports)} competitors")
    print(f"Sample IDs: {sample_ids}")

    judge = GeminiJudge()
    results = []

    for query_id in sample_ids:
        grep_report = grep_reports[query_id]
        task = grep_report.get('prompt', queries.get(query_id, {}).get('prompt', ''))

        for comp_name, comp_reports in competitor_reports.items():
            if query_id not in comp_reports:
                print(f"  Query {query_id} not in {comp_name}, skipping")
                continue

            comp_report = comp_reports[query_id]

            print(f"\nEvaluating Q{query_id}: GREP-V2 vs {comp_name}...")

            eval_result = await judge.evaluate(
                task=task,
                report_a=grep_report['article'],
                report_b=comp_report['article'],
                competitor_name=comp_name
            )

            if eval_result:
                result = EvalResult(
                    query_id=query_id,
                    task=task[:100] + "...",
                    competitor=comp_name,
                    scores_a={k: v['report_a'] for k, v in eval_result.get('dimension_scores', {}).items()},
                    scores_b={k: v['report_b'] for k, v in eval_result.get('dimension_scores', {}).items()},
                    weighted_a=eval_result.get('weighted_total', {}).get('report_a', 0),
                    weighted_b=eval_result.get('weighted_total', {}).get('report_b', 0),
                    winner=eval_result.get('winner', 'UNKNOWN'),
                    confidence=eval_result.get('confidence', 'UNKNOWN'),
                    key_differentiators=eval_result.get('key_differentiators', []),
                    summary=eval_result.get('summary', ''),
                    raw_response=json.dumps(eval_result, indent=2)
                )
                results.append(result)

                winner_str = "GREP-V2" if result.winner == "A" else comp_name if result.winner == "B" else "TIE"
                print(f"  Winner: {winner_str} ({result.confidence} confidence)")
                print(f"  Scores: GREP-V2={result.weighted_a:.2f} vs {comp_name}={result.weighted_b:.2f}")
            else:
                print(f"  Failed to get evaluation")

    return results


def print_summary(results: List[EvalResult]):
    """Print summary statistics"""

    print("\n" + "="*80)
    print("EVALUATION SUMMARY")
    print("="*80)

    # Win rates by competitor
    by_competitor = {}
    for r in results:
        if r.competitor not in by_competitor:
            by_competitor[r.competitor] = {"wins": 0, "losses": 0, "ties": 0, "total": 0}

        by_competitor[r.competitor]["total"] += 1
        if r.winner == "A":
            by_competitor[r.competitor]["wins"] += 1
        elif r.winner == "B":
            by_competitor[r.competitor]["losses"] += 1
        else:
            by_competitor[r.competitor]["ties"] += 1

    print("\nGREP-V2 Win Rate by Competitor:")
    print("-" * 60)
    for comp, stats in by_competitor.items():
        win_rate = stats["wins"] / stats["total"] * 100 if stats["total"] > 0 else 0
        print(f"  vs {comp}:")
        print(f"    Wins: {stats['wins']}/{stats['total']} ({win_rate:.1f}%)")
        print(f"    Losses: {stats['losses']}, Ties: {stats['ties']}")

    # Overall stats
    total_wins = sum(s["wins"] for s in by_competitor.values())
    total_losses = sum(s["losses"] for s in by_competitor.values())
    total_ties = sum(s["ties"] for s in by_competitor.values())
    total = total_wins + total_losses + total_ties

    print(f"\nOverall: {total_wins}/{total} wins ({total_wins/total*100:.1f}%)")

    # Average scores by dimension
    print("\nAverage Dimension Scores:")
    print("-" * 60)
    dimensions = ["analytical_depth", "structural_sophistication", "insight_density",
                  "evidence_quality", "actionability"]

    for dim in dimensions:
        grep_scores = [r.scores_a.get(dim, 0) for r in results if dim in r.scores_a]
        comp_scores = [r.scores_b.get(dim, 0) for r in results if dim in r.scores_b]

        if grep_scores and comp_scores:
            grep_avg = sum(grep_scores) / len(grep_scores)
            comp_avg = sum(comp_scores) / len(comp_scores)
            diff = grep_avg - comp_avg
            print(f"  {dim}: GREP-V2={grep_avg:.2f}, Competitors={comp_avg:.2f} (Δ={diff:+.2f})")

    # Key differentiators frequency
    print("\nMost Common GREP-V2 Advantages:")
    print("-" * 60)
    all_diffs = []
    for r in results:
        if r.winner == "A":
            all_diffs.extend(r.key_differentiators)

    from collections import Counter
    diff_counts = Counter(all_diffs)
    for diff, count in diff_counts.most_common(5):
        print(f"  - {diff} ({count}x)")


async def main():
    print("Starting LLM-as-Judge Evaluation")
    print("Model:", MODEL)
    print("-" * 60)

    results = await run_evaluation(sample_size=10)

    # Save detailed results
    output_path = os.path.join(os.path.dirname(__file__), "llm_judge_results.jsonl")
    with open(output_path, 'w') as f:
        for r in results:
            f.write(json.dumps({
                "query_id": r.query_id,
                "competitor": r.competitor,
                "scores_a": r.scores_a,
                "scores_b": r.scores_b,
                "weighted_a": r.weighted_a,
                "weighted_b": r.weighted_b,
                "winner": r.winner,
                "confidence": r.confidence,
                "key_differentiators": r.key_differentiators,
                "summary": r.summary
            }) + '\n')

    print(f"\nDetailed results saved to: {output_path}")

    print_summary(results)


if __name__ == "__main__":
    asyncio.run(main())
