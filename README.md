# GREP-V2 on DeepResearch Bench

We built GREP-V2, a multi-agent research system. It scored 54.37 on DeepResearch Bench, beating Tavily (52.44), ThinkDepth (52.43), and everyone else on the leaderboard.

Here's the thing: most "deep research" tools produce surface-level summaries. GREP-V2 produces PhD-level analysis.

## The Numbers

### RACE Leaderboard (Top 10)

| Rank | Model | Overall | Comp | Insight | IF | Read |
|:----:|-------|:-------:|:----:|:-------:|:--:|:----:|
| 1 | **GREP-V2** | **54.37** (+1.93) | **55.02** (+2.18) | **56.26** (+2.67) | 52.03 (+0.11) | **52.50** (+3.29) |
| 2 | Tavily Research | 52.44 | 52.84 | 53.59 | 51.92 | 49.21 |
| 3 | ThinkDepth.ai | 52.43 | 52.02 | 53.88 | **52.04** | 50.12 |
| 4 | Cellcog | 51.94 | 52.17 | 51.90 | 51.37 | 51.94 |
| 5 | Salesforce AIR | 50.65 | 50.00 | 51.09 | 50.77 | 50.32 |
| 6 | Gensee Search GPT-5 | 50.60 | 50.06 | 50.76 | 51.31 | 49.72 |
| 7 | Gemini 2.5 Pro DeepResearch* | 49.71 | 49.51 | 49.45 | 50.12 | 50.00 |
| 8 | LangChain Open Deep Research GPT-5 | 49.33 | 49.80 | 47.34 | 51.05 | 48.99 |
| 9 | OpenAI DeepResearch* | 46.45 | 46.46 | 43.73 | 49.39 | 47.22 |
| 10 | Claude Research* | 45.00 | 45.34 | 42.79 | 47.58 | 44.66 |

*Deltas show improvement vs #2 (Tavily)*

**\*** Third-party evaluation from original paper (June 2025). These were run by the benchmark team, not submitted by Anthropic, OpenAI, or Google. Results may not reflect current performance.

### LLM-as-Judge Evaluation

We ran 40 head-to-head comparisons using Gemini 3 Pro Preview as an expert judge.

| vs Competitor | GREP-V2 Wins |
|---------------|--------------|
| OpenAI Deep Research | 9/10 (90%) |
| Gemini 2.5 Pro Deep Research | 8/10 (80%) |
| Perplexity Research | 10/10 (100%) |
| Grok Deeper Search | 10/10 (100%) |
| **Overall** | **37/40 (92.5%)** |

Note: DeepResearch Bench uses Gemini 2.5 for RACE scoring. We used Gemini 3 Pro Preview for our own LLM-as-judge evaluation because it wasn't available when the benchmark was created. Future benchmark versions should probably update this.

## How GREP-V2 Works

It's a multi-agent system built on the Claude Agent SDK. Four stages:

**1. Research Planning**

Claude Opus 4.5 analyzes the query. It identifies the literal question vs the deeper intent, the causal questions that need answering, and the perspectives required.

**2. Parallel Expert Research**

We spawn 4-8 specialized "research interns" per query. Each has a domain-specific persona and search strategy. They work in parallel, hitting the web for real-time information.

**3. Section Synthesis**

Each expert writes comprehensive markdown sections. These get persisted to disk for fault tolerance - important when you're running 100 PhD-level queries overnight.

**4. Report Integration**

A chief researcher synthesizes all findings, resolves contradictions, and produces the final report with an executive summary.

## Why It Wins

Based on our qualitative analysis:

**vs OpenAI Deep Research**: GREP-V2 provides deeper causal analysis. OpenAI tends toward descriptive summaries.

**vs Gemini 2.5 Pro**: GREP-V2 has more structured methodology sections and actionable recommendations.

**vs Perplexity**: No contest. Perplexity produces overviews. GREP-V2 produces analysis.

**vs Grok**: GREP-V2 handles nuance and multi-faceted questions better.

## Running the LLM Evaluator

