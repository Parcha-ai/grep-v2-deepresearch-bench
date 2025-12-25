# GREP-V2 Qualitative Analysis: Manual Report Comparison

**Date:** December 24, 2024

---

## Executive Summary

Manual analysis of 50 English queries across 5 models reveals **GREP-V2 produces fundamentally different research outputs** compared to competitors. The differences are not incremental - they represent a different approach to deep research.

---

## Quantitative Comparison (50 EN Queries)

| Metric | GREP-V2 | OpenAI | Gemini | Perplexity | Grok |
|--------|---------|--------|--------|------------|------|
| **Avg Length** | **132,388** | 65,494 | 91,817 | 19,845 | 11,913 |
| **H2 Headers** | 21.4 | 4.6 | 6.4 | 6.8 | 3.2 |
| **H3 Headers** | **74.3** | 2.2 | 14.6 | 12.6 | 4.3 |
| **"Because" (causal)** | **100.2** | 4.7 | 1.3 | 0.2 | 0.0 |
| **Citations** | 137.2 | 83.2 | **182.7** | **192.0** | 19.7 |

### Key Observations

1. **GREP-V2 is 2x longer than OpenAI, 11x longer than Grok**
2. **GREP-V2 has 33x more section structure (H3) than OpenAI**
3. **GREP-V2 uses causal reasoning 21x more than OpenAI, 77x more than Gemini**
4. **Perplexity/Gemini have more citation markers but shallower analysis**

---

## Deep Dive: Q53 - Sovereign Wealth Fund Investment Strategies

### Prompt
> "Researching how the world's wealthiest governments invest."

### Report Lengths
| Model | Length | Relative |
|-------|--------|----------|
| **GREP-V2** | **410,830** | 1.0x |
| Gemini | 79,266 | 0.19x |
| Reference | 70,483 | 0.17x |
| OpenAI | 47,052 | 0.11x |
| Perplexity | 19,015 | 0.05x |
| Grok | 12,497 | 0.03x |

### Structural Analysis

#### GREP-V2 Opening
```markdown
# Asian Sovereign Wealth Funds: Singapore and China's Strategic Investment Models

## Overview

Asian sovereign wealth funds represent a distinct third model of state-backed
investing that differs fundamentally from both Nordic transparency-focused
approaches and Gulf diversification strategies. Singapore operates a sophisticated
dual-fund structure with GIC (Government of Singapore Investment Corporation)
and Temasek Holdings managing over $1.1 trillion combined, while China's CIC
(China Investment Corporation) and SAFE (State Administration of Foreign Exchange)
control approximately $1.5 trillion in assets (Sovereign Wealth Fund Institute, 2024).

This model emphasizes patient, long-term capital deployment combined with strategic
national interests BECAUSE these nations view sovereign wealth as tools for both
financial returns and geopolitical influence. This matters BECAUSE their investment
decisions shape global capital flows and corporate ownership patterns. As a result,
Asian SWFs have become pivotal players in international M&A, infrastructure
development, and technology sector investments.
```

**Analysis:** GREP-V2 immediately establishes:
- Comparative framework (Asian vs Nordic vs Gulf models)
- Specific data ($1.1T, $1.5T assets)
- Causal reasoning chain (BECAUSE → matters BECAUSE → As a result)
- Strategic implications

#### OpenAI Opening
```markdown
# How the World's Wealthiest Governments Invest

## Overview of Sovereign Wealth Funds (SWFs)

Wealthy nations often channel surplus revenues into **Sovereign Wealth Funds (SWFs)**
– state-owned investment funds – to save for the future and achieve strategic goals.
These funds manage **hundreds of billions to trillions of dollars** in assets and
invest globally in stocks, bonds, real estate, infrastructure, private equity, and more.
```

**Analysis:** OpenAI provides:
- Generic definition
- Broad asset ranges ("hundreds of billions to trillions")
- List of asset classes
- No causal reasoning or comparative framework

#### Grok Opening
```markdown
### Key Points
- Research suggests the wealthiest governments invest through sovereign wealth funds
  (SWFs), focusing on diversified, long-term strategies.
- It seems likely that SWFs allocate to equities, bonds, real estate, and private
  equity, with growing emphasis on sustainability.
```

**Analysis:** Grok hedges with "Research suggests" and "It seems likely" - reads like a quick summary, not research.

---

## Deep Dive: Q54 - ML in FinTech Asset Allocation

### Prompt
> "In the field of FinTech, machine learning algorithms are now widely applied to asset allocation..."

### Structural Comparison

