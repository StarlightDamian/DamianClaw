# DamianClaw Source Modules

本目录按**高内聚低耦合**原则组织代码，每个能力对应一个独立模块。

## 模块列表

| 模块 | 功能 |
|------|------|
| [audio/](./audio/) | 语音处理（语音识别、文字转语音）|
| [translation/](./translation/) | 多语言翻译 |
| [system/](./system/) | 操作系统控制 |
| [image/](./image/) | 图片编辑与生成 |
| [output/](./output/) | 流式输出 / 结构化输出 |
| [memory/](./memory/) | 思考模式管理 |
| [cache/](./cache/) | 长记忆缓存 |
| [browser/](./browser/) | 浏览器自动化操纵 |
| [data/](./data/) | 数据库获取与数据提取 |
| [docs/](./docs/) | 项目结构分析，读取接口文档 |
| [collaboration/](./collaboration/) | 多人协作支持 |
| [frontend/](./frontend/) | 前端拖拽可视化，交互式数据网站 |
| [conversion/](./conversion/) | 格式转换（book2skill）|
| [documents/](./documents/) | 文档处理（PPT绘制）|
| [graphics/](./graphics/) | 图标/logo/动图生成 |
| [utils/](./utils/) | 工具集合 (JSON快速填写) |
| [schedule/](./schedule/) | 定时自动发送 |
| [api/](./api/) | API 接口层 |

## 开发规范

1. **每个模块一个职责**，不要交叉污染
2. **依赖注入**，模块间通过接口通信
3. **类型注解**，所有公开函数添加类型注解
4. **精简代码**，保持简洁，避免过度设计