We built a custom evaluator using Gemini 3 Pro Preview. It scores reports on 5 dimensions:
- Analytical Depth (25%)
- Structural Sophistication (20%)
- Insight Density (25%)
- Evidence Quality (20%)
- Actionability (10%)

To run it yourself:

```bash
# Set your API key
export GEMINI_API_KEY="your-key"

# Point to your deep_research_bench clone
export DEEPRESEARCH_BENCH_PATH="/path/to/deep_research_bench"

# Run the evaluation
python analysis/llm_judge_eval.py
```

The script evaluates 10 random queries against 4 competitors. Results get saved to `analysis/llm_judge_results.jsonl`.

## Repo Structure

```
├── data/grep-v2.jsonl              # All 100 research reports
├── analysis/
│   ├── llm_judge_eval.py           # LLM judge script (Gemini 3 Pro)
│   ├── llm_judge_results.jsonl     # Raw judge output
│   ├── GREP_V2_SOTA_REPORT.md      # Detailed analysis
│   ├── GREP_V2_LLM_JUDGE_RESULTS.md
│   └── GREP_V2_QUALITATIVE_ANALYSIS.md
└── competitor_comparison/          # Competitor reports
```

## Individual Reports

All 100 reports ranked by score. Click to view.

<details>
<summary>Full results table (100 reports)</summary>

