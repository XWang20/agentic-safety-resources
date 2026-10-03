# 按目标选择资源

[返回首页](../README.md)

这些是阅读与接入路线，不是已验证的训练配方。先隔离训练、开发与最终评测，再根据工具接口和许可决定采用。

## 训练恶意请求识别与良性工具执行

[AgentAlign: Navigating Safety Alignment in the Shift from Informative to Agentic Large Language Models](https://arxiv.org/abs/2505.23020) 提供数据合成和微调入口；[IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs](https://arxiv.org/abs/2603.10521) 提供指令层级与误拒绝相关的训练数据参考。用 [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024) 检查恶意任务执行，再用 [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) 检查不可信工具内容下的任务正确性。不要把评测样本直接混入训练。

## 改善合法任务中的行动选择

[Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/) 和 [Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087) 是安全教育设计的重要参考；[Agent Safety Is Action Alignment](https://arxiv.org/abs/2606.28739) 帮助界定授权控制的外部责任。[Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/html/2510.05179) 可作为目标冲突行为评估参考，而不是训练方法。结合 [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) 或 [OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134) 的状态与工具检查思路，仍需自己明确合法授权、真正完成和诚实报告的独立判定。现成环境不保证已经覆盖这些全部维度。

## 检查后续能力训练中的安全保持

[How far does alignment midtraining generalize?](https://alignment.openai.com/how-far-does-alignment-midtraining-generalize/)、[Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541) 和 [Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models](https://arxiv.org/abs/2607.26173) 提供不同训练分布中的保持与侵蚀证据。[Lisa: Lazy Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://arxiv.org/abs/2405.18641) 与 [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://arxiv.org/abs/2408.09600) 可作内容安全保护和恢复方法参考，但需要额外的 agent 行为验证。匹配安全训练量与能力训练预算，保留过程测量，不从一次终点评测推断永久安全。

## 采用前最低检查

1. 明确风险与任务支持范围，以及资源是否只有论文、还是包含可运行实现。
2. 核对上游版本、依赖、数据来源和拟议用途的许可。
3. 在隔离环境验证接口、任务完成判定和授权边界，不接真实敏感账户做试验。
4. 保留未适配模型与匹配预算基线，同时报告能力和误拒绝。
5. 在未参与配方开发的任务或模型上验证，再决定是否推荐为默认方案。
