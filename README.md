# company-brief · 会前公司速读

> 本技能是 **visitread-codex 的拆解版**：原版把"查公司"和"查人"合在一个技能里，本仓库把它拆成独立技能（company-brief 管公司、person-brief 管人物），用哪个装哪个，触发更直接、响应更快。

会前公司速读：给 BD / 销售在拜访客户前用。把公司名发过来，它联网查这家公司的公开资料，整理成一份报告，让你进门前心里有数。

- **你要给它的**：公司名称 / 公司网址 / 我方业务 / 会面目的
- **它给你的**：一份 HTML 报告文件（速读卡 / 公司快照 / 招聘信号 / 风险信号 / 会面话题 / Fit 评估 / 社交账号 / 检索记录），浏览器打开查看

## 安装

本 skill 在 **WorkBuddy** 上实测可用，安装到 WorkBuddy 的 skills 目录（`~/.workbuddy/skills/`）。

**WorkBuddy · macOS / Linux：**

```bash
git clone https://github.com/Yara918/company-brief.git "$HOME/.workbuddy/skills/company-brief"
```

**WorkBuddy · Windows PowerShell：**

```powershell
git clone https://github.com/Yara918/company-brief.git "$env:USERPROFILE\.workbuddy\skills\company-brief"
```

**手动安装（任意系统）：**

```bash
# 1. 克隆到本地
git clone https://github.com/Yara918/company-brief.git

# 2. 把整个目录放进 skills 目录
cp -r company-brief ~/.workbuddy/skills/company-brief
```

## 使用

在对话里直接说，把示例中的信息换成实际的：

```
帮我做一份会前公司速读：公司：某某科技；网址：https://xxx；我方业务：ERP 实施；会面目的：业务合作
```

信息齐全会自动开工：联网检索 → 生成报告 → 链接校验（无效链接拦截后换真实内容再交付）。

## 目录结构

```
company-brief/
├── SKILL.md               # 主文件（工作流 / 输入 / 规则 / 报告结构）
├── README.md
├── references/reference.md     # 分层查询 / 字数 / 免责声明
├── scripts/
│   ├── make-queries.py    # 检索清单生成
│   └── verify-links.py    # 链接真实性校验（交付前必跑）
├── report-template.html   # 商务 HTML 模板
├── examples/              # 虚构示例报告
└── tests/                 # 自检
```

## 测试情况

- 本 skill 在 **WorkBuddy** 上实测通过（输入 → 联网检索 → HTML 报告 → 聊天交付）。
- **不同模型的产出结果会有差异**（排版 / 检索质量 / 规则遵守随模型能力波动）：建议用自己的模型实测一轮，找到最适合你的模型与生成方式；报告质量以机器校验（verify-links.py，覆盖链接 / 敏感词 / KPI / 来源 / HTML 结构）为准。
- 已知情况：Claude Code 接 DeepSeek 模型时，聊天窗口可能不输出交付句（模型缺陷，报告文件可正常生成）。

## 设计原则

1. 链接必须来自本次联网检索结果，禁止编造 / 拼接；无效链接由校验脚本拦截。
2. 每条内容带可点来源按钮，按钮文字描述来源，禁止统一写「来源」。
3. 打不开 / 空壳 / 内容不符的链接不引用。
4. 财务数据用全年 + 同比 + 趋势，负面信号进风险区。
5. 查不到如实写「未检索到」+ 检索记录，绝不编造。
6. 技能文件不含真实公司名 / 人名 / 敏感词。

## 说明

- 示例均为虚构（公司 / 人名为代称），不含真实客户信息。
- 报告基于公开网络信息生成，仅供拜访前参考，不构成投资或商业决策依据。

## License

MIT — 见 [LICENSE](LICENSE)。
