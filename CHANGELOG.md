# Changelog

优先级教练 Priority Coach（`priority-coach`）的版本变更记录。

- 最新版本：**0.3.3**
- 发布渠道：[ClawHub](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- 版本数：11（含初始版本）

> 本文件由 ClawHub registry 的逐版本发布记录回溯整理生成（2026-09-29）。此后每次发版请在此追加一条。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

- 新增本 CHANGELOG.md，回溯整理 0.1.0 → 0.3.3 的历史版本记录（内容取自 ClawHub 逐版本发布记录，未改动代码）

## [0.3.3] - 2026-09-19

License consistency fix: LICENSE is standard MIT (with attribution clause) while SKILL.md frontmatter / README / skill-card said MIT-0 (MIT No Attribution). Unified to MIT across the repo. Note: the MIT-0 shown on the ClawHub skill page is the platform's own generated metadata field and cannot be set via clawhub publish — the repository LICENSE file is authoritative.

## [0.3.2] - 2026-09-13

discoverability fix — categories and topics now set (was 'other'); description leads with a bilingual problem statement plus a Not-for clause; SKILL.md gains When-not-to-use / How-it-differs sections. No behavior change.

## [0.3.1] - 2026-09-03

v0.3.1: 补脚本用途说明与案例示意, displayName 修正

## [0.3.0] - 2026-08-28

新增 mainline_review 状态：断更承接（停了一阵回来接着上次，不重跑冷启动不审判中断）+ 主线重检（稳/漂/下车三栏卡）；补齐定优先级→做→回顾的方法论闭环

## [0.2.3] - 2026-08-28

修复 states.md：7 处记录动作从默认写入改为用户同意后写入，文件头加记录铁律，与 SKILL.md 同意条款完全一致

## [0.2.2] - 2026-08-28

安全加固：本地记录全量 opt-in（修复与同意条款矛盾）；新增能力与信任边界声明（不联网/不执行shell/不越目录读写）；发布包移除维护者监控工具

## [0.2.1] - 2026-08-28

0.2.1: added dual-layer local storage, session summaries, weekly review tooling, and documentation updates for AI-suggested, human-reviewed iteration.

## [0.2.0] - 2026-08-26

0.2.0: state-based v2 release with routing, overwhelmed mode, full state scripts, OpenClaw-aligned local memory, and updated docs.

## [0.1.2] - 2026-08-23

行动优先：先动起来再做清楚，找方向而非排满日程；背景定位与核心原则加入行动优先哲学

## [0.1.1] - 2026-08-23

priority-coach 0.1.1 更新日志

- 新增本地记录脚本（scripts/record.py），可增删查历史主线结果，提升回溯和对比体验
- 本地数据记录功能说明细化，收录脚本用法与交互规范
- 强化主功能不涉上传，确保数据只存在本地
- 交互流程加入状态分支，根据不同状态生成不同风格和类型的“最小行动”
- 明确“悦己”也可成为优先级，优化相关表述
- 移除 skill-card.md，简化资源结构

## [0.1.0] - 2026-08-23

Initial release of priority-coach: a gentle, non-pressuring coaching skill for personal prioritization and growth.

- Guides users to clarify and select their top 3 current priorities using 5 concise, empathetic questions inspired by 《会赚时间的妈妈》.
- Focuses on clarity, not busyness: supports daily planning, morning routines, evening reflections, and habit building.
- Features a private-by-default design, minimal input required, and multiple summarization steps to help users find their own growth "main line."
- Provides structured outputs: top 3 priorities, today’s smallest actionable step, and things to postpone.
- Designed with a gentle tone—no judgment, no pressure, and never overloads the user.
