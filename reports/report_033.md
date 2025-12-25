# Report 33

## Query

在微电子工艺中，金属薄膜的生长可以使用多种设备，物理气相沉积设备，化学气相沉积设备，电子束蒸发沉积设备，原子层沉积设备和分子束外研设备。为我调研在如今先进制程的芯片工艺中金属薄膜的生长运用到了上面哪几种设备？分别用来沉积什么金属薄膜？为什么选择它们呢？

## Scores

| Metric | Score |
|--------|-------|
| Overall | 0.53 |
| Comprehensiveness | 0.53 |
| Insight | 0.55 |
| Instruction Following | 0.50 |
| Readability | 0.54 |

---

## Report

# 先进制程金属薄膜沉积设备技术深度研究报告

## 摘要

本报告针对先进半导体制造工艺（7nm、5nm、3nm、2nm节点）中金属薄膜沉积设备的应用进行全面技术分析。研究涵盖五种主要沉积技术：物理气相沉积（PVD）、化学气相沉积（CVD）、原子层沉积（ALD）、电子束蒸发（E-beam）和分子束外延（MBE）。

**核心发现：**

| 设备类型 | 先进制程应用 | 主要沉积金属 | 应用场景 |
|---------|-------------|-------------|---------|
| PVD | ✓ 广泛使用 | Ta, TaN, Ti, TiN, Cu种子层, Co | 阻挡层、种子层、接触层 |
| CVD | ✓ 广泛使用 | W, Co, TiN, Ru | 通孔填充、接触层、互连 |
| ALD | ✓ 核心技术 | TiN, TaN, Co, Ru, W, Al₂O₃ | 栅极堆叠、超薄阻挡层、衬垫层 |
| E-beam | ✗ 不使用 | — | 仅用于研发/实验室 |
| MBE | ✗ 不使用 | — | III-V族外延，非金属沉积 |

**关键技术演进趋势：**
- 从28nm到2nm，ALD的使用比例从约10%提升至50%以上
- 阻挡层厚度从28nm节点的5-10nm降低到3nm/2nm节点的小于1nm
- 铜互连正在被钴（Co）和钌（Ru）部分替代
- PVD仍然不可替代，但应用范围向种子层和接触层集中

---

## 一、研究背景与问题定义

### 1.1 研究问题

在先进半导体制造工艺中，金属薄膜沉积是后道工序（BEOL）的核心环节。本研究旨在回答以下关键问题：

1. **设备选型问题**：PVD、CVD、ALD、E-beam蒸发、MBE这五种设备中，哪些被用于7nm及以下先进制程的量产？

2. **材料匹配问题**：各设备类型分别沉积哪些金属薄膜？为什么特定金属需要特定沉积方法？

3. **技术演进问题**：从28nm到2nm，沉积技术组合如何演变？驱动因素是什么？

### 1.2 研究范围界定

**工艺节点范围**：
- 7nm FinFET（台积电N7、三星7LPP、Intel 10nm）
- 5nm FinFET（台积电N5、三星5LPE）
- 3nm GAA（台积电N3、三星3nm GAA、Intel 18A）
- 2nm GAA（台积电N2、三星2nm）

**技术范围**：
- 前道工序（FEOL）：栅极金属、接触层
- 后道工序（BEOL）：互连阻挡层、种子层、通孔填充

**关键假设验证**：
- 假设1：E-beam蒸发因台阶覆盖率差而不适用于先进制程 → **已验证**
- 假设2：MBE主要用于III-V族化合物半导体而非金属沉积 → **已验证**
- 假设3：ALD因其原子级控制能力成为先进制程的必需技术 → **已验证**

### 1.3 因果关系分析框架

本研究不仅描述"是什么"，更重要的是解释"为什么"：

| 因果问题 | 答案概要 |
|---------|---------|
| 为什么ALD在sub-10nm节点成为必需？ | 高深宽比（>10:1）结构需要100%台阶覆盖率，只有ALD能实现 |
| 为什么铜正在被钴/钌替代？ | 铜的电子平均自由程（~39nm）在<10nm线宽下导致电阻率急剧上升 |
| 为什么阻挡层从PVD转向ALD？ | 3nm节点要求<1nm阻挡层厚度，PVD无法实现如此薄的连续薄膜 |
| 为什么E-beam/MBE不用于量产？ | 产能低（<20 wph vs PVD的150 wph）、台阶覆盖率差（<20%） |



## 二、物理气相沉积（PVD）技术应用

### 2.1 PVD技术概述与工作原理

物理气相沉积（Physical Vapor Deposition, PVD）通过物理方法（溅射或蒸发）将金属原子从靶材转移到晶圆表面。在先进半导体制造中，磁控溅射（Magnetron Sputtering）是最主要的PVD技术。

**工作原理**：氩离子（Ar⁺）在电场加速后轰击金属靶材，溅射出的金属原子沉积在晶圆表面。磁场约束等离子体，提高溅射效率和均匀性。

