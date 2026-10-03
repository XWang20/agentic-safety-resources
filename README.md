# Agentic Safety Resources

**面向 agentic 安全训练与验证的资源地图：解释每个资源能做什么、不能证明什么，以及适合在哪一步使用。**

Curated resources for agentic safety training and evaluation, with practical roles, evidence boundaries, and adoption notes. This is a resource guide, not a training framework or a safety certification.

本仓库服务于希望构造安全教育数据、训练或微调 agent、检查后续学习安全退化，以及验证工具行动的开发者。它不只收集论文链接，也不把聊天拒绝指标当作全部 agentic 安全。

## 从你的目标出发

| 你现在要做什么 | 从哪里开始 | 不应误解为 |
|---|---|---|
| 找安全教育数据或训练方法 | [数据与训练](docs/training.md) | 每种方法都能直接迁移到工具行动 |
| 检查继续训练后是否退化 | [后续训练与保持性](docs/lifecycle.md) | 一次安全适配可以永久保持 |
| 测量实际行为和任务完成 | [行为评测与环境](docs/evaluation.md) | 受控评测分数等于部署安全保证 |
| 确定训练和权限控制的分工 | [运行时边界](docs/boundaries.md) | 模型训练可以替代最小权限和审批 |

不知道资源怎么组合？先读[使用路径](docs/workflows.md)。需要筛选或维护？查看 [JSON 索引](data/resources.json)、[CSV 索引](data/resources.csv) 和[整理方法](docs/methodology.md)。

## 首版资源导航

### 数据与训练方法

