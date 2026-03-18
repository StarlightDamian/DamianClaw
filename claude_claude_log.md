## 模式

claude --dangerously-skip-permissions    # YOLO模式
claude --permission-mode plan                # 规划模式

## 创建

~/.claude/CLAUDE.md

## 常用组合

/code-review /重构

## SKILL

* export-conversation-history ：导出对话历史，
* code-refactor 重构
*  naming-refactor 重命名
*  exit  退出 使用/git和/export-conversation-history 这两个SKILL
* cross-border-finance  数据库表结构设计、业务流程架构、命名规范、合规性咨询、财务报表设计   
* frontend-design-cn 前端设计

## subagent

* 

## Tip

Tip: Run claude --continue or claude --resume to resume a conversation 

## 日志

```
 /find-skills 使用playwright来高效操作浏览器 通过CLI挂载playwright MCP                                                                                                                 
将具体场景登录、抓取、点击作为prompt输入，利用代码生成能力和MCP的上下文理解自动编写DOM强依赖具体的DOM节点的python playwright脚本，在底层飞速操作浏览器

 推荐安装：
  # 1. MCP 构建工具（用于挂载 Playwright MCP）
  npx skills add anthropics/skills@mcp-builder -g -y

  # 2. Playwright 最佳实践
  npx skills add currents-dev/playwright-best-practices-skill@playwright-best-practices -g -y

  # 3. Playwright 代码生成
  npx skills add github/awesome-copilot@playwright-generate-test -g -y


```

/code-review 如果设计到python代码相关，帮我保存到D:\03_software_engineering\05_github\DamianClaw\src 首先你要进行代码的规划 [Pasted text #1 +9 lines] [Pasted text #2 +10 lines]     
  这些都是我后续要完成的事情，你先要把能力和对象解耦，高内聚低耦合，其次代码要精简。规划后新建对应的文件夹，后续python代码直接放入其中，并且进行更新。文件结构树和技术框架写入D:\03_so  
  ftware_engineering\05_github\DamianClaw\CLAUDE.md