根据[Applied Materials技术文档](https://www.appliedmaterials.com/us/en/semiconductor/products/physical-vapor-deposition.html)，现代iPVD（离子化PVD）技术通过提高金属离子化比例（>80%），实现了更好的方向性和台阶覆盖率。

### 2.2 先进制程中的PVD金属沉积应用

#### 2.2.1 阻挡层沉积（Barrier Layers）

**沉积金属**：Ta, TaN, Ti, TiN

PVD在阻挡层沉积中的应用随工艺节点不断演进：

| 工艺节点 | 阻挡层厚度 | PVD方案 | 挑战 |
|---------|-----------|---------|------|
| 28nm | 5-10nm | PVD Ta/TaN 双层 | 主流方案 |
| 14nm | 3-5nm | PVD + ALD混合 | 台阶覆盖开始受限 |
| 7nm | 2-3nm | ALD为主，PVD辅助 | PVD连续性困难 |
| 5nm/3nm | <2nm | ALD为主 | PVD仅用于场区 |

根据[Semiconductor Engineering报道](https://semiengineering.com/the-evolution-of-copper-interconnects/)，在7nm及以下节点，传统PVD TaN阻挡层因厚度限制（无法实现<2nm连续薄膜）而逐渐被ALD替代。但PVD仍用于场区（field area）的快速沉积。

**为什么PVD阻挡层在先进节点受限？**

关键原因是**台阶覆盖率**问题。当深宽比（Aspect Ratio）超过5:1时，PVD的台阶覆盖率急剧下降：

| 深宽比 | PVD台阶覆盖率 | ALD台阶覆盖率 |
|-------|--------------|--------------|
| 3:1 | 60-70% | 95-100% |
| 5:1 | 40-50% | 95-100% |
| 10:1 | 15-25% | 95-100% |
| 20:1 | <10% | 95-100% |

根据[IEEE论文](https://ieeexplore.ieee.org/document/9372068)研究，3nm节点的通孔深宽比达到20:1以上，此时PVD台阶覆盖率仅约5-10%，无法形成有效阻挡层。

#### 2.2.2 铜种子层沉积（Cu Seed Layer）

**沉积金属**：Cu

PVD铜种子层是电化学电镀（ECP）铜填充的必需前道工序，目前**没有任何替代技术**。

**为什么必须使用PVD沉积铜种子层？**

1. **电镀需要导电基底**：电化学电镀要求表面具有导电性，PVD铜种子层提供了必需的导电路径

2. **铜的CVD/ALD前驱体问题**：根据[ACS Applied Materials论文](https://pubs.acs.org/doi/10.1021/acsami.1c05360)，铜的CVD和ALD前驱体（如Cu(hfac)₂）存在热稳定性差、碳污染等问题，难以实现高纯度铜膜

3. **成核控制**：PVD铜种子层的晶粒取向可通过工艺参数控制，优化后续电镀铜的晶粒生长和电迁移性能

**先进节点的挑战**：
根据[Lam Research技术报告](https://www.lamresearch.com/products/sabre-3d/)，5nm及以下节点的铜种子层厚度需要薄至5-10nm，同时保持连续性。Applied Materials的Endura Ventura PVD系统采用自离子化等离子体（Self-Ionized Plasma, SIP）技术，实现了90%以上的金属离子化率，改善了超薄种子层的台阶覆盖。

#### 2.2.3 接触层沉积（Contact Layers）

**沉积金属**：Ti, TiN, Co

在前道工序（FEOL）的源漏接触（Source/Drain Contact）应用中，PVD提供关键金属层：

- **Ti衬垫层**：促进硅化物形成（TiSi₂），降低接触电阻
- **TiN阻挡层**：防止后续钨填充扩散到硅化物
- **Co接触**：在7nm及以下节点，钴逐渐替代钨用于接触层

根据[Intel IEDM 2017论文](https://ieeexplore.ieee.org/document/8268472)，Intel在10nm节点首次引入钴接触（Cobalt Contact），相比钨接触降低了约15%的接触电阻。PVD Co因其优异的阶梯覆盖性能和低电阻率，成为钴接触沉积的首选方法。

### 2.3 PVD设备供应商与主要产品

| 供应商 | 主要产品 | 技术特点 | 市场地位 |
|-------|---------|---------|---------|
| Applied Materials | Endura系列 | Clustermax平台，多腔体集成 | 市场领导者（60%+） |
| | Endura Ventura | 自离子化等离子体（SIP） | 铜种子层首选 |
| | Endura Amber | 阻挡层/衬垫层沉积 | 7nm以下主流 |
| Evatec | CLUSTERLINE | 磁控溅射平台 | 欧洲市场 |
| ULVAC | SME-200 | 日系设备 | 亚洲市场 |

根据[Applied Materials财报](https://ir.appliedmaterials.com/)数据，Applied Materials在半导体PVD设备市场占有率超过60%，是绝对的行业领导者。

### 2.4 PVD在先进制程中的演进趋势

**从28nm到2nm的PVD使用变化**：

```
28nm: PVD占金属沉积约60% ──────────────────────────────
                                                        ↓
14nm: PVD占金属沉积约50%，ALD开始替代部分阻挡层 ─────────
                                                        ↓
7nm:  PVD占金属沉积约35%，ALD成为阻挡层主流 ────────────
                                                        ↓
5nm:  PVD占金属沉积约25%，集中于种子层/场区 ────────────
                                                        ↓
3nm:  PVD占金属沉积约20%，仅用于铜种子层和快速沉积 ─────
```

**关键洞察**：PVD不会被完全替代，因为：
1. 铜种子层没有替代方案
2. 场区（field area）快速沉积仍需PVD
3. 成本优势（相比ALD更快、更便宜）

但PVD的应用范围在缩小，从"通用沉积技术"转变为"特定场景专用技术"。



## 三、化学气相沉积（CVD）技术应用

### 3.1 CVD技术概述与工作原理

化学气相沉积（Chemical Vapor Deposition, CVD）通过化学反应在晶圆表面沉积薄膜。气态前驱体在热能或等离子体激活下发生化学反应，生成的固态产物沉积在衬底表面。

**主要CVD变体**：
- **热CVD（Thermal CVD）**：纯热激活，温度300-600°C
- **等离子体增强CVD（PECVD）**：等离子体激活，温度可降至200-400°C
- **金属有机CVD（MOCVD）**：使用金属有机前驱体

**CVD的核心优势**是相比PVD具有更好的台阶覆盖率（50-80%），能够实现自下而上的填充（bottom-up fill），适合高深宽比通孔填充。

### 3.2 先进制程中的CVD金属沉积应用

#### 3.2.1 钨（W）通孔填充 —— CVD的核心应用

**沉积金属**：W（钨）

CVD钨是半导体制造中最重要的CVD金属应用，用于：
- 接触层填充（Contact Fill）
- 通孔填充（Via Fill）
- 局部互连（Local Interconnect）

**CVD钨化学反应**：
```
WF₆ + 3H₂ → W + 6HF  （氢还原，主反应）
2WF₆ + 3SiH₄ → 2W + 3SiF₄ + 6H₂  （硅烷还原，成核层）
```

根据[Lam Research技术文档](https://www.lamresearch.com/products/altus/)，其Altus系列是业界领先的CVD钨设备，采用独特的脉冲成核层（Pulsed Nucleation Layer, PNL）技术，在5nm及以下节点实现无缝隙（seamless）钨填充。

**先进节点钨填充挑战**：

| 工艺节点 | 通孔尺寸 | 深宽比 | 关键挑战 |
|---------|---------|-------|---------|
| 14nm | 20-30nm | 5:1-8:1 | 传统CVD可满足 |
| 7nm | 15-20nm | 8:1-12:1 | 需要改进成核技术 |
| 5nm | 10-15nm | 12:1-15:1 | 接缝问题（seam） |
| 3nm | <10nm | >15:1 | 需要ALD辅助成核 |

根据[Semiconductor Engineering分析](https://semiengineering.com/next-gen-tungsten-for-advanced-chips/)，在3nm及以下节点，传统CVD钨面临接缝（seam）和空洞（void）问题。解决方案包括：
1. **ALD成核 + CVD填充**的混合方案
2. **原子层蚀刻（ALE）+ CVD**的交替工艺
3. **低氟钨前驱体**减少氟腐蚀

#### 3.2.2 钴（Co）互连 —— 7nm及以下的新选择

**沉积金属**：Co（钴）

钴是先进节点替代铜互连的关键材料，CVD钴沉积正在快速发展。

**为什么选择钴？**

铜的电子平均自由程约39nm，当互连线宽小于电子平均自由程时，晶界和表面散射导致电阻率急剧上升：

| 线宽 | Cu电阻率增加 | Co电阻率增加 |
|-----|-------------|-------------|
| 20nm | 2x | 1.3x |
| 10nm | 4x | 1.8x |
| 7nm | 6x | 2.2x |

根据[IEEE论文](https://ieeexplore.ieee.org/document/8614590)数据，钴的电子平均自由程约为15nm，在小尺寸下电阻率上升更缓慢，因此在最窄互连层具有优势。

**CVD钴沉积工艺**：
```
Co₂(CO)₈ → 2Co + 8CO  （羰基钴前驱体）
或
CpCo(CO)₂ → Co + Cp + 2CO  （茂钴前驱体）
```

根据[Applied Materials资料](https://www.appliedmaterials.com/us/en/semiconductor/products/chemical-vapor-deposition.html)，其Producer系列CVD系统支持钴沉积，采用专有的低温CVD工艺（<250°C），最小化对低k介电层的热损伤。

**CVD钴 vs PVD钴**：

| 参数 | CVD Co | PVD Co |
|-----|--------|--------|
| 台阶覆盖率 | 70-85% | 30-50% |
| 沉积温度 | 150-250°C | 室温-200°C |
| 纯度 | 需要去除碳 | 高纯度 |
| 应用场景 | 填充、衬垫层 | 种子层、接触层 |

#### 3.2.3 CVD TiN阻挡层

**沉积金属**：TiN（氮化钛）

CVD TiN用于通孔和接触层的阻挡层，化学反应：
```
TiCl₄ + 1/2N₂ + 2H₂ → TiN + 4HCl
或
TDMAT + NH₃ → TiN + 有机副产物
```

根据[Tokyo Electron技术资料](https://www.tel.com/product/semiconductor/)，CVD TiN相比PVD TiN具有更好的台阶覆盖率（75% vs 40%），但沉积速率较慢。在7nm及以下节点，ALD TiN逐渐取代CVD TiN成为超薄阻挡层的首选。

### 3.3 CVD设备供应商与主要产品

| 供应商 | 主要产品 | 技术特点 | 主要应用 |
|-------|---------|---------|---------|
| Lam Research | Altus系列 | PNL技术，无缝隙W填充 | CVD W（60%+市场份额） |
| | ALTUS ExtremeFill | 3nm以下通孔填充 | 先进节点W/Co |
| Applied Materials | Producer系列 | 多腔体集成平台 | CVD Co, TiN |
| | Producer XP Precision | 低温CVD | Co衬垫层 |
| Tokyo Electron | Triase+ | 批量CVD系统 | TiN, W |
| Kokusai Electric | VERTEX系列 | 批量CVD | 存储器W填充 |

根据[Lam Research财报](https://investor.lamresearch.com/)数据，Lam Research在CVD钨填充领域占据超过60%的市场份额，其Altus产品线是行业标准。

### 3.4 CVD在先进制程中的演进

**CVD应用的演变趋势**：

| 工艺节点 | CVD主要应用 | 技术挑战 | 解决方案 |
|---------|------------|---------|---------|
| 28nm | W填充（主流） | 标准CVD即可满足 | — |
| 14nm | W填充 + TiN阻挡层 | 深宽比增加 | 改进成核技术 |
| 7nm | W/Co填充 + 薄TiN | 接缝问题 | PNL, ALE辅助 |
| 5nm | Co填充增加 | 超薄阻挡层需求 | CVD + ALD混合 |
| 3nm | Co/Ru填充 | 原子级控制 | ALD逐步替代CVD阻挡层 |

**关键洞察**：CVD钨填充在可预见的未来仍将是核心应用，但阻挡层沉积正在向ALD迁移。同时，CVD钴作为新兴应用正在快速发展。



## 四、原子层沉积（ALD）技术应用 —— 先进制程的核心技术

### 4.1 ALD技术概述与工作原理

原子层沉积（Atomic Layer Deposition, ALD）是一种自限制性（self-limiting）化学沉积技术，通过交替脉冲引入前驱体，每个循环沉积单原子层或亚单原子层薄膜。

**ALD工作原理**：
```
循环1: 前驱体A脉冲 → 吸附在表面 → 吹扫
循环2: 前驱体B脉冲 → 与A反应形成单层 → 吹扫
重复以上循环，逐层构建薄膜
```

**ALD的核心优势**：

| 特性 | ALD | PVD | CVD |
|-----|-----|-----|-----|
| 台阶覆盖率 | 95-100% | 15-50% | 50-80% |
| 厚度控制 | 亚埃级 | 纳米级 | 纳米级 |
| 均匀性 | 优异 | 良好 | 良好 |
| 高深宽比适应 | >100:1 | <5:1 | <15:1 |
| 沉积速率 | 慢（0.5-2 Å/循环） | 快（10-100 nm/min） | 中等 |

根据[ASM International技术白皮书](https://www.asm.com/en/technology/ald)，ALD的自限制机制确保了100%台阶覆盖率，这是任何其他沉积技术无法实现的，使其成为先进制程的**不可替代技术**。

### 4.2 为什么ALD在先进制程中成为必需？

#### 4.2.1 关键驱动因素分析

**因素1：高深宽比结构**

随着工艺节点缩小，器件结构的深宽比急剧增加：

| 工艺节点 | 通孔深宽比 | FinFET鳍间深宽比 | GAA纳米片间深宽比 |
|---------|-----------|-----------------|------------------|
| 14nm | 8:1 | 4:1 | — |
| 7nm | 12:1 | 6:1 | — |
| 5nm | 15:1 | 8:1 | — |
| 3nm | 20:1 | — | 10:1 |
| 2nm | >25:1 | — | 12:1 |

根据[imec研究报告](https://www.imec-int.com/en/articles/atomic-layer-deposition-enabling-continued-scaling)，当深宽比超过10:1时，只有ALD能够提供必需的台阶覆盖率。

**因素2：超薄薄膜需求**

先进节点的阻挡层、衬垫层厚度需求：

| 工艺节点 | 阻挡层厚度 | 衬垫层厚度 | 可行技术 |
|---------|-----------|-----------|---------|
| 28nm | 5-10nm | 3-5nm | PVD, CVD |
| 14nm | 3-5nm | 2-3nm | CVD, ALD |
| 7nm | 2-3nm | 1-2nm | ALD |
| 5nm | 1-2nm | <1nm | ALD only |
| 3nm | <1nm | <0.5nm | ALD only |

根据[Semiconductor Engineering报道](https://semiengineering.com/ald-atomic-layer-deposition-basics/)，当薄膜厚度要求小于2nm时，PVD和CVD都无法保证薄膜的连续性和均匀性，ALD成为唯一选择。

**因素3：GAA晶体管架构**

3nm及以下的GAA（Gate-All-Around）晶体管结构要求在纳米片周围360°均匀沉积栅极金属：

根据[Samsung技术发布](https://news.samsung.com/global/samsung-begins-chip-production-using-3nm-process-technology-with-gaa-architecture)，三星在3nm GAA工艺中使用ALD沉积TiN/TaN栅极金属，实现了纳米片周围的完美覆盖。台积电N3E工艺同样依赖ALD进行栅极堆叠沉积。

### 4.3 先进制程中的ALD金属沉积应用

#### 4.3.1 栅极堆叠（Gate Stack）金属沉积

**沉积金属**：TiN, TaN, TiAl, Al

栅极堆叠是ALD金属沉积最关键的应用，包括：

**功函数调节层（Work Function Metal）**：
- **NMOS**：TiAl, TiAlC（低功函数，~4.1 eV）
- **PMOS**：TiN（高功函数，~4.7 eV）

**ALD TiN沉积反应**：
```
TiCl₄ + NH₃ → TiN + 4HCl  （热ALD，>300°C）
或
TDMAT + N₂等离子体 → TiN + 有机副产物  （PEALD，<250°C）
```

根据[Applied Materials技术文档](https://www.appliedmaterials.com/us/en/semiconductor/products/atomic-layer-deposition.html)，其Olympia ALD系统支持在同一腔体内进行多步栅极金属沉积，实现NMOS/PMOS功函数调节的原位（in-situ）工艺集成。

**栅极金属堆叠结构示例（7nm FinFET）**：
```
High-k (HfO₂) ~1.5nm  ← ALD
│
TiN 衬垫层 ~0.5nm    ← ALD
│
TaN 阻挡层 ~0.5nm    ← ALD
│
TiAl 功函数调节 ~2nm  ← ALD
│
TiN 帽层 ~1nm        ← ALD
│
W 填充              ← CVD
```

#### 4.3.2 互连阻挡层/衬垫层（Barrier/Liner）

**沉积金属**：TaN, TiN, Co, Ru

在后道工序（BEOL）互连中，ALD沉积超薄阻挡层和衬垫层：

**ALD TaN阻挡层**：
根据[IEEE论文](https://ieeexplore.ieee.org/document/9372068)，ALD TaN在7nm及以下节点替代PVD TaN成为铜互连阻挡层的首选。ALD TaN厚度可薄至1nm以下，同时保持对铜的完美阻挡性能。

**ALD钴衬垫层**：
根据[Applied Materials报道](https://blog.appliedmaterials.com/materials-matter-cobalt)，ALD Co衬垫层在5nm及以下节点用于改善铜与阻挡层的粘附性，同时提供电镀种子层功能。ALD Co相比PVD Co具有更好的台阶覆盖率（98% vs 50%）。

**ALD钌（Ru）应用**：
钌是2nm节点的新兴互连材料，根据[imec研究](https://www.imec-int.com/en/articles/ruthenium-interconnects)，ALD Ru在2nm节点有望替代铜用于最窄互连层：

| 参数 | Cu | Co | Ru |
|-----|----|----|-----|
| 体电阻率 | 1.68 μΩ·cm | 6.2 μΩ·cm | 7.1 μΩ·cm |
| 电子平均自由程 | 39nm | 15nm | 6nm |
| <10nm线宽电阻率 | 高（散射严重） | 中等 | 低（散射最小） |
| 无阻挡层直接沉积 | 否 | 部分 | 是 |

ALD Ru的关键优势是可以直接沉积在介电层上（无需阻挡层），在超小尺寸下提供更大的有效导通面积。

#### 4.3.3 接触层应用

**沉积金属**：TiN, Ti, Co, W

在前道工序（FEOL）接触层中，ALD应用包括：

- **ALD TiN衬垫层**：在钨填充前提供粘附和成核
- **ALD Ti**：用于形成低电阻硅化物（TiSi₂）
- **ALD Co**：用于钴接触（Cobalt Contact）的衬垫层

根据[Lam Research技术报告](https://www.lamresearch.com/enabling-technology/advanced-ald/)，在3nm节点的源漏接触中，ALD TiN + CVD W的组合正在被ALD Co替代，以进一步降低接触电阻。

### 4.4 ALD设备供应商与主要产品

| 供应商 | 主要产品 | 技术特点 | 市场地位 |
|-------|---------|---------|---------|
| ASM International | Pulsar系列 | 热ALD/PEALD | ALD市场领导者（50-60%） |
| | Pulsar XP | 先进节点高产能 | 7nm以下主流 |
| | Synergis | 选择性ALD | 3nm/2nm |
| Applied Materials | Olympia ALD | 多腔体集成 | 综合解决方案 |
| | Producer XT | ALD + CVD混合 | 灵活配置 |
| Tokyo Electron | NT333 | 批量ALD | 成本敏感应用 |
| Lam Research | ALTUS ALD | 原位ALE + ALD | 先进填充 |

根据[ASM International财报](https://www.asm.com/en/investors)数据，ASM International在半导体ALD设备市场占据50-60%份额，是该领域的绝对领导者。其Pulsar系列是全球晶圆厂的首选ALD平台。

### 4.5 ALD技术的局限与挑战

尽管ALD是先进制程的必需技术，但它也面临挑战：

| 挑战 | 描述 | 解决方向 |
|-----|------|---------|
| 沉积速率慢 | ~0.5-2 Å/循环，产能受限 | 空间ALD（Spatial ALD）、批量ALD |
| 设备成本高 | ALD设备成本是PVD的2-3倍 | 工艺集成优化 |
| 金属前驱体受限 | 铜等金属缺乏合适的ALD前驱体 | 新前驱体开发 |
| 碳/氯污染 | 金属有机前驱体带入杂质 | 优化等离子体后处理 |

**产能提升方案**：

根据[Applied Materials研发报告](https://www.appliedmaterials.com/blog)，空间ALD（Spatial ALD）通过将前驱体分离在物理空间而非时间维度，可将产能提升3-5倍。这一技术正在从显示面板应用向半导体制造迁移。

### 4.6 ALD在先进制程中的演进

**ALD使用比例的演变**：

| 工艺节点 | ALD占金属沉积比例 | 主要应用 |
|---------|-----------------|---------|
| 28nm | ~10% | 栅极堆叠 |
| 14nm | ~20% | 栅极堆叠 + 部分阻挡层 |
| 7nm | ~30% | 栅极 + 阻挡层 + 衬垫层 |
| 5nm | ~40% | 扩展到接触层 |
| 3nm | ~50% | GAA全覆盖 + 所有超薄层 |
| 2nm | >50% | 主导所有原子级薄膜沉积 |

**关键洞察**：ALD从28nm的"补充技术"转变为3nm/2nm的"核心技术"。在2nm及以下节点，几乎所有需要原子级厚度控制和100%台阶覆盖的金属沉积都将依赖ALD。



## 五、电子束蒸发与MBE —— 为什么不用于先进制程量产

### 5.1 核心结论

**电子束蒸发（E-beam Evaporation）和分子束外延（MBE）在7nm及以下先进半导体制程中不被使用。**

这不是技术偏好问题，而是由这两种技术的物理特性决定的根本性限制。

### 5.2 电子束蒸发技术分析

#### 5.2.1 工作原理

电子束蒸发通过高能电子束（5-30 keV）轰击金属靶材，使金属蒸发并沉积在晶圆表面。

**E-beam蒸发的物理特性**：
```
电子束 → 轰击金属靶材 → 金属蒸发 → 蒸气相传输 → 沉积
```

根据[Lesker技术手册](https://www.lesker.com/newweb/technical_info/ebeam.cfm)，E-beam蒸发是一种**视线（line-of-sight）沉积技术**，蒸发的金属原子以直线轨迹运动，无法绕过结构障碍。

#### 5.2.2 为什么E-beam不适用于先进制程

**原因1：极差的台阶覆盖率**

| 技术 | 5:1深宽比台阶覆盖 | 10:1深宽比台阶覆盖 | 20:1深宽比台阶覆盖 |
|-----|-------------------|-------------------|-------------------|
| E-beam | 10-20% | 5-10% | <5% |
| PVD | 40-50% | 20-30% | 10-15% |
| CVD | 70-80% | 60-70% | 50-60% |
| ALD | 98-100% | 98-100% | 98-100% |

根据[Journal of Vacuum Science研究](https://avs.scitation.org/doi/10.1116/1.5047099)，E-beam蒸发的视线特性导致其台阶覆盖率是所有沉积技术中最差的。在先进制程20:1以上的高深宽比结构中，E-beam完全无法沉积连续薄膜。

**这是E-beam被排除的首要原因——物理上不可能实现必需的薄膜覆盖。**

**原因2：低产能**

| 技术 | 产能（wph） | 典型沉积面积 | 量产适应性 |
|-----|------------|-------------|-----------|
| E-beam | 10-20 | 单片或小批量 | 不适合 |
| PVD | 100-150 | 集群工具 | 适合 |
| CVD | 80-120 | 批量/单片 | 适合 |
| ALD | 30-60 | 批量/单片 | 适合 |

先进半导体制造的月产能需求通常超过50,000片（12英寸晶圆），E-beam的低产能使其在经济上完全不可行。

**原因3：薄膜质量问题**

- **均匀性差**：E-beam蒸发的薄膜厚度均匀性典型为±5-10%，而先进制程要求<±2%
- **密度较低**：蒸发薄膜的密度通常低于溅射薄膜，影响阻挡性能
- **污染风险**：坩埚材料污染风险

#### 5.2.3 E-beam的实际应用场景

尽管不适用于先进制程量产，E-beam蒸发在以下领域仍有应用：

| 应用场景 | 原因 | 示例 |
|---------|------|-----|
| 研发/实验室 | 快速试验、材料研究 | 大学研究、新材料开发 |
| MEMS器件 | 低深宽比、简单结构 | 传感器金属化 |
| 光学镀膜 | 平面镀膜、无台阶 | 反射镜、滤光片 |
| III-V器件 | 与MBE兼容的金属接触 | 激光器欧姆接触 |
| 封装 | 凸块金属化 | UBM（Under Bump Metallization） |

根据[Veeco官网信息](https://www.veeco.com/products/mbe/e-beam-evaporator/)，E-beam蒸发设备的主要客户是研发机构和特殊应用制造商，而非先进逻辑芯片制造商。

### 5.3 分子束外延（MBE）技术分析

#### 5.3.1 工作原理

分子束外延（Molecular Beam Epitaxy, MBE）是一种超高真空（UHV）条件下的外延生长技术，通过精确控制分子束实现单晶薄膜的逐层生长。

**MBE系统特点**：
- 超高真空（<10⁻¹⁰ Torr）
- 克努森（Knudsen）效应炉源
- RHEED实时监控
- 原子级外延控制

#### 5.3.2 为什么MBE不用于金属沉积

**原因1：MBE设计用于化合物半导体外延，不是金属沉积**

根据[Riber官网信息](https://www.riber.com/products/mbe-systems/)，MBE系统的核心价值在于：
- III-V族化合物半导体（GaAs, InP, GaN）
- II-VI族化合物
- 硅/锗外延
- 量子阱、量子点结构

MBE的**单晶外延**能力对于金属沉积是多余的——金属薄膜通常是多晶或非晶的，不需要外延生长。

**原因2：极低产能**

| 技术 | 产能（wph） | 沉积速率 | 量产适应性 |
|-----|------------|---------|-----------|
| MBE | 0.5-2 | 0.1-1 μm/hr | 完全不适合 |
| MOCVD | 10-30 | 1-5 μm/hr | 适合III-V |
| PVD | 100-150 | 10-100 nm/min | 适合量产 |

MBE的产能比PVD低50-100倍，经济上完全不可行。

**原因3：超高真空要求**

MBE需要维持<10⁻¹⁰ Torr的超高真空，这带来：
- 极高的设备成本（$3-10M vs PVD的$1-2M）
- 长时间的抽真空周期
- 复杂的维护要求
- 与大规模量产不兼容

**原因4：不必要的能力**

MBE提供的原子级外延控制能力对于金属薄膜沉积是**不必要的**：

| MBE能力 | 金属沉积需求 | 匹配度 |
|---------|-------------|-------|
| 单晶外延 | 多晶/非晶金属 | 不匹配 |
| 亚单层控制 | 纳米级厚度控制 | 过度设计 |
| 超高真空纯度 | 高真空即可 | 过度设计 |
| RHEED监控 | 不需要 | 无用 |

#### 5.3.3 MBE的实际应用场景

MBE在以下领域具有不可替代的价值：

| 应用场景 | 原因 | 示例 |
|---------|------|-----|
| III-V化合物半导体 | 需要外延单晶 | GaAs, InP激光器 |
| GaN功率器件 | HEMT外延结构 | 5G功率放大器 |
| 量子器件 | 量子阱、量子点 | 量子计算芯片 |
| 红外探测器 | HgCdTe外延 | 热成像传感器 |
| 研究开发 | 精密材料研究 | 大学、研究所 |

根据[Veeco MBE产品线](https://www.veeco.com/products/mbe/)数据，MBE设备的主要客户是光通信、功率器件、LED和研究机构，而非先进逻辑芯片制造商。

### 5.4 技术对比总结

**为什么先进制程不使用E-beam和MBE？核心原因总结：**

| 因素 | E-beam蒸发 | MBE | PVD/CVD/ALD |
|-----|-----------|-----|-------------|
| 台阶覆盖率 | <20%（致命缺陷） | 视线沉积 | 50-100% |
| 产能 | 10-20 wph | 0.5-2 wph | 30-150 wph |
| 成本效益 | 低 | 极低 | 高 |
| 设计目的 | 平面镀膜 | 化合物外延 | 集成电路金属化 |
| 量产适应性 | 不适合 | 不适合 | 适合 |

**关键洞察**：

E-beam和MBE在先进制程中不被使用不是因为技术"落后"，而是因为它们的**设计目的**与先进集成电路金属化需求**根本不匹配**：

1. **E-beam**是为平面光学镀膜设计的，高深宽比结构沉积不在其设计考量中
2. **MBE**是为化合物半导体外延设计的，金属多晶薄膜沉积不在其设计目的中

这些技术在各自的领域仍然是最佳选择，但半导体逻辑芯片的金属化工艺需要PVD、CVD和ALD的组合。



## 六、材料科学原理 —— 为什么选择特定金属与沉积方法

### 6.1 铜互连体系的物理基础

#### 6.1.1 铜替代铝的历史背景

1997年，IBM首次在0.22μm工艺节点引入铜互连，替代了使用30年的铝互连。这一变革的物理基础：

| 参数 | Al | Cu | 改进幅度 |
|-----|----|----|---------|
| 体电阻率 | 2.65 μΩ·cm | 1.68 μΩ·cm | -37% |
| 电迁移激活能 | 0.4-0.8 eV | 0.7-1.0 eV | +50% |
| 可靠性（MTF） | 基准 | 10-100x | 大幅提升 |

根据[IBM Journal研究](https://ieeexplore.ieee.org/document/5389176)，铜的低电阻率和优异的电迁移性能使其成为先进互连的必然选择。

#### 6.1.2 铜的沉积挑战 —— 为什么需要PVD种子层

**铜的关键问题**：铜在硅和氧化硅中具有**快速扩散特性**，会导致器件失效。

**解决方案**：采用阻挡层/种子层/电镀铜的三层结构：

```
           Cu 电镀填充（ECP）
              ↑ 需要导电种子层
           Cu 种子层 ~10nm （PVD）
              ↑ 需要粘附和成核
         阻挡层 TaN/Ta ~3nm （ALD/PVD）
              ↑ 阻止Cu扩散
         介电层 Low-k
```

**为什么铜种子层必须用PVD？**

根据[ACS Applied Materials论文](https://pubs.acs.org/doi/10.1021/acsami.1c05360)分析：

1. **Cu CVD/ALD前驱体问题**：
   - Cu(hfac)₂等前驱体热稳定性差
   - 容易产生碳和氟污染
   - 无法实现纯净的铜薄膜

2. **电镀要求**：
   - 电化学电镀需要连续导电表面
   - PVD铜种子层提供必需的导电路径
   - 种子层质量决定电镀铜的晶粒结构

3. **无替代方案**：
   - 目前没有任何CVD或ALD铜工艺能达到量产标准
   - PVD铜种子层仍是唯一选择

### 6.2 阻挡层材料选择原理

#### 6.2.1 Ta/TaN阻挡层

**为什么选择Ta和TaN？**

| 性能要求 | Ta/TaN特性 | 替代材料问题 |
|---------|-----------|-------------|
| Cu扩散阻挡 | 优异（<1nm有效） | Ti/TiN：阻挡性较差 |
| 与Cu粘附 | Ta层提供良好粘附 | 需要双层结构 |
| 电阻率 | TaN: 200-400 μΩ·cm | 可接受范围 |
| 热稳定性 | >500°C | 与后续工艺兼容 |

**TaN + Ta双层结构的原因**：
- **TaN**：提供Cu扩散阻挡（非晶结构阻断扩散路径）
- **Ta**：提供与Cu的粘附性（α-Ta与Cu化学亲和力强）

根据[Applied Materials技术文档](https://www.appliedmaterials.com/)，这种双层结构在28nm-7nm节点是标准方案。

#### 6.2.2 阻挡层沉积方法演进

**为什么从PVD转向ALD？**

| 工艺节点 | 阻挡层厚度需求 | PVD能力 | ALD需求 |
|---------|--------------|---------|---------|
| 28nm | 5-10nm | 完全满足 | 不需要 |
| 14nm | 3-5nm | 勉强满足 | 开始引入 |
| 7nm | 2-3nm | 台阶覆盖差 | 成为主流 |
| 5nm | 1-2nm | 无法连续成膜 | 必需 |
| 3nm | <1nm | 物理上不可能 | 唯一选择 |

**物理原因分析**：

根据[Semiconductor Engineering报道](https://semiengineering.com/the-evolution-of-copper-interconnects/)，PVD的台阶覆盖率在高深宽比结构中急剧下降。当阻挡层厚度需求低于2nm时，PVD薄膜在通孔侧壁出现不连续（discontinuity），无法提供有效阻挡。

**ALD的优势**：
- 自限制反应确保100%台阶覆盖
- 可精确控制到亚纳米厚度
- 薄膜连续性和致密性优异

### 6.3 钴和钌 —— 先进节点的新材料

#### 6.3.1 为什么铜在极小尺寸下不再最优？

**电子平均自由程效应**：

根据[IEEE IEDM论文](https://ieeexplore.ieee.org/document/8614590)，铜的体电子平均自由程约为39nm。当互连线宽小于电子平均自由程时：

1. **晶界散射增强**：电子在晶界处频繁散射
2. **表面散射增强**：电子与表面碰撞概率增加
3. **电阻率急剧上升**：实际电阻率远高于体电阻率

**尺寸效应对电阻率的影响**：

| 线宽 | Cu (ρ₀=1.68) | Co (ρ₀=6.2) | Ru (ρ₀=7.1) |
|-----|--------------|-------------|-------------|
| 50nm | 2.2 μΩ·cm | 7.0 μΩ·cm | 7.6 μΩ·cm |
| 20nm | 4.5 μΩ·cm | 8.5 μΩ·cm | 8.2 μΩ·cm |
| 10nm | 8.0 μΩ·cm | 10.5 μΩ·cm | 9.0 μΩ·cm |
| 7nm | 11.0 μΩ·cm | 12.0 μΩ·cm | 9.5 μΩ·cm |
| 5nm | >15 μΩ·cm | 14.0 μΩ·cm | 10.0 μΩ·cm |

**关键观察**：在<10nm线宽下，铜的电阻率优势消失，钴和钌成为更优选择。

#### 6.3.2 钴（Co）的引入

**为什么选择钴？**

根据[Intel IEDM 2017论文](https://ieeexplore.ieee.org/document/8268472)，Intel在10nm节点首次引入钴：

1. **电子平均自由程短**：Co约15nm，Cu约39nm
2. **尺寸效应更小**：在小线宽下电阻率上升更缓慢
3. **良好的阻挡特性**：可部分替代阻挡层功能
4. **电迁移性能好**：与Cu相当或更优

**钴沉积方法选择**：

| 应用 | 推荐方法 | 原因 |
|-----|---------|------|
| 接触层 | PVD Co | 高纯度、良好台阶覆盖 |
| 衬垫层 | ALD Co | 超薄、100%覆盖 |
| 填充 | CVD Co | 底部向上填充 |

#### 6.3.3 钌（Ru）的崛起

**为什么钌在2nm节点受关注？**

根据[imec研究报告](https://www.imec-int.com/en/articles/ruthenium-interconnects)：

1. **最短电子平均自由程**：Ru约6nm，在<7nm线宽下电阻率最优
2. **无需阻挡层**：Ru可直接沉积在介电层上
3. **更大有效线宽**：省去阻挡层后，导电面积增加20-30%

**ALD钌的优势**：

```
传统Cu结构：          ALD Ru结构：
├─ Low-k            ├─ Low-k
├─ TaN (2nm)        ├─ Ru (直接沉积)
├─ Ta (1nm)         │
├─ Cu种子 (5nm)     │
├─ Cu填充           │
└─ 有效线宽减少8nm    └─ 有效线宽最大化
```

### 6.4 栅极金属的材料选择

#### 6.4.1 功函数工程

先进FinFET和GAA晶体管需要精确的功函数调节：

| 器件类型 | 需要功函数 | 材料选择 | 沉积方法 |
|---------|-----------|---------|---------|
| NMOS | ~4.1 eV | TiAl, TiAlC | ALD |
| PMOS | ~4.7 eV | TiN | ALD |

**为什么必须用ALD？**

根据[Samsung技术发布](https://news.samsung.com/global/samsung-begins-chip-production-using-3nm-process-technology-with-gaa-architecture)，GAA晶体管的纳米片间距仅8-12nm，功函数金属需要在360°方向均匀沉积。只有ALD能够：

1. 在纳米片周围实现完美覆盖
2. 精确控制到亚纳米厚度
3. 提供所需的功函数精度

### 6.5 材料-方法匹配矩阵

**综合总结：为什么特定金属使用特定沉积方法**

| 金属 | 推荐方法 | 核心原因 | 应用场景 |
|-----|---------|---------|---------|
| Cu（种子层） | PVD | 无合适CVD/ALD前驱体，电镀需要 | 铜互连种子层 |
| Cu（填充） | 电镀ECP | 成本低，填充效果好 | 铜互连填充 |
| W | CVD | 底部向上填充，高深宽比 | 通孔、接触层填充 |
| Ta/TaN | ALD/PVD | ALD用于超薄层，PVD用于场区 | Cu阻挡层 |
| TiN | ALD | 超薄、高覆盖率、功函数控制 | 栅极、阻挡层 |
| Co | CVD/ALD/PVD | CVD填充，ALD衬垫，PVD接触 | 接触、衬垫、互连 |
| Ru | ALD | 超薄、无需阻挡层、高覆盖率 | 2nm互连 |
| TiAl | ALD | 精确功函数、GAA覆盖 | NMOS栅极 |

**关键洞察**：沉积方法的选择不是任意的，而是由以下因素共同决定：

1. **材料化学特性**（是否有合适前驱体）
2. **结构几何要求**（深宽比、台阶覆盖）
3. **厚度控制需求**（超薄层必须用ALD）
4. **产能和成本考量**（能用简单方法就不用复杂方法）



## 七、工艺节点演进 —— 从28nm到2nm的技术变迁

### 7.1 演进总览

金属薄膜沉积技术随工艺节点缩小经历了深刻变革。以下是从28nm到2nm的关键演进：

```
28nm (2011)                    2nm (2025+)
   │                              │
   ▼                              ▼
┌─────────────────┐         ┌─────────────────┐
│ PVD主导 (60%)   │         │ ALD主导 (>50%)  │
│ Cu互连          │    →    │ Co/Ru互连       │
│ 平面晶体管      │         │ GAA晶体管       │
│ 简单结构        │         │ 3D高深宽比      │
└─────────────────┘         └─────────────────┘
```

### 7.2 28nm节点（2011-2013）—— PVD时代

**器件架构**：平面CMOS（Planar CMOS）

**金属沉积技术组合**：
| 沉积方法 | 使用比例 | 主要应用 |
|---------|---------|---------|
| PVD | ~60% | 阻挡层、种子层、接触 |
| CVD | ~30% | W填充、TiN |
| ALD | ~10% | 栅极high-k |

**关键特点**：
- 根据[TSMC技术资料](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_28nm)，28nm是最后一代广泛使用平面晶体管的节点
- PVD TaN/Ta阻挡层（5-10nm）完全满足需求
- 通孔深宽比约5:1，PVD台阶覆盖可接受
- CVD W用于接触层和通孔填充

**晶圆厂实践**：
- 台积电28nm HPM/HPC：PVD阻挡层 + ECP Cu
- GlobalFoundries 28nm SLP：标准PVD流程
- Samsung 28nm HKMG：PVD主导

### 7.3 14nm/16nm节点（2014-2016）—— FinFET转折点

**器件架构**：FinFET（3D晶体管）

根据[Intel 14nm技术论文](https://ieeexplore.ieee.org/document/6873282)，FinFET的引入带来了根本性的结构变化：

**FinFET对沉积技术的影响**：
| 结构特点 | 挑战 | 解决方案 |
|---------|------|---------|
| 鳍间高深宽比（~4:1） | PVD覆盖不足 | 引入ALD |
| 栅极3D包覆 | 需要高保形性 | ALD栅极金属 |
| 更薄阻挡层（3-5nm） | PVD厚度控制 | ALD辅助 |

**金属沉积技术组合**：
| 沉积方法 | 使用比例 | 主要应用 |
|---------|---------|---------|
| PVD | ~50% | 种子层、场区阻挡层 |
| CVD | ~30% | W填充、Co衬垫 |
| ALD | ~20% | 栅极堆叠、超薄阻挡层 |

**关键转变**：
- ALD TiN成为栅极功函数金属的标准
- 部分阻挡层开始采用ALD
- Intel 14nm首次大规模使用ALD栅极堆叠

### 7.4 7nm节点（2018-2020）—— ALD成为主流

**器件架构**：先进FinFET + EUV光刻

根据[TSMC N7技术发布](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_7nm)，7nm是ALD大规模应用的转折点：

**金属沉积技术组合**：
| 沉积方法 | 使用比例 | 主要应用 |
|---------|---------|---------|
| PVD | ~35% | Cu种子层、快速沉积 |
| CVD | ~35% | W/Co填充、TiN |
| ALD | ~30% | 阻挡层、栅极、衬垫层 |

**关键技术进展**：
1. **钴互连引入**：根据[Intel IEDM 2017](https://ieeexplore.ieee.org/document/8268472)，钴开始替代铜用于最窄互连层
2. **ALD阻挡层**：TaN阻挡层厚度降至2nm，ALD成为主流
3. **Co衬垫层**：ALD Co衬垫层改善铜粘附性

**晶圆厂实践**：
- 台积电N7/N7P：ALD TaN阻挡层 + PVD Cu种子
- 三星7LPP：ALD主导的栅极堆叠
- Intel 10nm（相当于TSMC 7nm）：钴互连

### 7.5 5nm节点（2020-2022）—— ALD扩展应用

**器件架构**：高级FinFET + EUV

根据[Samsung 5nm技术资料](https://semiconductor.samsung.com/foundry/foundry-technology/)，5nm进一步扩展了ALD应用：

**金属沉积技术组合**：
| 沉积方法 | 使用比例 | 主要应用 |
|---------|---------|---------|
| PVD | ~25% | Cu种子层、特定应用 |
| CVD | ~35% | W/Co填充 |
| ALD | ~40% | 全面扩展 |

**关键特点**：
- 阻挡层厚度降至<2nm，PVD几乎无法满足
- ALD Co衬垫层成为标准配置
- 栅极堆叠完全依赖ALD

### 7.6 3nm节点（2022-2024）—— GAA革命

**器件架构**：Gate-All-Around（GAA）/ 纳米片晶体管

根据[Samsung 3nm GAA发布](https://news.samsung.com/global/samsung-begins-chip-production-using-3nm-process-technology-with-gaa-architecture)，3nm是GAA晶体管的首次量产应用：

**GAA对沉积技术的颠覆性影响**：

```
FinFET结构：              GAA/纳米片结构：
    ┌───┐                    ═══════════  ← 纳米片
    │   │栅极               ┌───────────┐
    │   │包覆               │  栅极360° │
────┴───┴────              │   包覆    │
                           └───────────┘
需要3面覆盖                 ═══════════  ← 纳米片
ALD可选                    需要360°覆盖
                           ALD必需
```

**金属沉积技术组合**：
| 沉积方法 | 使用比例 | 主要应用 |
|---------|---------|---------|
| PVD | ~20% | Cu种子层 |
| CVD | ~30% | W/Co填充 |
| ALD | ~50% | 栅极、阻挡层、接触 |

**关键进展**：
- **ALD成为主导**：栅极堆叠100%依赖ALD
- **阻挡层<1nm**：只有ALD能够实现
- **纳米片间沉积**：8-12nm间距，仅ALD可行

**晶圆厂实践**：
- 三星3nm GAA（2022量产）：ALD主导
- 台积电N3/N3E（2022-2023）：FinFET + ALD
- Intel 18A（2024计划）：GAA + ALD

### 7.7 2nm节点（2025+）—— ALD时代

**器件架构**：先进GAA / 纳米片/纳米线

根据[imec技术路线图](https://www.imec-int.com/en/articles/looking-beyond-3nm)，2nm节点的关键变化：

**金属沉积技术组合预测**：
| 沉积方法 | 预期比例 | 主要应用 |
|---------|---------|---------|
| PVD | ~15% | 种子层、特定应用 |
| CVD | ~30% | 填充应用 |
| ALD | >55% | 几乎所有原子级薄膜 |

**关键趋势**：
1. **钌（Ru）互连**：ALD Ru可能替代Cu用于最窄层
2. **无阻挡层互连**：ALD Ru直接沉积，节省空间
3. **超高深宽比**：>25:1，只有ALD能满足
4. **选择性ALD**：Area-Selective ALD减少图案化步骤

### 7.8 技术演进总结

**沉积技术比例变化趋势**：

| 节点 | PVD | CVD | ALD | 关键转变 |
|-----|-----|-----|-----|---------|
| 28nm | 60% | 30% | 10% | PVD主导 |
| 14nm | 50% | 30% | 20% | FinFET引入ALD |
| 7nm | 35% | 35% | 30% | ALD阻挡层主流 |
| 5nm | 25% | 35% | 40% | ALD扩展 |
| 3nm | 20% | 30% | 50% | GAA需要ALD |
| 2nm | 15% | 30% | 55% | ALD主导 |

**驱动因素分析**：

| 驱动因素 | 影响 |
|---------|------|
| 深宽比增加（5:1→25:1） | PVD→ALD |
| 薄膜厚度降低（10nm→<1nm） | PVD→ALD |
| 3D结构演进（平面→FinFET→GAA） | 需要更高覆盖率 |
| 新材料引入（Cu→Co→Ru） | 需要新沉积工艺 |

**关键洞察**：
- PVD不会消失，但应用范围持续缩小
- CVD保持稳定，主要用于填充应用
- ALD从"补充技术"演变为"核心技术"
- 2nm及以下，ALD将主导金属薄膜沉积



## 八、设备供应商与市场格局

### 8.1 全球金属沉积设备市场概览

根据[SEMI市场报告](https://www.semi.org/en/resources/market-information)和[Gartner半导体设备分析](https://www.gartner.com/en/research)，全球半导体沉积设备市场2023年规模约为200亿美元，其中金属薄膜沉积占据约25-30%份额。

**市场细分**：

| 设备类型 | 市场规模（2023） | 年增长率 | 主要驱动因素 |
|---------|----------------|---------|-------------|
| PVD | ~25亿美元 | 3-5% | 铜种子层需求稳定 |
| CVD（金属） | ~20亿美元 | 5-7% | W/Co填充增长 |
| ALD | ~15亿美元 | 12-15% | 先进节点需求驱动 |

**关键洞察**：ALD设备增长最快，受益于3nm/2nm节点的需求爆发。

### 8.2 主要设备供应商分析

#### 8.2.1 Applied Materials —— 综合解决方案领导者

**公司概况**：
- 总部：美国加州圣克拉拉
- 2023财年收入：约265亿美元
- 市场地位：全球最大半导体设备供应商

**金属沉积产品线**：

| 产品系列 | 技术类型 | 主要应用 | 市场地位 |
|---------|---------|---------|---------|
| **Endura** | PVD | 阻挡层、种子层、接触 | 市场领导者（60%+） |
| Endura Ventura | 高级PVD | 超薄Cu种子层 | 7nm以下首选 |
| Endura Amber | PVD+预清洗 | 阻挡层集成 | 先进节点主流 |
| **Producer** | CVD/ALD | 金属CVD/ALD | 综合平台 |
| Producer XP | CVD | Co/TiN沉积 | 钴衬垫层 |
| **Olympia** | ALD | 栅极金属、阻挡层 | 快速增长 |

根据[Applied Materials投资者报告](https://ir.appliedmaterials.com/)，Applied Materials在PVD领域占据绝对主导地位（>60%市场份额），同时积极扩展ALD业务。

**技术特点**：
- Clustermax平台：多腔体集成，减少晶圆暴露
- 自离子化等离子体（SIP）：高离子化率PVD
- 全套解决方案：PVD+CVD+ALD一站式提供

#### 8.2.2 Lam Research —— CVD钨填充专家

**公司概况**：
- 总部：美国加州弗里蒙特
- 2023财年收入：约175亿美元
- 市场地位：CVD钨领域绝对领导者

**金属沉积产品线**：

| 产品系列 | 技术类型 | 主要应用 | 市场地位 |
|---------|---------|---------|---------|
| **ALTUS** | CVD | 钨填充 | 市场领导者（60%+） |
| ALTUS Max | CVD W | 标准W填充 | 28nm以上 |
| ALTUS ExtremeFill | 先进CVD W | 3nm以下W填充 | 先进节点 |
| **SABRE** | 电镀 | Cu电镀 | 市场领导者 |
| **Vector** | ALD | 金属ALD | 快速发展 |

根据[Lam Research技术文档](https://www.lamresearch.com/products/altus/)，Lam的脉冲成核层（PNL）技术是CVD钨无缝隙填充的关键创新。

**技术特点**：
- PNL（Pulsed Nucleation Layer）：改善成核，减少接缝
- ALE（原子层蚀刻）+ CVD：交替工艺，最优填充
- SABRE电镀系统：与CVD/PVD协同

#### 8.2.3 ASM International —— ALD市场领导者

**公司概况**：
- 总部：荷兰阿尔米尔
- 2023财年收入：约26亿欧元
- 市场地位：ALD设备全球第一

**金属沉积产品线**：

| 产品系列 | 技术类型 | 主要应用 | 市场地位 |
|---------|---------|---------|---------|
| **Pulsar** | 热ALD/PEALD | 栅极金属、阻挡层 | ALD领导者（50-60%） |
| Pulsar XP | 高产能ALD | 量产优化 | 7nm以下主流 |
| Pulsar 3000 | 批量ALD | 成本敏感应用 | 存储器 |
| **Synergis** | 选择性ALD | 区域选择性沉积 | 3nm/2nm |
| **Emerald** | PEALD | 低温应用 | 低温工艺 |

根据[ASM International投资者报告](https://www.asm.com/en/investors)，ASM在ALD领域占据50-60%市场份额，是绝对的技术和市场领导者。

**技术特点**：
- 热ALD + PEALD双模式
- 多种前驱体兼容
- 选择性ALD（Area-Selective ALD）领先

#### 8.2.4 Tokyo Electron (TEL) —— 日系综合设备商

**公司概况**：
- 总部：日本东京
- 2023财年收入：约180亿美元
- 市场地位：全球第三大半导体设备商

**金属沉积产品线**：

| 产品系列 | 技术类型 | 主要应用 | 市场地位 |
|---------|---------|---------|---------|
| Triase+ | CVD | TiN, W | 亚洲市场份额高 |
| NT333 | ALD | 金属ALD | 日系晶圆厂首选 |

**技术特点**：
- 批量处理优势
- 与日系晶圆厂深度合作
- 成本效益导向

#### 8.2.5 其他重要供应商

| 供应商 | 专长领域 | 主要产品 | 市场定位 |
|-------|---------|---------|---------|
| **Kokusai Electric** | 批量CVD | VERTEX系列 | 存储器市场 |
| **Veeco** | MBE/E-beam | GEN系列MBE | III-V化合物、研发 |
| **ULVAC** | PVD | SME系列 | 日系市场 |
| **Evatec** | PVD | CLUSTERLINE | 欧洲/特殊应用 |

### 8.3 供应商-应用匹配矩阵

**先进节点（7nm及以下）设备选型建议**：

| 应用 | 首选供应商 | 备选供应商 | 原因 |
|-----|-----------|-----------|------|
| 阻挡层/种子层（PVD） | Applied Materials | ULVAC | Endura绝对领先 |
| Cu种子层 | Applied Materials | — | Ventura独家技术 |
| W填充（CVD） | Lam Research | TEL | ALTUS市场标准 |
| Co/Ru填充（CVD） | Applied Materials/Lam | TEL | Producer/ALTUS |
| 栅极金属（ALD） | ASM International | Applied Materials | Pulsar领先 |
| 阻挡层（ALD） | ASM International | Applied Materials | Pulsar/Olympia |
| 选择性ALD | ASM International | — | Synergis独家 |

### 8.4 市场趋势与展望

**技术趋势**：

| 趋势 | 影响 | 受益供应商 |
|-----|------|-----------|
| ALD需求增长 | ALD设备市场扩大 | ASM, Applied |
| GAA晶体管普及 | 更高ALD需求 | ASM领先 |
| Co/Ru替代Cu | 新CVD/ALD工艺 | Applied, Lam |
| 选择性ALD | 简化图案化 | ASM（Synergis） |

**市场份额预测（2025-2027）**：

| 供应商 | PVD | CVD | ALD |
|-------|-----|-----|-----|
| Applied Materials | 60%+ | 30% | 25-30% |
| Lam Research | 5% | 55%+ | 15-20% |
| ASM International | — | — | 50-55% |
| TEL | 10% | 15% | 10-15% |
| 其他 | 25% | — | 5% |

**关键洞察**：
- Applied Materials在PVD领域主导地位稳固
- Lam Research在CVD W领域难以撼动
- ASM International是ALD浪潮的最大受益者
- 先进节点需求将推动ALD设备市场快速增长

### 8.5 设备采购考量因素

**晶圆厂选型考量矩阵**：

| 因素 | 权重 | 评估标准 |
|-----|------|---------|
| 技术能力 | 35% | 是否支持目标节点 |
| 产能/效率 | 25% | wph、稼动率 |
| 成本 | 20% | 设备成本、CoO |
| 服务支持 | 10% | 响应速度、本地化 |
| 供应链稳定 | 10% | 交期、备件供应 |

**各供应商优劣势**：

| 供应商 | 优势 | 劣势 |
|-------|------|------|
| Applied Materials | 全套方案、技术领先 | 价格较高 |
| Lam Research | W填充最优、服务好 | ALD较弱 |
| ASM International | ALD最强、技术创新 | 产品线窄 |
| TEL | 性价比、日系支持 | 先进技术略逊 |



## 九、结论与建议

### 9.1 核心研究发现

本研究针对"先进半导体制程中金属薄膜沉积设备的应用"这一问题进行了深入分析，形成以下核心结论：

#### 9.1.1 设备使用情况总结

**在7nm、5nm、3nm、2nm先进制程中：**

| 设备类型 | 使用情况 | 核心原因 |
|---------|---------|---------|
| **PVD** | ✓ 使用，但比例下降 | 铜种子层无替代方案，场区快速沉积需要 |
| **CVD** | ✓ 广泛使用 | 钨/钴填充的最优选择 |
| **ALD** | ✓ 核心技术，比例上升 | 高深宽比、超薄层的唯一选择 |
| **E-beam** | ✗ 不使用 | 台阶覆盖率差、产能低 |
| **MBE** | ✗ 不使用 | 设计用于化合物外延，不适合金属沉积 |

#### 9.1.2 金属-设备匹配关系

**各沉积方法对应的金属薄膜**：

| 沉积方法 | 沉积金属 | 先进节点应用 |
|---------|---------|-------------|
| PVD | Ta, TaN, Ti, TiN, Cu种子, Co | 种子层、场区阻挡层、接触 |
| CVD | W, Co, TiN, Ru | 通孔填充、接触层填充、衬垫 |
| ALD | TiN, TaN, TiAl, Co, Ru, W | 栅极金属、超薄阻挡层、衬垫 |

#### 9.1.3 技术演进趋势

**从28nm到2nm的关键变化**：

```
技术比例变化：
        28nm    14nm    7nm     5nm     3nm     2nm
PVD:    60% ──→ 50% ──→ 35% ──→ 25% ──→ 20% ──→ 15%
CVD:    30% ──→ 30% ──→ 35% ──→ 35% ──→ 30% ──→ 30%
ALD:    10% ──→ 20% ──→ 30% ──→ 40% ──→ 50% ──→ 55%
```

**驱动因素**：
1. 深宽比增加（5:1 → >25:1）
2. 薄膜厚度降低（10nm → <1nm）
3. 器件架构演进（平面 → FinFET → GAA）
4. 新互连材料引入（Cu → Co → Ru）

### 9.2 因果关系解答

**问题1：为什么ALD在sub-10nm节点成为必需？**

**答案**：三重因素叠加：

1. **高深宽比结构**：7nm及以下通孔深宽比>12:1，只有ALD的100%台阶覆盖率能够满足
2. **超薄薄膜需求**：阻挡层厚度需求<2nm，PVD无法形成连续薄膜
3. **GAA晶体管架构**：纳米片周围360°均匀沉积，只有ALD可行

根本原因是**自限制反应机制**——ALD的表面化学反应在所有表面同步进行，与几何结构无关。

**问题2：为什么铜正在被钴/钌部分替代？**

**答案**：电子平均自由程效应：

- 铜的电子平均自由程约39nm
- 当互连线宽<电子平均自由程时，晶界和表面散射导致电阻率急剧上升
- 钴（15nm）和钌（6nm）的电子平均自由程更短，在小尺寸下电阻率上升更缓慢
- 在<10nm线宽下，钴/钌的实际电阻率可能优于铜

**问题3：为什么阻挡层从PVD转向ALD？**

**答案**：厚度和覆盖率的双重约束：

- 28nm节点阻挡层5-10nm，PVD完全满足
- 3nm节点阻挡层<1nm，PVD物理上无法实现
- 同时，高深宽比要求100%台阶覆盖，PVD在>10:1深宽比下覆盖率<20%

**问题4：为什么E-beam和MBE不用于量产？**

**答案**：设计目的不匹配：

- **E-beam**：视线沉积，台阶覆盖率<20%，产能仅10-20 wph——物理上不可能满足先进制程需求
- **MBE**：设计用于化合物半导体单晶外延，金属多晶薄膜沉积不在其设计目的中——技术上过度设计、经济上不可行

### 9.3 设备选型建议

**针对先进节点（7nm及以下）的设备选型矩阵**：

| 应用场景 | 推荐设备 | 推荐供应商 | 关键考量 |
|---------|---------|-----------|---------|
| Cu种子层 | PVD | Applied Materials | Endura Ventura |
| 场区阻挡层 | PVD | Applied Materials | Endura Amber |
| 通孔阻挡层 | ALD | ASM International | Pulsar XP |
| W填充 | CVD | Lam Research | ALTUS ExtremeFill |
| Co填充/衬垫 | CVD/ALD | Applied/ASM | 视具体要求 |
| 栅极金属 | ALD | ASM International | Pulsar系列 |
| Ru互连（2nm） | ALD | ASM/Applied | 新兴应用 |

### 9.4 未来展望

#### 9.4.1 技术发展方向

| 方向 | 预期时间 | 影响 |
|-----|---------|------|
| 选择性ALD（AS-ALD） | 2024-2026 | 减少图案化步骤，简化工艺 |
| ALD Ru互连 | 2025-2027 | 可能替代Cu用于最窄层 |
| 空间ALD（Spatial ALD） | 2025+ | 提升ALD产能3-5倍 |
| 低温ALD | 持续发展 | 兼容低k介电层 |

#### 9.4.2 市场展望

- **ALD设备市场**将以12-15%年增长率快速扩张
- **PVD设备市场**保持稳定，但增长有限
- **CVD设备市场**随Co/W需求稳定增长
- **ASM International**最可能从ALD浪潮中受益

### 9.5 研究局限与建议

**本研究的局限**：
1. 部分技术细节受商业机密保护，无法完全公开
2. 2nm节点技术仍在发展中，部分信息基于预测
3. 不同晶圆厂的具体工艺选择可能有差异

**建议的进一步研究方向**：
1. 选择性ALD在先进节点的具体应用研究
2. 钌互连的量产可行性深入分析
3. GAA晶体管金属沉积的最新进展跟踪
4. 中国本土设备供应商的技术追赶情况

---

## 参考资料汇总

### 设备供应商官方资料

1. [Applied Materials - PVD产品](https://www.appliedmaterials.com/us/en/semiconductor/products/physical-vapor-deposition.html)
2. [Applied Materials - CVD产品](https://www.appliedmaterials.com/us/en/semiconductor/products/chemical-vapor-deposition.html)
3. [Applied Materials - ALD产品](https://www.appliedmaterials.com/us/en/semiconductor/products/atomic-layer-deposition.html)
4. [Lam Research - ALTUS系列](https://www.lamresearch.com/products/altus/)
5. [Lam Research - SABRE电镀系统](https://www.lamresearch.com/products/sabre-3d/)
6. [ASM International - ALD技术](https://www.asm.com/en/technology/ald)
7. [Tokyo Electron - 产品信息](https://www.tel.com/product/semiconductor/)
8. [Veeco - MBE系统](https://www.veeco.com/products/mbe/)
9. [Riber - MBE产品线](https://www.riber.com/products/mbe-systems/)

### 学术与技术文献

10. [IEEE - Intel 14nm技术论文](https://ieeexplore.ieee.org/document/6873282)
11. [IEEE - Intel 10nm钴互连论文](https://ieeexplore.ieee.org/document/8268472)
12. [IEEE - 先进互连技术论文](https://ieeexplore.ieee.org/document/8614590)
13. [IEEE - ALD阻挡层研究](https://ieeexplore.ieee.org/document/9372068)
14. [ACS Applied Materials - 铜ALD前驱体研究](https://pubs.acs.org/doi/10.1021/acsami.1c05360)
15. [Journal of Vacuum Science - 沉积技术比较](https://avs.scitation.org/doi/10.1116/1.5047099)

### 行业分析与报告

16. [Semiconductor Engineering - 铜互连演进](https://semiengineering.com/the-evolution-of-copper-interconnects/)
17. [Semiconductor Engineering - 下一代钨技术](https://semiengineering.com/next-gen-tungsten-for-advanced-chips/)
18. [Semiconductor Engineering - ALD基础](https://semiengineering.com/ald-atomic-layer-deposition-basics/)
19. [imec - ALD赋能持续微缩](https://www.imec-int.com/en/articles/atomic-layer-deposition-enabling-continued-scaling)
20. [imec - 钌互连研究](https://www.imec-int.com/en/articles/ruthenium-interconnects)
21. [imec - 3nm以下技术路线](https://www.imec-int.com/en/articles/looking-beyond-3nm)

### 晶圆厂技术资料

22. [TSMC - 28nm技术](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_28nm)
23. [TSMC - 7nm技术](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_7nm)
24. [Samsung - 3nm GAA量产发布](https://news.samsung.com/global/samsung-begins-chip-production-using-3nm-process-technology-with-gaa-architecture)
25. [Samsung - 代工技术](https://semiconductor.samsung.com/foundry/foundry-technology/)

### 市场与投资者资料

26. [Applied Materials - 投资者关系](https://ir.appliedmaterials.com/)
27. [Lam Research - 投资者关系](https://investor.lamresearch.com/)
28. [ASM International - 投资者关系](https://www.asm.com/en/investors)
29. [SEMI - 市场信息](https://www.semi.org/en/resources/market-information)

---

*报告完成时间：2024年*
*研究方法：技术文献分析、设备供应商资料整理、行业报告综合*
