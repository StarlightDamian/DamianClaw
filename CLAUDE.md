# DamianClaw

项目说明：这是一个个人 Agent 助手项目，目标是通过 nanoClaw 完成一个全能代理。

## 环境说明

- 当前运行环境：**Windows**
- **注意：不能直接使用 Linux 命令**（如 `grep` 等 GNU 工具不可用）
- 需要使用 Windows 兼容命令（如 `findstr` 替代 `grep`）

## 已安装工具

- `uv` 包管理器安装位置：`C:\Users\Damian\.local\bin\uv.exe`

## 架构设计

### 设计原则

- **能力与对象解耦**：每项能力独立成模块，高内聚低耦合
- **单一职责**：每个模块只负责一项功能
- **易于扩展**：新增功能只需增加新模块，不影响现有代码
- **代码精简**：保持代码简洁，避免过度设计

## 文件结构树

```
DamianClaw/
├── src/
│   ├── api/                    # API 接口层
│   ├── audio/                  # 语音能力
│   │   ├── speech/           # 语音识别
│   │   └── tts/              # 文本转语音
│   ├── translation/            # 多语言翻译
│   ├── system/                # 操作系统控制
│   ├── image/                 # 图像处理
│   │   ├── editor/           # 图片编辑
│   │   └── generation/       # 图片生成
│   ├── output/                # 输出模式
│   │   ├── streaming/        # 流式输出
│   │   └── structured/      # 结构化输出
│   ├── memory/                # 思考模式
│   ├── cache/                 # 长记忆缓存
│   ├── browser/               # 浏览器操纵 (Playwright MCP)
│   ├── data/                  # 数据处理
│   │   ├── database/        # 数据库获取
│   │   └── extraction/      # 数据提取
│   ├── docs/                  # 项目结构分析 / 接口文档读取
│   ├── collaboration/         # 多人协作支持
│   ├── frontend/              # 前端可视化
│   │   ├── draggable/       # 拖拽交互
│   │   └── visualization/   # 交互式数据网站
│   ├── conversion/            # 格式转换 (book2skill)
│   ├── documents/             # 文档处理
│   │   └── ppt/             # PPT 绘制生成
│   ├── graphics/              # 图形生成
│   │   ├── logo/            # Logo 生成
│   │   ├── icons/           # 图标生成
│   │   └── gif/             # 动图生成
│   ├── utils/                 # 工具集
│   │   ├── json/            # JSON 快速填写
│   │   └── form/            # 表单处理
│   ├── schedule/              # 定时任务 / 自动发送
│   └── contrib/               # 第三方依赖 (nanoClaw)
├── .claude/
│   └── skills/                # Claude Code 技能
│       └── custom-playwright-mcp/  # Playwright MCP 自动化
└── CLAUDE.md                  # 项目说明
```

## 模块能力对照表

| 模块 | 能力 | 说明 |
|------|------|------|
| `audio/` | 语音 | 语音识别、语音合成 |
| `translation/` | 多语言翻译 | 多语言互译 |
| `system/` | 操作系统控制 | 文件操作、进程管理、系统命令 |
| `image/` | 图片编辑/生成 | 图片编辑处理、图像生成 |
| `output/streaming/` | 流式输出 | 支持流式响应输出 |
| `output/structured/` | 结构化输出 | JSON/Markdown 结构化输出 |
| `memory/` | 思考模式 | 多步骤推理、思考链管理 |
| `cache/` | 长记忆缓存 | 长期会话记忆缓存 |
| `browser/` | 浏览器操纵 | Playwright MCP 自动化操作 |
| `data/database/` | 数据库获取 | 数据库连接、数据查询 |
| `docs/` | 项目结构分析 | 读取接口文档、分析项目结构 |
| `collaboration/` | 多人协作 | 多 Agent 协作支持 |
| `frontend/` | 拖拽可视化 | 生成交互式数据可视化网站 |
| `conversion/` | book2skill | 书籍文档转换为技能 |
| `documents/ppt/` | PPT 绘制 | 自动生成 PPT 文档 |
| `graphics/` | 图标/logo/动图 | 生成图标、Logo、GIF 动图 |
| `utils/json/` | JSON 快速填写 | 快速填充 JSON 模板 |
| `schedule/` | 定时自动发送 | 定时任务、自动消息发送 |

## 技术框架

- **语言**：Python 3.12+
- **包管理**：uv
- **浏览器自动化**：Playwright + MCP (Model Context Protocol)
- **设计模式**：模块化设计，每个能力独立模块，依赖注入
- **遵循原则**：高内聚低耦合，代码精简，易于扩展

## Python 3.12 编码规范

**命名**：使用 snake_case 变量/函数，PascalCase 类，UPPER_CASE 常量。命名清晰，避免缩写。

**格式**：缩进使用 4 空格，行长不超过 88 字符，空行分隔逻辑块。

**类型**：所有公共函数必须添加类型注解，充分利用 Python 3.12 的 `|` 联合类型语法。

**导入**：按标准库 → 第三方 → 本地顺序排列，每行一个导入。

**异常**：捕获具体异常而非 bare `except`，使用上下文管理器管理资源。

**注释**：复杂逻辑添加注释，公共函数使用 docstring 说明输入输出。
