# AI Agent 核心概念

## 一、AI Agent 的技术定义

AI Agent（Artificial Intelligence Agent）是一种基于大语言模型（LLM）的自主智能系统，其核心能力包括：

1. **感知（Perception）**：接收并解析多模态输入——文本、图像、语音、文件、结构化数据
2. **规划（Planning）**：将复杂任务分解为可执行的子任务序列，通常借助思维链（Chain of Thought）推理
3. **行动（Action）**：通过工具调用（Tool Use / Function Calling）操作外部系统，完成真实世界任务
4. **记忆（Memory）**：在三个时间尺度上保持状态——短期（上下文窗口）、中期（向量检索）、长期（持久存储）

这四者的协同构成 Agent 与传统 LLM 的本质差异。

---

## 二、LLM 与 AI Agent 的架构对比

| 维度 | 纯 LLM | AI Agent |
|------|--------|----------|
| **输入边界** | 单一对话窗口，最长受限于 context window | 跨窗口、跨 session，整合多源数据 |
| **决策机制** | 概率最高的下一个 token | LLM 推理 + 显式规划 + 条件判断 |
| **工具调用** | 需要人工编排 prompt 或外部编排器 | 自主决策是否调用工具、调用哪个工具 |
| **执行链路** | 输入→LLM→输出（文字）| 输入→LLM推理→Tool Call→外部执行→结果回传→LLM再推理→最终输出 |
| **状态管理** | 无状态（stateless）| 有状态（stateful），维护会话内外的世界模型 |
| **典型输出** | 文字回答或代码片段 | 可执行的代码/文件/系统操作/多轮对话结果 |

---

## 三、ReAct 范式：Agent 的决策循环

当前主流 Agent 采用 **ReAct**（Reasoning + Acting）循环：

```
User Input
    ↓
[1] LLM Reasoning（分析意图，决定下一步）
    ↓
[2] Action Planning（生成工具调用计划）
    ↓
[3] Tool Execution（执行搜索/代码/数据库等外部操作）
    ↓
[4] Observation（收集执行结果）
    ↓
[5] LLM Reasoning（结合结果再推理）
    ↓ → 重复 [1]-[5] 直至任务完成或达到上限
Final Output
```

典型工具调用格式（JSON）：

```json
{
  "name": "search_web",
  "arguments": {
    "query": "MCP protocol 2026 adoption",
    "max_results": 10
  }
}
```

---

## 四、RAG：检索增强生成的技术机制

RAG（Retrieval Augmented Generation）解决 LLM 两类核心缺陷：

1. **幻觉（Hallucination）**：LLM 在知识边界处生成看似合理但事实错误的内容
2. **知识陈旧（Knowledge Cutoff）**：LLM 无法获取训练截止日期之后的信息

### RAG 工作流程

```
User Query
    ↓
[1] Embedding Model（将 query 转换为向量）
    ↓
[2] Vector Search（在向量数据库中检索 top-k 相关文档）
    ↓
[3] Context Assembly（将检索结果拼入 prompt 作为上下文）
    ↓
[4] LLM Generation（基于检索上下文生成答案，引用源）
    ↓
Final Answer（含引用溯源的文字输出）
```

### 企业 RAG 架构关键组件

| 组件 | 作用 | 主流方案 |
|------|------|---------|
| **Embedding 模型** | 将文本映射为向量 | OpenAI text-embedding-3 / BGE / Jina |
| **向量数据库** | 高效相似性检索 | Milvus / Qdrant / Pinecone / ChromaDB |
| **重排序（ReRanker）** | 精细化排序检索结果 | BGE-Reranker / Cohere Rerank |
| **混合检索** | 关键词 + 语义双路检索 | BM25 + 向量检索融合 |
| **元数据过滤** | 按时间/来源/类型过滤 | 支持 field filter 的向量数据库 |

---

## 五、Function Calling / Tool Use 的技术原理

Function Calling 是 LLM 连接到外部世界的桥梁，本质是将自然语言意图转换为结构化 API 调用。

### 支持 Function Calling 的主流模型

| 模型 | Function Calling 能力 | 精度 |
|------|---------------------|------|
| GPT-4o / GPT-4o-mini | 原生支持，多工具并行 | 高 |
| Claude 3.5 Sonnet | 原生支持，工具选择精准 | 高 |
| Gemini 1.5 Pro | 原生支持，多模态函数调用 | 高 |
| DeepSeek V3 | 支持，工具选择能力接近 GPT-4 | 中高 |
| Kimi K2 | 支持，长上下文优化 | 中高 |

### 工具调用安全边界

| 安全层级 | 机制 | 说明 |
|---------|------|------|
| **权限控制** | OAuth / API Key 范围限制 | Agent 只能访问被授权的接口 |
| **操作确认** | Human-in-the-Loop | 高风险操作（删除/付费/外发）需人工确认 |
| **沙箱执行** | 独立进程/容器隔离 | Agent Zero 等框架每个操作在独立 shell 运行 |
| **审计日志** | 完整操作记录 | 所有工具调用入日志，可追溯 |
| **速率限制** | API 调用频次控制 | 防止异常调用导致系统过载 |

---

## 六、记忆系统的三层架构

### 短期记忆：Context Window
- 受限于模型 context length（当前最长 200 万 Token）
- 优点：无延迟，零额外成本
- 缺点：session 结束即丢失，无法跨会话

### 中期记忆：向量检索（RAG）
- 将交互历史向量化，存入向量数据库
- 检索时取 top-k 相关片段注入 context
- 优点：可跨 session 积累，语义检索
- 缺点：依赖检索质量，有延迟

### 长期记忆：结构化持久存储
- 知识图谱：实体-关系-属性三层结构（ MemPalace 的 wing/room/drawer 属于此类）
- 传统数据库：SQL/NoSQL 存储关键状态
- 优点：精确查询、结构化推理、可持久化
- 代表方案：MemPalace（本地优先，96.6% R@5）、Mem0、Recursive Mem

---

## 七、多 Agent 协作模式

### 单一 Agent 的局限
- 单个 Agent 的 context 和工具集有限
- 复杂任务拆解后，单一 Agent 难以高效分工
- 单一 Agent 缺乏交叉验证机制

### 协作架构分类

| 模式 | 说明 | 代表框架 |
|------|------|---------|
| **层次式（Hierarchical）** | 一个 Orchestrator Agent 负责任务分解和调度，子 Agent 执行具体任务 | LangGraph / Magentic-One |
| **对等式（Peer-to-Peer）** | Agent 之间通过 A2A 协议直接通信，地位平等 | AutoGen / CrewAI |
| **流水线式（Pipeline）** | Agent 串联，前一个 Agent 的输出是后一个 Agent 的输入 | 自定义工作流 |
| **联邦式（Federated）** | 不同组织/系统的 Agent 通过标准化协议互联 | A2A 协议商用场景 |