# 3033-061
CSCI-GA 3033-061Final Project

# **融合多模态信息的电影推荐系统 (Multimodal Movie Recommendation System) 项目企划书**

## **摘要 (Abstract)**

随着多媒体内容的爆炸式增长，传统的推荐系统在帮助用户筛选个性化电影内容时面临挑战。现有系统大多依赖单一的评分数据或稀疏的文本元数据（如类型、演员），难以捕捉影响用户偏好的深层叙事风格、视觉元素和情感共鸣。本项目旨在设计并实现一个**融合多模态信息 (multimodal information)** 的电影推荐系统，以解决上述问题。

系统将综合利用多种数据源：包括电影的**元数据 (metadata)**、从预告片和正片中提取的**代表性视觉帧 (representative still frames)**、剧情摘要、以及深度的**用户评论 (user reviews)**。技术上，我们将采用预训练的**视觉变换器 (Vision Transformer, ViT)** 来提取图像特征，并利用**大型语言模型 (Large Language Models, LLM)** 对剧情和用户评论等长文本进行深度分析与摘要。最终，通过一个**基于注意力机制的融合模块 (attention-based fusion module)**，动态地结合不同模态的特征，生成更精准、更多样化且更具个性化的电影推荐。我们期望通过**消融实验 (ablation studies)** 证明多模态融合，特别是深度视觉和文本语义信息的引入，能显著提升推荐系统的性能和用户体验。

## **1. 问题陈述 (Problem Statement)**

当前电影推荐系统主要面临以下挑战：

* **数据单一与稀疏**：传统推荐系统严重依赖用户-项目评分矩阵或稀疏的元数据（如类型、演员），信息维度不足。
* **忽略深层特征**：它们难以捕捉到影响用户偏好的深层叙事风格 (narrative)、视觉美学 (visual aesthetics) 或情感基调 (stylistic/tone)，而这些往往是用户做出选择的关键。
* **用户反馈利用不充分**：系统常常忽略评论和讨论中蕴含的丰富情感 (sentiment) 和观点 (reasoning)，错失了理解用户真实想法的机会。
* **冷启动与偏见问题**：**冷启动 (Cold-start)** 和**流行度偏见 (popularity bias)** 问题依然严峻，导致推荐结果趋于重复和浅薄。
* **标签相似度的局限性**：仅基于标签的相似度计算，可能会推荐出主题相似但风格、基调迥异的电影，无法满足用户多样化的品味。

## **2. 项目目标与计划 (Project Goals & Plan)**

为应对上述挑战，本项目的核心计划如下：

* **开发多模态融合模型**：构建一个能够有效融合视觉与文本特征的推荐模型，以实现更深度的个性化。
* **超越传统视觉材料**：不止步于海报和预告片，我们将通过算法**挑选更具代表性的视频帧 (representative video frames)**，并引入更长的内容形式，如YouTube上的**剧情讲解 (plot explanations)** 和深度影评。
* **利用大型语言模型 (LLM)**：应用先进的LLM来自动**概括和分析 (summarize and analyze)** 复杂的电影剧情和海量用户评论，提取核心观点和情感。
* **提取深层语义**：利用自然语言处理（NLP）技术从文本中提取**情感倾向 (sentiment)** 和**主题 (themes)**，为推荐提供更丰富的决策依据。
* **采用注意力融合机制**：应用**基于注意力的融合技术 (attention-based fusion techniques)**，让模型能够自适应地权衡不同模态信息的重要性，实现更智能的特征组合。

## **3. 数据源与采集 (Data Sources & Collection)**

为了构建一个全面的多模态数据集，我们将从以下渠道采集数据，对应于您的系统设计图：

| 数据类型 (Data Type) | 描述 (Description) | 来源与采集方式 (Source & Collection Method) |
| :--- | :--- | :--- |
| **元数据 (Metadata)** | 电影的基本信息，如类型、导演、演员、年份、时长等。 | IMDb, TMDB API (例如使用 `Cinemagoer` 库) |
| **视觉内容 (Visual Content)** | 电影海报、预告片、以及最具代表性的正片静态截图。 | 通过自动化脚本从TMDB下载高清海报和背景图，并截取视频关键帧。 |
| **剧情与文本 (Plots & Text)** | 官方剧情简介、社区贡献的详细剧情、以及预告片字幕。 | IMDb/TMDB API获取简介，利用LLM API (如GROK, OpenAI) 丰富或生成更详细的剧情摘要。 |
| **用户评论 (User Reviews)** | 用户的文字评论和评分。 | 从IMDb, MovieLens等平台收集，是提取用户情感和偏好的关键。 |
| **社交媒体内容 (Social Media)** | (可选扩展) YouTube上的影评视频、影迷讨论等。 | YouTube Data API，用于提取视频字幕和分析社区热点。 |