| Rank | ID | Query | Overall | Comp | Insight | IF | Read | Report |
|:----:|:---:|-------|:-------:|:----:|:-------:|:---:|:----:|:------:|
| 1 | 14 | 收集整理全球数学与量子计算交叉领域的主要研究团队及其成果，横向比较其研究方向、论文产出、国际合作、资... | **0.70** | 0.61 | 0.80 | 0.72 | 0.61 | [View](reports/report_014.md) |
| 2 | 83 | Acting as a senior hardware product manager, condu... | **0.62** | 0.63 | 0.66 | 0.60 | 0.55 | [View](reports/report_083.md) |
| 3 | 49 | 为我调研全球范围内，20-30岁的女性对口腔正畸和医美的共同需求的比重。未来有没有把正畸和医美联系起... | **0.62** | 0.62 | 0.61 | 0.62 | 0.60 | [View](reports/report_049.md) |
| 4 | 20 | 研究下Anthropic最新发布的Streamable HTTP的工程中的具体实现方案 | **0.61** | 0.68 | 0.54 | 0.72 | 0.53 | [View](reports/report_020.md) |
| 5 | 4 | 分析 2010 年至今的黄金走势，用思维导图告诉我黄金未来有可能的趋势，关键压力，关键支撑位置 | **0.61** | 0.56 | 0.56 | 0.75 | 0.61 | [View](reports/report_004.md) |
| 6 | 97 | Find data and evidence to support or refute the hy... | **0.58** | 0.59 | 0.62 | 0.53 | 0.55 | [View](reports/report_097.md) |
| 7 | 90 | Analyze the complex issue of liability allocation ... | **0.58** | 0.58 | 0.61 | 0.55 | 0.53 | [View](reports/report_090.md) |
| 8 | 51 | From 2020 to 2050, how many elderly people will th... | **0.58** | 0.60 | 0.62 | 0.50 | 0.58 | [View](reports/report_051.md) |
| 9 | 2 | 收集整理目前国际综合实力前十的保险公司的相关资料，横向比较各公司的融资情况、信誉度、过往五年的增长幅... | **0.57** | 0.63 | 0.54 | 0.58 | 0.55 | [View](reports/report_002.md) |
| 10 | 8 | 能否给我提供一份详尽的报告，分析机器学习或者深度学习在优化材料元素组合配比以实现最佳的材料性能方面的... | **0.57** | 0.59 | 0.59 | 0.55 | 0.54 | [View](reports/report_008.md) |
| 11 | 41 | 收集整理目前中国电影票房前十的电影的相关资料，横向比较各电影的主题、技制作公司、题材、时长等维度，并... | **0.57** | 0.56 | 0.61 | 0.55 | 0.52 | [View](reports/report_041.md) |
| 12 | 89 | Research and analyze the latest advancements and c... | **0.57** | 0.57 | 0.59 | 0.57 | 0.52 | [View](reports/report_089.md) |
| 13 | 86 | Conduct a research report on the manufacturing tec... | **0.57** | 0.59 | 0.59 | 0.53 | 0.55 | [View](reports/report_086.md) |
| 14 | 56 | Is there a general method for solving a first-pric... | **0.57** | 0.57 | 0.59 | 0.54 | 0.55 | [View](reports/report_056.md) |
| 15 | 70 | Trace the evolution from Java Servlets to the Spri... | **0.57** | 0.58 | 0.60 | 0.54 | 0.53 | [View](reports/report_070.md) |
| 16 | 34 | 在二维半导体的接触领域，科研人员为了降低接触电阻做了许多努力。以二硫化钼为例，半金属接触，纯金接触等... | **0.57** | 0.55 | 0.61 | 0.53 | 0.54 | [View](reports/report_034.md) |
| 17 | 67 | Summarize recent research progress in reinforcemen... | **0.57** | 0.60 | 0.60 | 0.51 | 0.52 | [View](reports/report_067.md) |
| 18 | 58 | Exploring Horizontal Gene Transfer (HGT) in Plants... | **0.56** | 0.56 | 0.59 | 0.52 | 0.54 | [View](reports/report_058.md) |
| 19 | 92 | For a research project titled 'Analysis and Study ... | **0.56** | 0.58 | 0.60 | 0.52 | 0.47 | [View](reports/report_092.md) |
| 20 | 64 | Regarding the attitude control problem for UAVs, m... | **0.56** | 0.57 | 0.59 | 0.51 | 0.52 | [View](reports/report_064.md) |
| 21 | 73 | As a senior elementary school English teacher, I n... | **0.56** | 0.57 | 0.59 | 0.53 | 0.54 | [View](reports/report_073.md) |
| 22 | 61 | Research on the price dynamics of chub mackerel in... | **0.56** | 0.60 | 0.56 | 0.52 | 0.53 | [View](reports/report_061.md) |
| 23 | 85 | The primary components of a precision piezoelectri... | **0.56** | 0.59 | 0.58 | 0.50 | 0.50 | [View](reports/report_085.md) |
| 24 | 7 | 在当前中国房地产市场低迷的情况下，政府税收减少，这会多大程度上影响地方政府的财政收入 | **0.56** | 0.56 | 0.57 | 0.53 | 0.55 | [View](reports/report_007.md) |
| 25 | 63 | (working on LN-based nonlinear photonics): Possibl... | **0.55** | 0.56 | 0.58 | 0.50 | 0.54 | [View](reports/report_063.md) |
| 26 | 99 | Research the current applications and recent scien... | **0.55** | 0.57 | 0.60 | 0.50 | 0.51 | [View](reports/report_099.md) |
| 27 | 11 | 请总结碳钢常用缓蚀剂种类，并分析每种缓蚀剂是具有拉曼活性还是红外活性。注意如果是复合缓蚀剂需要分别分... | **0.55** | 0.56 | 0.55 | 0.56 | 0.54 | [View](reports/report_011.md) |
| 28 | 40 | 中国当前的刑罚体系中，死刑、死刑缓期执行、终身监禁的数量、比例、减刑率。 你能否结合中国刑罚执行的全... | **0.55** | 0.52 | 0.58 | 0.57 | 0.53 | [View](reports/report_040.md) |
| 29 | 88 | How did Netflix manage to successfully adapt One H... | **0.55** | 0.55 | 0.59 | 0.51 | 0.53 | [View](reports/report_088.md) |
| 30 | 29 | 50年代至今，中国大陆中国古代文学研究头部学者知识背景差异调查 具体做法：收集整理50年代至今从事中... | **0.55** | 0.58 | 0.57 | 0.55 | 0.44 | [View](reports/report_029.md) |
| 31 | 44 | 国内城市轨道交通行业（主要指地铁）每年的碳滑板用量是多少？主要供应商的份额以及行业趋势分析 | **0.55** | 0.56 | 0.56 | 0.54 | 0.54 | [View](reports/report_044.md) |
| 32 | 54 | In the field of FinTech, machine learning algorith... | **0.55** | 0.56 | 0.58 | 0.51 | 0.53 | [View](reports/report_054.md) |
| 33 | 77 | What is the role of need for closure on misinforma... | **0.55** | 0.56 | 0.58 | 0.50 | 0.54 | [View](reports/report_077.md) |
| 34 | 74 | Please conduct a study and prepare a report on the... | **0.55** | 0.57 | 0.58 | 0.50 | 0.52 | [View](reports/report_074.md) |
| 35 | 72 | Please write a literature review on the restructur... | **0.55** | 0.56 | 0.56 | 0.53 | 0.54 | [View](reports/report_072.md) |
| 36 | 80 | Please investigate the influence of mass media on ... | **0.55** | 0.54 | 0.61 | 0.50 | 0.53 | [View](reports/report_080.md) |
| 37 | 93 | Please prepare a market research analysis of the g... | **0.55** | 0.56 | 0.59 | 0.50 | 0.52 | [View](reports/report_093.md) |
| 38 | 98 | Research Topic: Crafting Techniques for Non-Alcoho... | **0.55** | 0.54 | 0.59 | 0.50 | 0.54 | [View](reports/report_098.md) |
| 39 | 76 | The significance of the gut microbiota in maintain... | **0.55** | 0.55 | 0.58 | 0.52 | 0.53 | [View](reports/report_076.md) |
| 40 | 39 | 我是一名游戏开发，帮我分析一下不同类型游戏的用户群体画像 | **0.55** | 0.57 | 0.57 | 0.50 | 0.51 | [View](reports/report_039.md) |
| 41 | 81 | Write an analysis exploring how historical narrati... | **0.54** | 0.55 | 0.57 | 0.50 | 0.54 | [View](reports/report_081.md) |
| 42 | 3 | 中国金融未来的发展趋势，未来哪一个细分领域（例如投行、pe、固收等）更有上升空间 | **0.54** | 0.55 | 0.55 | 0.51 | 0.56 | [View](reports/report_003.md) |
| 43 | 84 | Research for me how to improve the Static Noise Ma... | **0.54** | 0.56 | 0.57 | 0.50 | 0.53 | [View](reports/report_084.md) |
| 44 | 37 | 调研问题：爵士钢琴在现代音乐创作中的创新与风格演变研究  背景与问题意识： 爵士钢琴，作为爵士乐的核... | **0.54** | 0.55 | 0.57 | 0.50 | 0.53 | [View](reports/report_037.md) |
| 45 | 47 | 2025 年，有哪些因素影响着旅客选择前往不同目的地旅游 | **0.54** | 0.58 | 0.55 | 0.50 | 0.51 | [View](reports/report_047.md) |
| 46 | 5 | 调研国内金融机构之间的投资借贷关系与系统性风险的联系？对不同层次或类型的借贷关系和风险建模 | **0.54** | 0.53 | 0.58 | 0.51 | 0.53 | [View](reports/report_005.md) |
| 47 | 55 | While the market features diverse quantitative str... | **0.54** | 0.54 | 0.57 | 0.51 | 0.50 | [View](reports/report_055.md) |
| 48 | 82 | Research and analyze the diverse paths taken by va... | **0.54** | 0.52 | 0.59 | 0.51 | 0.55 | [View](reports/report_082.md) |
| 49 | 95 | Create comprehensive, in-depth study notes for the... | **0.54** | 0.55 | 0.54 | 0.54 | 0.54 | [View](reports/report_095.md) |
| 50 | 18 | 请你学习一下GCS算法的原理。目前的GCS算法主要是用于安全凸集内的路径自动求解。目前，针对凸集的生... | **0.54** | 0.54 | 0.57 | 0.52 | 0.53 | [View](reports/report_018.md) |
| 51 | 10 | 在800V高压/碳化硅电驱/固态电池/分布式驱动等技术迭代加速的窗口期，如何构建覆盖研发制造-使用场... | **0.54** | 0.53 | 0.56 | 0.53 | 0.54 | [View](reports/report_010.md) |
| 52 | 1 | 收集整理目前中国9阶层实际收入和财务状况，特别研究得出中国的中产有哪些特点，实际中产人数，财力等等 | **0.54** | 0.53 | 0.56 | 0.54 | 0.53 | [View](reports/report_001.md) |
| 53 | 16 | 收集整理目前非接触式感知领域做的最好的算法策略，并为我评估他们的输入信号与准确率 | **0.54** | 0.57 | 0.54 | 0.55 | 0.44 | [View](reports/report_016.md) |
| 54 | 78 | Parkinson's disease has a profound impact on patie... | **0.54** | 0.56 | 0.56 | 0.51 | 0.53 | [View](reports/report_078.md) |
| 55 | 38 | 收集针对近三年内珠宝设计流行趋势变化，如高奢类品牌珠宝以及高定类竞拍品等，总结其共通点以及特色亮点。 | **0.54** | 0.54 | 0.56 | 0.52 | 0.53 | [View](reports/report_038.md) |
| 56 | 68 | I need to dynamically adjust Kubernetes (K8S) clus... | **0.54** | 0.53 | 0.56 | 0.51 | 0.54 | [View](reports/report_068.md) |
| 57 | 13 | 为我调研AI算法能否提升现有电子学读出时幅修正方法 | **0.54** | 0.57 | 0.54 | 0.50 | 0.54 | [View](reports/report_013.md) |
| 58 | 9 | 在计算化学这个领域，我们通常使用Gaussian软件模拟各种情况下分子的结构和性质计算，比如在关键词... | **0.54** | 0.54 | 0.55 | 0.53 | 0.53 | [View](reports/report_009.md) |
| 59 | 53 | Researching how the world's wealthiest governments... | **0.54** | 0.55 | 0.57 | 0.50 | 0.47 | [View](reports/report_053.md) |
| 60 | 21 | 现在AI这么热门，我最感兴趣的就是人工智能在教育领域应用现状，实际能落地的场景还有在教育领域所面临的... | **0.54** | 0.57 | 0.56 | 0.50 | 0.53 | [View](reports/report_021.md) |
| 61 | 94 | Could you provide information on recent developmen... | **0.54** | 0.55 | 0.56 | 0.50 | 0.54 | [View](reports/report_094.md) |
| 62 | 65 | As an agricultural engineering researcher focusing... | **0.54** | 0.54 | 0.54 | 0.52 | 0.53 | [View](reports/report_065.md) |
| 63 | 96 | Please draft a research report analyzing future pr... | **0.54** | 0.54 | 0.56 | 0.50 | 0.52 | [View](reports/report_096.md) |
| 64 | 57 | Summarize the global investments, key initiatives,... | **0.54** | 0.53 | 0.59 | 0.50 | 0.53 | [View](reports/report_057.md) |
| 65 | 35 | 市政污水收集和处理大部分城市采取的模式是核拨制，但这种机制造成了效率的不足，作为政府管理部门有何种操... | **0.54** | 0.55 | 0.55 | 0.51 | 0.53 | [View](reports/report_035.md) |
| 66 | 19 | prometheus 的高流失率会造成什么影响，有什么系统的方案可以解决？各家云厂商有没有现有方案？ | **0.53** | 0.53 | 0.56 | 0.50 | 0.53 | [View](reports/report_019.md) |
| 67 | 69 | Please provide a detailed explanation of the diffe... | **0.53** | 0.53 | 0.54 | 0.51 | 0.55 | [View](reports/report_069.md) |
| 68 | 31 | 选题：中外博物馆教育的现状与未来趋势。要求1.分别总结国内外的现状与特点，特别是国外的现状要按代表性... | **0.53** | 0.55 | 0.56 | 0.50 | 0.53 | [View](reports/report_031.md) |
| 69 | 87 | Are AI fashion design tools leading to creative ho... | **0.53** | 0.53 | 0.55 | 0.51 | 0.52 | [View](reports/report_087.md) |
| 70 | 27 | 如何将AI心理咨询和人类心理咨询有机结合，以便为人类心理健康谋求福利？ | **0.53** | 0.53 | 0.54 | 0.51 | 0.51 | [View](reports/report_027.md) |
| 71 | 91 | I would like a detailed analysis of the Saint Seiy... | **0.53** | 0.53 | 0.53 | 0.53 | 0.54 | [View](reports/report_091.md) |
| 72 | 28 | 传统的药物研究，即便是从多组学角度出发也难以系统地，宏观地解析药物对机体产生的影响。而且个人异质性会... | **0.53** | 0.53 | 0.54 | 0.52 | 0.51 | [View](reports/report_028.md) |
| 73 | 33 | 在微电子工艺中，金属薄膜的生长可以使用多种设备，物理气相沉积设备，化学气相沉积设备，电子束蒸发沉积设... | **0.53** | 0.53 | 0.55 | 0.50 | 0.54 | [View](reports/report_033.md) |
| 74 | 36 | 制造业离散制造（单件小批）基本上靠人的技能才能完成的，为我调研实现自动化的难度有多大 | **0.53** | 0.54 | 0.53 | 0.51 | 0.52 | [View](reports/report_036.md) |
| 75 | 59 | In ecology, how do birds achieve precise location ... | **0.53** | 0.53 | 0.54 | 0.50 | 0.53 | [View](reports/report_059.md) |
| 76 | 48 | 我今年五十三岁，体重一百六十斤，为我提供一份两周的食谱，包含更科学、健康、简单易做的营养搭配（我是中... | **0.53** | 0.55 | 0.55 | 0.50 | 0.53 | [View](reports/report_048.md) |
| 77 | 60 | How to conduct comprehensive and accurate situatio... | **0.53** | 0.52 | 0.54 | 0.51 | 0.52 | [View](reports/report_060.md) |
| 78 | 17 | ""在当今软件开发行业中，低代码/无代码平台对传统开发流程的影响有多大？它们是否真正提高了开发效率，... | **0.53** | 0.52 | 0.54 | 0.51 | 0.52 | [View](reports/report_017.md) |
| 79 | 24 | 如何增强自闭症学生课堂参与度？有哪些有效的策略可供选择？ | **0.53** | 0.53 | 0.54 | 0.50 | 0.50 | [View](reports/report_024.md) |
| 80 | 71 | Acting as an expert in K-12 education research and... | **0.52** | 0.54 | 0.52 | 0.51 | 0.51 | [View](reports/report_071.md) |
| 81 | 79 | Write a paper on Middle Eastern and North African ... | **0.52** | 0.53 | 0.52 | 0.52 | 0.51 | [View](reports/report_079.md) |
| 82 | 30 | 全球南方合作如何推动文明交流互鉴？从理论角度给出深入的学术分析，必须考虑以下维度：非西方现代化、后殖... | **0.52** | 0.56 | 0.53 | 0.50 | 0.49 | [View](reports/report_030.md) |
| 83 | 22 | 中国的艺术生就业领域长期以来较为单一，主要集中在传统艺术机构、教育部门或文创企业。随着社会的发展，艺... | **0.52** | 0.52 | 0.54 | 0.50 | 0.53 | [View](reports/report_022.md) |
| 84 | 62 | What are the most effective approaches to scaling ... | **0.52** | 0.51 | 0.55 | 0.50 | 0.52 | [View](reports/report_062.md) |
| 85 | 50 | 收集整理有关孩子身心健康成长的相关资料，比如怎样合理安排学习、生活、兴趣爱好，以及怎样找到合适自己的... | **0.52** | 0.51 | 0.57 | 0.50 | 0.50 | [View](reports/report_050.md) |
| 86 | 52 | What are the investment philosophies of Duan Yongp... | **0.52** | 0.54 | 0.52 | 0.50 | 0.52 | [View](reports/report_052.md) |
| 87 | 42 | 中共中央 国务院2025年印发的《教育强国建设规划纲要（2024—2035年）》指出实施学生体质强健... | **0.52** | 0.52 | 0.53 | 0.50 | 0.53 | [View](reports/report_042.md) |
| 88 | 6 | 请帮我整理下目前全球具身智能发展的技术路线，以及各个路线的代表性公司，需要包括这些公司的技术路径，产... | **0.52** | 0.54 | 0.51 | 0.51 | 0.51 | [View](reports/report_006.md) |
| 89 | 100 | Write a paper to discuss the influence of AI inter... | **0.52** | 0.50 | 0.53 | 0.50 | 0.54 | [View](reports/report_100.md) |
| 90 | 25 | 请为我整合近几年有关"中性粒细胞在脑缺血急性期和慢性期的功能和发展变化"的研究成果。在此基础上预测中... | **0.52** | 0.53 | 0.52 | 0.50 | 0.49 | [View](reports/report_025.md) |
| 91 | 43 | 软件行业未来趋势和被AI替代的可能性 | **0.52** | 0.52 | 0.52 | 0.50 | 0.52 | [View](reports/report_043.md) |
| 92 | 15 | 收集整理目前世界上关于量子网络的研究，横向比较各课题组的相关工作，从以下几个维度，也可以不局限于这些... | **0.51** | 0.50 | 0.52 | 0.50 | 0.53 | [View](reports/report_015.md) |
| 93 | 32 | 收集整理目前中国历史学界对1937-1949年（抗日战争以及战后）研究的成果和相关论著，横向对比分析... | **0.51** | 0.51 | 0.54 | 0.45 | 0.53 | [View](reports/report_032.md) |
| 94 | 46 | 房地产行业可持续发展的动力是什么？未来10年国家在政策、资金、导向如何促进该行业有序、良性地发展。 | **0.51** | 0.49 | 0.53 | 0.48 | 0.51 | [View](reports/report_046.md) |
| 95 | 23 | 我们部门正在辅导高校老师竞赛，比较想了解创新赛、青教赛的全国一等奖课程的情况和资料。 | **0.51** | 0.52 | 0.52 | 0.51 | 0.44 | [View](reports/report_023.md) |
| 96 | 66 | Which Obsidian plugins can effectively replicate N... | **0.51** | 0.53 | 0.52 | 0.50 | 0.43 | [View](reports/report_066.md) |
| 97 | 45 | 分析《老子》历代注本中"神"的发展 | **0.51** | 0.51 | 0.50 | 0.50 | 0.53 | [View](reports/report_045.md) |
| 98 | 75 | Could the rapeutic interventions aimed at modulati... | **0.51** | 0.48 | 0.52 | 0.50 | 0.52 | [View](reports/report_075.md) |
| 99 | 26 | 为我调研在慢性抗原刺激下（如肿瘤微环境或HIV潜伏感染），CD8+ T细胞线粒体动力学（融合/裂变平... | **0.51** | 0.52 | 0.49 | 0.50 | 0.52 | [View](reports/report_026.md) |
| 100 | 12 | 收集整理近10年来国际上自来水生产及销售企业在技术创新且已经实现创新成果产业化应用方面，按技术产业化... | **0.39** | 0.42 | 0.46 | 0.30 | 0.37 | [View](reports/report_012.md) |

</details>

## Limitations

1. **No citation accuracy metrics**: The benchmark's FACT evaluation uses a scraper that flagged valid sources as invalid. We could fetch these URLs fine, but their scraper couldn't. Skipped for now.
2. **No cost or time tracking**: The benchmark doesn't measure latency or API spend. We should probably add this.
3. **Single benchmark (for now)**: We're focused on research quality vs simple Q&A, so DeepResearch Bench fits well. Planning to adapt for DeepSearchQA, HumanityLastExam, and others. Open to suggestions.

## Links

- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)
- [DeepResearch Bench Repo](https://github.com/Ayanami0730/deep_research_bench)

## Citation

```bibtex
@misc{grep-v2-2024,
  title={GREP-V2 Deep Research Agent Results on DeepResearch Bench},
  author={Parcha AI},
  year={2024},
  url={https://github.com/Parcha-ai/grep-v2-deepresearch-bench}
}
```

MIT License