| Model | Length | H2 | H3 | "Because" | Citations |
|-------|--------|-----|-----|-----------|-----------|
| **GREP-V2** | 92,251 | 10 | 72 | 30 | 87 |
| Gemini | 70,097 | 8 | 19 | 4 | 50 |
| OpenAI | 41,369 | 0 | 0 | 3 | 61 |

### Key Findings Comparison

#### GREP-V2 Key Finding
```markdown
**The 1/N Paradox Persists**: Despite 70+ years of optimization research,
equal-weight portfolios frequently match or outperform sophisticated optimization
in out-of-sample tests. According to [DeMiguel, Garlappi, and Uppal (2007)],
approximately 3,000 monthly observations (250 years!) are required before
mean-variance optimization reliably outperforms naive diversification—far
exceeding available data for most assets.
```

**Analysis:** GREP-V2 provides:
- Named concept ("1/N Paradox")
- Historical context (70+ years)
- Specific quantitative threshold (3,000 observations = 250 years)
- Academic citation
- Practical implication

#### OpenAI Equivalent Section
```markdown
**Traditional Mean-Variance Optimization (Markowitz):** The classical mean-variance
model (Markowitz, 1952) bases decisions solely on two parameters – **expected return**
and **risk measured as variance**.
```

**Analysis:** OpenAI provides textbook definition without the critical insight about the paradox.

---

## Causal Reasoning Analysis

GREP-V2's distinctive "BECAUSE → matters BECAUSE → As a result" pattern appears **100 times per report on average** vs near-zero for competitors.

### Example from Q53 (GREP-V2)
```
Singapore's model emerged from pragmatic necessity in the 1970s and 1980s
BECAUSE the city-state lacked natural resources and needed to transform
foreign exchange reserves into sustainable intergenerational wealth.

The dual-fund structure separates conservative reserve management (GIC)
from active commercial investing (Temasek) BECAUSE this division allows
for different risk profiles while maintaining government control.

This matters BECAUSE it provides a template for how small, resource-poor
nations can build substantial sovereign wealth through financial
sophistication rather than commodity extraction.

As a result, Singapore achieved one of the highest sovereign wealth-to-GDP
ratios globally, with SWF assets exceeding 200% of GDP.
```

This pattern:
1. States the fact
2. Explains WHY (root cause)
3. Explains WHY IT MATTERS (significance)
4. States the OUTCOME (result)

**No other model consistently applies this reasoning framework.**

---

## Model-by-Model Assessment

### OpenAI DeepResearch
- **Strengths:** Clean formatting, balanced coverage
- **Weaknesses:** Shallow analysis, textbook-style definitions, lacks unique insights
- **Style:** Encyclopedia entry

### Gemini 2.5 Pro DeepResearch
- **Strengths:** Good academic structure, reasonable depth
- **Weaknesses:** Dense prose, limited causal reasoning, over-relies on citations
- **Style:** Academic paper draft

### Perplexity Research
- **Strengths:** Many citations, current data
- **Weaknesses:** Very short, superficial, more like search results than research
- **Style:** Enhanced search summary

### Grok Deeper Search
- **Strengths:** Quick reads, bullet points
- **Weaknesses:** Extremely shallow, hedging language ("seems likely"), blog-post quality
- **Style:** Twitter thread / blog post

### GREP-V2 (Ours)
- **Strengths:** Deep analysis, causal reasoning, comprehensive coverage, expert-level insights
- **Weaknesses:** Can be very long (400K+ chars for complex topics)
- **Style:** PhD-level research report

---

## Why GREP-V2 Scores Higher on RACE

Based on this analysis, GREP-V2's RACE advantage comes from:

### 1. Comprehensiveness (+2.05 over Tavily)
- 2x average length
- 5x more section structure
- Covers topics from multiple angles

### 2. Insight (+2.80 over Tavily)
- 20x+ more causal reasoning
- Named concepts and frameworks
- Quantitative thresholds and specific data
- "This matters because" explanations

### 3. Readability (+3.29 over Tavily)
- Clear section hierarchy (74 H3 headers avg)
- Consistent reasoning patterns
- Executive summaries with key findings

### 4. Instruction Following (+0.02 over Tavily)
- Similar to competitors (all follow instructions)

---

## Conclusion

GREP-V2 doesn't just produce longer reports - it produces **fundamentally different research**:

| Dimension | Competitors | GREP-V2 |
|-----------|-------------|---------|
| Approach | Summarize sources | Synthesize & analyze |
| Reasoning | Implicit | Explicit causal chains |
| Depth | Surface-level | Root cause analysis |
| Structure | Flat | Deeply hierarchical |
| Style | Encyclopedia/Blog | PhD Research |

**The 1.90 point SOTA gap understates the qualitative difference.**

---

*Analysis conducted December 24, 2024*
