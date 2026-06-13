<div align="center">
<h1 align="center">what-is-ai-agent-skill 🤖</h1>

<p align="center">
  <a href="https://github.com/quick123-666/what-is-ai-agent-skill/stargazers"><img src="https://img.shields.io/github/stars/quick123-666/what-is-ai-agent-skill.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/quick123-666/what-is-ai-agent-skill/issues"><img src="https://img.shields.io/github/issues/quick123-666/what-is-ai-agent-skill.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/quick123-666/what-is-ai-agent-skill/network/members"><img src="https://img.shields.io/github/forks/quick123-666/what-is-ai-agent-skill.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/quick123-666/what-is-ai-agent-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/quick123-666/what-is-ai-agent-skill.svg?style=for-the-badge" alt="License"></a>
</p>

[English](#english) | [中文](#中文)

---

一个 OpenClaw/Claude Skill，提供全面的 AI Agent 知识，从核心概念到行业趋势。设计为"资深工程师朋友"，用数据驱动的洞察力回答你的 AI Agent 问题。

</div>

## 功能特性 🎯

- [x] **核心概念**：Agent 定义、记忆架构、规划算法、工具调用
- [x] **协议详解**：MCP（模型上下文协议）、A2A（Agent 间协议）深度解析
- [x] **框架横评**：AutoGen、LangGraph、Semantic Kernel、CrewAI、Swarm
- [x] **行业趋势**：月度/周度 AI Agent 行业动态
- [x] **企业案例**：真实落地场景与实践
- [x] **语义检索**：纯本地检索，无需外部 API，响应 < 100ms
- [x] **全网动态**：多信息源并行搜索，结构化汇总报告
- [x] **播客模式**：将报告转换为语音播客（TTS）
- [x] **双语支持**：中文/English 完整支持

## 快速开始 🚀

### 安装

将 skill 添加到 OpenClaw 即可自动触发，无需额外配置。

### 使用方式

| 触发词 | 说明 |
|--------|------|
| "AI Agent 是什么" / "What is AI Agent" | 核心概念解释 |
| "MCP 协议" / "MCP protocol" | 协议深度解析 |
| "趋势周报" / "Weekly trends" | 生成趋势报告 |
| "全网动态" / "Full web search" | 全网多源搜索 |
| "深度调研 XXX" | 启动深度调研流程 |
| "通俗版" / "Technical version" | 切换解释风格 |
| "做成音频" / "生成播客" | 生成音频播客 |

## 交互模式

### 三种解释风格

| 模式 | 说明 |
|------|------|
| **通俗版** | 用生活类比讲解，不懂技术也能听懂 |
| **技术版** | 直接讲原理、框架、协议等硬核内容 |
| **两种都给我** | 并排输出通俗版 + 技术版 |

### 语义检索（本地运行）

```bash
cd search
python semantic_search.py "MCP 协议是什么"
```

- 算法：关键词匹配 + 位置权重 + 精确匹配加分
- 数据源：references/ 下 7 个 .md 文件，共 ~240 个段落
- 依赖：纯 Python，无需 ML 库
- 响应时间：< 100ms

## 文件结构

```
what-is-ai-agent-skill/
├── README.md                      # 本文件
├── SKILL.md                       # Skill 入口
├── search/
│   └── semantic_search.py        # 本地语义检索
└── references/
    ├── 01-core-concepts.md        # 核心概念
    ├── 02-protocols.md            # MCP/A2A 协议
    ├── 03-frameworks.md           # 框架横评
    ├── 04-trends-2026-06.md       # 2026年6月趋势
    ├── 05-llm-comparison.md       # LLM 对比
    ├── 06-enterprise-cases.md     # 企业案例
    └── 07-quick-start.md          # 快速入门
```

## 技术细节

| 项目 | 说明 |
|------|------|
| **检索方式** | 本地关键词检索（类 BM25 算法） |
| **依赖** | 纯 Python，无需 ML 库 |
| **响应时间** | < 100ms |
| **索引规模** | 7 个参考文件，约 240 个段落 |
| **运行模式** | 离线运行，无外部 API 依赖 |

## 许可证 📝

MIT License - 点击查看 [`LICENSE`](LICENSE) 文件

---

## English

### Overview

An OpenClaw/Claude Skill that provides comprehensive AI Agent knowledge, from core concepts to industry trends. Designed as a "senior engineer friend" who answers your AI Agent questions with data-driven insights.

### Features

- **Core Concepts**: Agent definition, memory architecture, planning algorithms, tool calling
- **Protocols**: MCP (Model Context Protocol), A2A (Agent-to-Agent) deep dive
- **Frameworks**: AutoGen, LangGraph, Semantic Kernel, CrewAI, Swarm comparison
- **Trends**: Monthly/weekly AI Agent industry updates
- **Enterprise Cases**: Real-world deployment examples
- **Semantic Search**: Local-only retrieval, no external API required, < 100ms response
- **Full Web Search**: Multi-source parallel search with structured summary
- **Podcast Mode**: Convert reports to audio with TTS
- **Bilingual**: Complete Chinese/English support

### Quick Start

Add this skill to OpenClaw and it will auto-trigger on AI Agent questions.

### Trigger Commands

| Command | Description |
|---------|-------------|
| "AI Agent 是什么" / "What is AI Agent" | Core concept explanation |
| "MCP 协议" / "MCP protocol" | Protocol deep dive |
| "趋势周报" / "Weekly trends" | Generate trend report |
| "全网动态" / "Full web search" | Omni-scout multi-source search |
| "通俗版" / "Technical version" | Switch explanation style |

### Semantic Search (Local)

```bash
cd search
python semantic_search.py "What is MCP protocol"
```

- Algorithm: Keyword matching + position weighting + exact match bonus
- Data source: 7 .md files in references/, ~240 paragraphs
- Dependencies: Pure Python, no ML libraries
- Response time: < 100ms

### Technical Details

| Item | Description |
|------|-------------|
| **Retrieval** | Local keyword-based search (BM25-like) |
| **Dependencies** | Pure Python, no ML libraries |
| **Response Time** | < 100ms |
| **Index Size** | 7 reference files, ~240 paragraphs |
| **Mode** | Offline, no external API required |

### License

MIT License - See [`LICENSE`](LICENSE) file

---

*Last updated: 2026-06-13*