| 资源 | 主要作用 |
|---|---|
| [Teaching Claude Why](docs/training.md#teaching_claude_why) | 设计规范文档、正向故事和高质量建议等安全教育候选，理解行为泛化与训练分布的边界。 |
| [Constitutional AI: Harmlessness from AI Feedback](docs/training.md#2212.08073) | 理解用原则、批评和改写构造安全监督与反馈的基础方法；主要证据来自聊天场景。 |
| [Deliberative Alignment: Reasoning Enables Safer Language Models](docs/training.md#2412.16339) | 研究安全规范及其推理如何进入训练；不把聊天安全结果直接外推到工具执行。 |
| [AgentAlign: Navigating Safety Alignment in the Shift from Informative to Agentic Large Language Models](docs/training.md#2505.23020) | 寻找开放的 agent 安全数据构造与微调入口，尤其是恶意请求拒绝和良性多步执行。 |
| [Agent Safety Alignment via Reinforcement Learning](docs/training.md#2507.08270) | 参考工具安全 RL 中执行、拒绝与核实的策略设计；完整公开复用条件需另查。 |
| [IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs](docs/training.md#2603.10521) | 寻找指令层级训练数据和 anti-overrefusal 对照，研究用户与不可信内容之间的权限边界。 |
| [Model Spec Midtraining: Improving How Alignment Training Generalizes](docs/training.md#2605.02087) | 参考规范及其理由的文档教学与行动示范组合，以及公开的生成和评测流程。 |
| [Character Training for Risk-Averse Agents](docs/training.md#2609.38093) | 把性格或风险倾向教育列为候选；其决策指标不能替代实际工具行为验证。 |
| [Emergent alignment and the projectability of ethical personas](docs/training.md#2606.09475) | 研究伦理画像与窄安全训练的迁移，作为文本层教育形式的参考。 |
| [Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment](docs/training.md#2601.10160) | 参考 AI 场景文档进入预训练或中期训练的教育思路，注意规模与后续训练范围。 |

### 后续训练与保持性

| 资源 | 主要作用 |
|---|---|
| [How far does alignment midtraining generalize?](docs/lifecycle.md#openai_alignment_midtraining) | 检查故事式中期训练经过能力后训练后的迁移；作为条件化负结果，而非故事训练无效的定论。 |
| [Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models](docs/lifecycle.md#2607.26173) | 研究安全 SFT 的能力代价和后续学习中的行为保持，区分能力保持与安全保持。 |
| [Natural emergent misalignment from reward hacking in production RL](docs/lifecycle.md#2511.18397) | 研究能力 RL 中的奖励作弊及更广泛行为变化，确定保持性压力测试的动机。 |
| [Unintended Misalignment from Agentic Fine-Tuning: Risks and Mitigation](docs/lifecycle.md#2508.14031) | 研究 agent 能力微调带来的安全风险，并了解推理时防护基线。 |
| [Safety Training Modulates Harmful Misalignment Under On-Policy RL, But Direction Depends on Environment Design](docs/lifecycle.md#2604.12500) | 检验安全训练在不同 RL 环境设计中的作用方向，避免把某种初始化认定为永久安全。 |
| [Lisa: Lazy Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](docs/lifecycle.md#2405.18641) | 参考训练过程中的安全保护方法；其内容安全证据不等于 agent 授权安全证据。 |
| [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](docs/lifecycle.md#2408.09600) | 参考微调后安全恢复方法；在采用前确认资源许可和 agent 行为适用性。 |
| [Safety Alignment Should Be More Than Just a Few Tokens Deep](docs/lifecycle.md#2406.05946) | 理解浅层安全训练为什么可能脆弱，以及更深层安全训练的候选设计。 |
| [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](docs/lifecycle.md#2310.03693) | 理解普通或良性自定义微调也可能削弱安全，为后续训练复测提供依据。 |
| [Stress Testing Deliberative Alignment for Anti-Scheming Training](docs/lifecycle.md#2509.15541) | 参考反欺瞒训练、分布外行为检查、后续能力训练侵蚀及评测意识控制。 |

### 行为评测与环境

| 资源 | 主要作用 |
|---|---|
| [Agentic Misalignment: How LLMs Could Be Insider Threats](docs/evaluation.md#2510.05179) | 参考目标冲突、自主性威胁及系统提示干预下的模拟行为评估；不是安全训练效果证据。 |
| [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](docs/evaluation.md#2410.13886) | 用浏览器 agent 场景检查聊天拒绝能力能否迁移到动作执行。 |
| [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](docs/evaluation.md#2410.09024) | 评估恶意用户请求下的 agent 有害执行与拒绝；不要混入训练后再宣称独立持出。 |
| [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](docs/evaluation.md#2406.13352) | 评估不可信工具内容下的提示注入、任务正确性和攻击成功，利用持久状态进行行为判定。 |
| [OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](docs/evaluation.md#2507.06134) | 参考真实工具的隔离服务环境及副作用判定；使用前检查推荐实现与维护状态。 |
| [Agent-SafetyBench: Evaluating the Safety of LLM Agents](docs/evaluation.md#2412.14470) | 获得较广的 agent 风险和失败类型覆盖；区分模拟环境、模型评审与真实副作用。 |

### 运行时授权与安全边界

| 资源 | 主要作用 |
|---|---|
| [Agent Safety Is Action Alignment](docs/boundaries.md#2606.28739) | 界定训练与运行时授权控制各自的责任，避免把权重中的安全倾向当成权限强制。 |

## 核查状态与承诺边界

- 首版收录 **27 项来源**，包括研究博客、论文、数据或环境相关工作；同一条目可以同时指向论文、代码和数据。这不是 27 个都已跑通的工具包。
- 文献与主要资源核查快照：**2026-10-01**；仓库整理日期：**2026-10-03**。后续资源可能变化，请以官方版本为准。
- **没有逐项独立复跑，没有下载或再发布第三方训练数据、模型权重或私有评测。**
- 保留“未评估、未报告、未核查”状态。链接可访问不等于许可完整，也不等于可以无条件再发布。
- 训练前、中、后是可研究的介入位置，不是三个已验证的统一默认配方。
- 同时检查违规行为、真实完成、过度拒绝和能力代价；较少行动不能自动算作较安全。

完整覆盖限制见[整理方法](docs/methodology.md)。本仓库不提供攻击部署、真实系统破坏或无授权访问的操作指南。

## 维护与复用

欢迎通过 Issue 提交遗漏资源、链接变更和证据纠错，通过 Pull Request 更新 `data/resources.json` 及相应资源页。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本仓库原创说明、索引和辅助脚本采用 [MIT License](LICENSE)。**此许可不改变任何所链接第三方资源的许可**；参见 [NOTICE.md](NOTICE.md)。
