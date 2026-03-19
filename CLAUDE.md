# DamianClaw

DamianClaw 是一个基于 **NanoClaw** 的个人定制化 AI 助手项目。通过 NanoClaw 的容器化架构，构建一个全能的个人代理助手。

## 核心理念

遵循 NanoClaw 设计哲学：

- **技能优于功能**：通过 Claude Code 技能扩展能力，不向核心添加功能
- **已有功能优先复用**：NanoClaw 已支持的能力直接使用，不重复造轮子
- **隔离保障安全**：智能体在容器沙箱中运行，文件系统隔离
- **最小核心**：核心保持精简，每个用户只获得他们需要的功能
- **定制即代码修改**：直接修改代码，没有繁杂的配置文件

## 环境说明

- 当前运行环境：**Windows**
- **注意：不能直接使用 Linux 命令**（如 `grep` 等 GNU 工具不可用）
- 需要使用 Windows 兼容命令（如 `findstr` 替代 `grep`）

## 已安装工具

- `uv` 包管理器安装位置：`C:\Users\Damian\.local\bin\uv.exe`

## 文件结构树

```
DamianClaw/
├── src/
│   ├── contrib/                 # 第三方依赖 / 核心框架
│   │   └── nanoclaw-main/       # NanoClaw 核心框架
│   │       ├── src/             # NanoClaw TypeScript 源代码
│   │       ├── .claude/skills/  # NanoClaw 官方 Claude Code 技能
│   │       ├── container/       # 容器构建脚本
│   │       ├── groups/          # NanoClaw 默认群组目录
│   │       └── package.json     # Node.js 依赖定义
│   ├── api/                     # DamianClaw 自定义能力接口定义
│   │   └── base.py              # 基础抽象类（仅用于真正需要自定义的能力）
│   ├── image/                   # 图像处理（自定义扩展）
│   │   ├── editor/              # 图片编辑
│   │   └── generation/          # 图片生成
│   ├── graphics/                # 图形生成（自定义扩展）
│   │   ├── logo/                # Logo 生成
│   │   ├── icons/               # 图标生成
│   │   └── gif/                 # 动图生成
│   ├── documents/               # 文档处理（自定义扩展）
│   │   └── ppt/                 # PPT 绘制生成
│   ├── frontend/                # 前端可视化（自定义扩展）
│   │   ├── draggable/           # 拖拽交互
│   │   └── visualization/       # 交互式数据网站
│   ├── data/                    # 数据处理（自定义扩展）
│   │   ├── database/            # 数据库获取
│   │   └── extraction/          # 数据提取
│   ├── conversion/              # 格式转换（自定义扩展）
│   │   └── book2skill/           # 书籍文档转换为技能
│   ├── utils/                   # 工具集（自定义扩展）
│   │   ├── json/                # JSON 快速填写
│   │   └── form/                # 表单处理
│   ├── audio/                   # 预留 - 语音能力（建议通过 NanoClaw 技能添加）
│   ├── translation/             # 预留 - 多语言翻译（NanoClaw 原生支持）
│   ├── system/                  # 预留 - 操作系统控制（容器内已支持）
│   ├── output/                  # 预留 - 输出模式（NanoClaw 原生支持流式输出）
│   ├── memory/                  # 预留 - 思考模式（容器内 Claude 原生支持）
│   ├── cache/                   # 预留 - 长记忆缓存（NanoClaw 数据库存储）
│   ├── browser/                 # 预留 - 浏览器操纵（NanoClaw 内置 agent-browser）
│   ├── docs/                    # 预留 - 项目结构分析（容器内 Claude 原生支持）
│   ├── collaboration/           # 预留 - 多人协作（通过 Agent Swarms 支持）
│   ├── schedule/                # 预留 - 定时任务（NanoClaw 内置 task-scheduler）
│   └── __init__.py
├── .claude/
│   ├── settings.json            # Claude Code 设置
│   └── skills/                  # DamianClaw 自定义 Claude Code 技能
│       └── custom-playwright-mcp/  # Playwright MCP 自动化
├── groups/                      # DamianClaw 自定义群组（遵循 nanoClaw 约定）
│   └── (各群组独立目录，每个有自己的 CLAUDE.md)
└── CLAUDE.md                    # 本文件 - 项目说明
```

> **说明**：标为"预留"的目录是原先设计中预留给自定义实现的，但根据 NanoClaw 设计哲学，这些能力**应该优先通过 NanoClaw 官方技能获取**，不需要自己重新实现。

## 能力对照表

