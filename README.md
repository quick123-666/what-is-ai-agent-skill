# what-is-ai-agent-skill

[English](#english) | [中文](#中文)

---

## English

### Overview

**what-is-ai-agent-skill** is an OpenClaw/Claude skill that provides comprehensive AI Agent knowledge, from core concepts to industry trends. It's designed as a "senior engineer friend" who can answer your questions about AI Agents with data-driven insights.

### Features

- **Core Concepts**: Agent definition, memory architecture, planning algorithms, tool calling
- **Protocols**: MCP (Model Context Protocol), A2A (Agent-to-Agent) deep dive
- **Frameworks**: AutoGen, LangGraph, Semantic Kernel, CrewAI comparison
- **Trends**: Monthly/weekly AI Agent industry updates
- **Enterprise Cases**: Real-world deployment examples
- **Semantic Search**: Local-only retrieval, no external API required
- **Podcast Mode**: Convert reports to audio with TTS

### Quick Start

```bash
# Install skill (in OpenClaw)
# Just add this skill to your OpenClaw and it will auto-trigger on AI Agent questions
```

### Semantic Search

The skill includes a local semantic search system that doesn't require any external APIs:

```bash
cd search
python semantic_search.py "What is MCP protocol"
```

### File Structure

```
what-is-ai-agent-skill/
├── README.md                    # This file
├── SKILL.md                     # Skill entry point
├── search/
│   └── semantic_search.py      # Local semantic search (BM25-based)
└── references/
    ├── 01-core-concepts.md      # Core concepts
    ├── 02-protocols.md          # MCP/A2A protocols
    ├── 03-frameworks.md         # Framework comparison
    ├── 04-trends-2026-06.md     # June 2026 trends
    ├── 05-llm-comparison.md    # LLM comparison
    ├── 06-enterprise-cases.md  # Enterprise cases
    └── 07-quick-start.md       # Quick start guide
```

### Trigger Commands

| Command | Description |
|---------|-------------|
| "AI Agent 是什么" / "What is AI Agent" | Core concept explanation |
| "MCP 协议" / "MCP protocol" | Protocol deep dive |
| "趋势周报" / "Weekly trends" | Generate trend report |
| "全网动态" / "Full web search" | Omni-scout multi-source search |
| "通俗版" / "Technical version" | Switch explanation style |

### Technical Details

- **Retrieval**: Local keyword-based search (BM25-like algorithm)
- **Dependencies**: Pure Python, no ML libraries required
- **Response Time**: < 100ms
- **Index Size**: ~240 chunks from 12 reference files

### License

MIT License

---

## 中文

### 概述

**what-is-ai-agent-skill** 是一个 OpenClaw/Claude Agent 技能，提供全面的 AI Agent 知识，从核心概念到行业趋势。它被设计为一个"资深工程师朋友"，用数据驱动的洞察力回答你的 AI Agent 问题。

### 功能特性

- **核心概念**：Agent 定义、记忆架构、规划算法、工具调用
- **协议详解**：MCP（模型上下文协议）、A2A（Agent 间协议）深度解析
- **框架对比**：AutoGen、LangGraph、Semantic Kernel、CrewAI
- **行业趋势**：月度/周度 AI Agent 行业动态
- **企业案例**：真实落地场景与实践
- **语义检索**：纯本地检索，无需外部 API
- **播客模式**：将报告转换为语音播客

### 快速开始

```bash
# 在 OpenClaw 中安装 skill
# 添加此 skill 后，自动响应 AI Agent 相关问题
```

### 语义检索

Skill 内置本地语义检索系统，无需任何外部 API：

```bash
cd search
python semantic_search.py "MCP 协议是什么"
```

### 文件结构

```
what-is-ai-agent-skill/
├── README.md                    # 本文件
├── SKILL.md                     # 技能入口
├── search/
│   └── semantic_search.py      # 本地语义检索（类 BM25 算法）
└── references/
    ├── 01-core-concepts.md      # 核心概念
    ├── 02-protocols.md          # MCP/A2A 协议
    ├── 03-frameworks.md         # 框架对比
    ├── 04-trends-2026-06.md     # 2026年6月趋势
    ├── 05-llm-comparison.md     # LLM 对比
    ├── 06-enterprise-cases.md   # 企业案例
    └── 07-quick-start.md        # 快速入门
```

### 触发命令

| 命令 | 说明 |
|------|------|
| "AI Agent 是什么" / "What is AI Agent" | 核心概念解释 |
| "MCP 协议" / "MCP protocol" | 协议深度解析 |
| "趋势周报" / "Weekly trends" | 生成趋势报告 |
| "全网动态" / "Full web search" | 全网多源搜索 |
| "通俗版" / "Technical version" | 切换解释风格 |

### 技术细节

- **检索方式**：本地关键词检索（类 BM25 算法）
- **依赖**：纯 Python，无需 ML 库
- **响应时间**：< 100ms
- **索引规模**：12 个参考文件，约 240 个段落

### 许可证

MIT License

---

## 贡献指南 / Contributing

欢迎提交 Issue 和 Pull Request！

Issues: https://github.com/quick123-666/what-is-ai-agent-skill/issues

---

*Last updated: 2026-06-13*
