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

深刻的理解nanoClaw这是你以后大部分能力最主要的来源包。D:\03_software_engineering\05_github\DamianClaw\src\contrib\nanoclaw-main 把框架和文件等都写入CLAUDE.md                         
  如果是已有的功能优先从nanoclaw引入，而不是自己新建对应代码和文件

你可以访问https://clash.razord.top配置相应的SKILL策略后，连接谷歌官网吗

D:\03_software\clash\Clash.for.Windows-0.20.16-ikuuu\data\profiles\1708358592002.yml 通过这个配置信息，我希望你能够访问谷歌官网，并且固定为SKILL

 访问谷歌并且查询“tun”是什么，把查询结果返回给我

安装 pi install git:github.com/pasky/chrome-cdp-skill@v1.0.1

/skill-creator 创建以下两个SKILL，他们是有联动关系的

创建一个通用的浏览器访问SKILL，当访问浏览器的时候，使用浏览器SKILL                                       

1. 访问浏览器的时候，不打开新的浏览器，而是尝试调用已打开的浏览器信息，避免验证，参考chrome-cdp-skill

2. 当访问浏览器的时候，尽可能快的把结果返回给我，质量好，速度快，参考“将具体场景登录、抓取、点击作为prompt输入，利用代码生成能力和MCP的上下文理解自动编写DOM强依赖具体的DOM节点的python playwright脚本，在底层飞速操作浏览器”

创建一个通用的外网访问SKILL，当访问外网的时候调用 外网SKILL和浏览器SKILL

1. 把刚才创建的clash-proxy-google-workspace 、clash-proxy-google 两个SKILL合并。当访问外网浏览器的时候，优先调用python脚本切换对应的ip。这个应该是固定的一个proxy server  

  这两个技能已经完全按照你的需求创建：
  - ✅ browser-automation：优先连接已打开浏览器避免验证，降级生成 Playwright 脚本
  - ✅ external-network：合并了原 clash-proxy-google，固定代理 127.0.0.1:7890，调用 browser-automation 实际执行
  - ✅ 两者完全解耦，browser-automation 可以独立用于不需要代理的场景
  - ✅ 复用了现有 chrome-cdp 代码，不重复造轮子
    /external-network 修改这个SKILL，当涉及到“翻墙”、“外网”，或者明显外网的网站（redhat\twitter\youtube\instagram等）的时候优先尝试这种方式

你能够访问“https://zhuanlan.zhihu.com/p/2000867285422866885”吗 

❯ 安装 npx skills add https://github.com/inferen-sh/skills --skill nano-banana-2 安装到全局 

安装这个SKILL到全局SKILL https://github.com/obra/superpowers   

/nano-banana-2 D:\02_work\03_平安\20_部门_信息安全平台部_数据模型组\Agent-SafetyBench框架分析报告.md 生成一张流程图，涵盖摘要、动作、数据、结论等