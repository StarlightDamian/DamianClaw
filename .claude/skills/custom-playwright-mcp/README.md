# Custom Playwright MCP 技能

## 功能

- 🎭 **Playwright 浏览器自动化** - 全速操作 Chrome/Chromium
- 🤖 **自动代码生成** - 根据你的自然语言描述（登录、抓取、点击）生成完整 Python 脚本
- 🎯 **精确 DOM 定位** - 生成强依赖具体 DOM 节点的选择器代码
- 🔌 **MCP 挂载** - 通过 CLI 以 Model Context Protocol 服务方式运行
- ⚡ **底层高速操作** - 直接调用 Playwright API，速度飞快

## 安装依赖

```bash
# 使用 uv（项目已配置 uv）
uv pip install -r .claude/skills/custom-playwright-mcp/requirements.txt

# 安装 Playwright 浏览器
playwright install chromium
```

## 使用方式

### 1. 作为 MCP 服务启动（Claude Code 挂载）

在你的 `mcp.json` 中添加：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "python",
      "args": [".claude/skills/custom-playwright-mcp/start_mcp.py"]
    }
  }
}
```

### 2. 使用流程

1. **你提供**：目标 URL + 场景描述（例如："打开知乎，点击登录，用手机号 138xxxx 密码 xxx 登录"）
2. **我生成**：完整的 Python 脚本，包含精确的 DOM 选择器定位
3. **MCP 执行**：脚本在底层自动执行，返回结果和截图

## 生成代码的原则

1. **强依赖具体 DOM 节点** - 使用页面实际存在的 id、class、属性定位，不依赖模糊匹配
2. **完全可运行** - 生成代码复制就能执行，不需要额外修改
3. **包含等待机制** - 正确处理页面加载和元素出现等待
4. **结果可验证** - 生成截图保存，方便验证结果

## 示例

查看 `example.py` 看 GitHub 登录示例。

## 工作流程

```
你的场景描述 (登录 XX 网站)
    ↓
分析页面 DOM 结构
    ↓
生成精确选择器
    ↓
输出完整 Python 脚本
    ↓
MCP 执行脚本
    ↓
返回结果截图
```