## **4. 技术方案与模型架构 (Technical Approach)**

本项目的核心技术框架包含特征提取、多模态融合和推荐预测三个部分。

### **4.1 特征提取 (Feature Extraction)**

* **视觉特征 (Visual Features)**：
    * **编码器 (Encoder)**：使用预训练的**视觉变换器 (Vision Transformer, ViT)**，例如 `google/vit-base-patch16-224`。
    * **流程**：对每部电影，我们选取N张最具代表性的静态帧（例如N=5）和1张官方海报。每张图片经过ViT编码后，生成一个高维（如768维）的特征向量，该向量捕获了图像的全局语义信息。

* **文本特征 (Textual Features)**：
    * **编码器 (Encoder)**：使用预训练的**BERT (Bidirectional Encoder Representations from Transformers)** 模型处理短文本（如元数据、标签）。
    * **LLM增强 (LLM Enrichment)**：针对剧情、用户长评论等复杂文本，首先利用**大型语言模型 (LLM)** 进行摘要、情感分析和主题提取，然后将这些结构化的输出送入BERT进行编码，以捕捉更深层次的语义。

### **4.2 多模态融合 (Multimodal Fusion)**

我们将采用一个**自注意力融合层 (Self-Attention Fusion Layer)** 来聚合来自不同模态的特征向量。与简单的拼接 (concatenation) 不同，注意力机制能够：

1.  **动态加权**：根据当前的预测目标，模型可以学习到在不同场景下，应该更“关注”视觉特征还是文本特征。
2.  **捕捉模态间交互**：有效学习不同模态特征之间的复杂关系。

最终，融合层会输出一个统一的、信息丰富的多模态表征向量 (multimodal representation vector)。

### **4.3 预测模型 (Prediction Model)**

* **任务**：主要任务是**评分预测 (rating prediction)**。同时，我们会引入一个辅助的**多任务学习 (multi-task learning)**，即**类型分类 (genre classification)**，这有助于模型学习到更具泛化能力的特征表示。
* **架构**：将融合后的多模态向量与用户特征向量（如果可用）进行拼接，输入到一个**多层感知机 (Multi-Layer Perceptron, MLP)** 回归器中，最终输出预测的评分值 (例如1-5分)。

## **5. 实验设计与评估 (Experiments & Evaluation)**

* **评估指标 (Metrics)**：
    * 评分预测：**均方根误差 (RMSE, Root Mean Square Error)** 和 **平均绝对误差 (MAE, Mean Absolute Error)**。
* **基线模型 (Baselines)**：
    * **单模态模型**：仅使用文本特征的模型、仅使用视觉特征的模型。
    * **传统模型**：基于矩阵分解的协同过滤 (Collaborative Filtering) 模型。
* **消融研究 (Ablation Study)**：
    * 我们将系统性地移除模型的关键组件（例如，移除视觉分支、移除评论情感特征、将注意力融合替换为简单拼接），以量化评估每个模态和技术选择对最终性能的贡献。这对于验证我们方案的有效性至关重要。

## **6. 项目时间线 (Tentative Timeline)**

| 日期 (Dates) | 任务 (Task) |
| :--- | :--- |
| **June 17–30** | 数据集收集 + 预告片/帧下载 + 元数据对齐 (Dataset collection + frame/trailer download + metadata alignment) |
| **July 1–14** | 文本/视觉编码器（BERT, ViT）实现；利用LLM进行剧情/标签丰富化 (Text/visual encoder; LLM for plot/tagline enrichment) |
| **July 15–26** | 融合模型开发与训练（包含多任务类型分类） (Fusion model, training with multitask genre classification) |
| **July 27–Aug 4** | 模型验证与消融实验（移除视觉/文本模态，测试冷启动）(Validation + Ablation) |
| **Aug 5–15** | 最终报告撰写、可视化、幻灯片制作和项目提交 (Final write-up, visualization, slide and report submission) |

## **7. 预期成果与贡献 (Expected Outcomes & Contributions)**

* **一个功能完备的多模态推荐系统原型**。
* **一份详细的实验报告**，通过与基线模型的对比和消融研究，清晰地证明本项目所提出的多模态融合方法的优越性。
* **公开的代码库和演示文稿**，分享我们的研究成果和实现细节。
* 为推荐系统领域贡献一个**新的思路**：证明了通过深度分析视觉内容和用户长评，并结合注意力机制，可以显著提升推荐的准确性和用户体验。