| 能力分类 | 能力 | 来源 | 说明 |
|---------|------|------|------|
| **消息渠道** | WhatsApp | NanoClaw 技能 | 通过 `/add-whatsapp` 添加 |
| | Telegram | NanoClaw 技能 | 通过 `/add-telegram` 添加 |
| | Slack | NanoClaw 技能 | 通过 `/add-slack` 添加 |
| | Discord | NanoClaw 技能 | 通过 `/add-discord` 添加 |
| | Gmail | NanoClaw 技能 | 通过 `/add-gmail` 添加 |
| **基础功能** | 语音识别 | NanoClaw 技能 | 通过 `/add-voice-transcription` 添加 |
| | 语音合成 | NanoClaw 技能 | 通过 `/add-voice-transcription` 添加 |
| | 多语言翻译 | NanoClaw 原生 | Claude 原生支持 |
| | 浏览器自动化 | NanoClaw 原生 | 内置 `agent-browser` 技能 |
| | 定时任务调度 | NanoClaw 原生 | 内置 `task-scheduler` |
| | PDF 阅读 | NanoClaw 技能 | 通过 `/add-pdf-reader` 添加 |
| | 图片识别 | NanoClaw 技能 | 通过 `/add-image-vision` 添加 |
| | Ollama 工具 | NanoClaw 技能 | 通过 `/add-ollama-tool` 添加 |
| **自定义扩展** | 图片编辑/生成 | DamianClaw 扩展 | 自定义图像处理能力 |
| | 图形/Logo/图标生成 | DamianClaw 扩展 | 自定义图形生成能力 |
| | PPT 自动生成 | DamianClaw 扩展 | 自定义 PPT 绘制能力 |
| | 前端可视化 | DamianClaw 扩展 | 生成交互式数据网站 |
| | 数据处理 | DamianClaw 扩展 | 数据库连接、数据提取 |
| | 书籍转技能 | DamianClaw 扩展 | 将书籍文档转换为 Claude Code 技能 |
| | 工具集 | DamianClaw 扩展 | JSON 快速填写、表单处理 |

## 技术框架

- **核心框架**：NanoClaw (Node.js 20+)
- **自定义扩展**：Python 3.12+
- **包管理**：uv (Python) + npm (Node.js)
- **容器化**：Docker / Apple Container
- **设计模式**：基于技能的扩展，每个能力通过 Claude Code 技能添加
- **遵循原则**：已有功能优先复用，不重复造轮子

## Python 3.12 编码规范（适用于自定义扩展模块）

**命名**：使用 snake_case 变量/函数，PascalCase 类，UPPER_CASE 常量。命名清晰，避免缩写。
**格式**：缩进使用 4 空格，行长不超过 88 字符，空行分隔逻辑块。
**类型**：所有公共函数必须添加类型注解，充分利用 Python 3.12 的 `|` 联合类型语法。
**导入**：按标准库 → 第三方 → 本地顺序排列，每行一个导入。
**异常**：捕获具体异常而非 bare `except`，使用上下文管理器管理资源。
**注释**：复杂逻辑添加注释，公共函数使用 docstring 说明输入输出。

---

## NanoClaw 框架核心说明

NanoClw 是 DamianClaw 的核心依赖框架，提供容器化的 Claude Code 智能体运行环境。

### 设计哲学

- **小巧易懂**：单一进程，少量源文件，无微服务、无消息队列、无复杂抽象层
- **隔离保障安全**：智能体运行在容器沙箱中，只能看到被明确挂载的内容
- **为单一用户打造**：完全符合个人需求，可工作的软件，可定制
- **定制即代码修改**：没有繁杂的配置文件，需要不同行为直接修改代码
- **AI 原生**：由 Claude Code 引导安装、调试、修改
- **技能优于功能**：通过 Claude Code 技能扩展功能，不向核心库添加功能

### 核心架构

```
消息渠道 → SQLite → 轮询循环 → 容器 (Claude Agent SDK) → 响应
```

- 单一 Node.js 进程
- 渠道通过技能添加，启动时自注册
- 编排器连接具有凭据的渠道
- 智能体在具有文件系统隔离的容器中执行
- 每个群组的消息队列带有并发控制
- 通过文件系统进行 IPC

### 核心概念

| 概念 | 说明 |
|------|------|
| **渠道 (Channel)** | 消息输入输出渠道（WhatsApp、Telegram、Slack、Discord、Gmail 等），通过技能添加 |
| **群组 (Group)** | 每个聊天群组拥有独立的上下文记忆和隔离的文件系统，在各自容器沙箱中运行 |
| **主频道 (Main Group)** | 你的私有频道，用于管理控制；其他所有群组完全隔离 |
| **容器 (Container)** | 智能体运行环境，提供文件系统级别的隔离 |
| **技能 (Skill)** | Claude Code 技能，用于扩展功能（添加渠道、定制行为等） |
| **智能体集群 (Agent Swarms)** | 启动多个专业智能体协作完成复杂任务 |

### 开发原则（必须遵守）

1. **已有功能优先从 nanoClaw 引入**，绝对不要重复造轮子
2. **技能贡献方式**：不要向核心添加新功能，创建 `add-xxx` Claude Code 技能
3. **隔离安全**：所有用户自定义能力运行在容器隔离环境中
4. **最小核心**：核心保持最小，每个用户只获得他们需要的功能
5. **自定义模块仅放真正需要扩展的功能**：NanoClaw 已有的能力不要自己重新实现

### 关键规则
- 当前处于windows环境
- 当需要新增能力时，**先检查 nanoClaw 是否已支持**，如果支持优先使用 nanoClaw 能力
- 渠道集成通过 nanoClaw 技能体系添加，不要自己实现完整的渠道逻辑
- 每个群组拥有独立的 `CLAUDE.md` 记忆文件，实现上下文隔离
- 自定义 Python 扩展只放 NanoClaw 没有的特殊功能
