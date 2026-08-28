# 优先级教练 · Priority Coach

优先级教练是一个温和、克制、不压迫的个人成长教练 skill。它不帮用户把一天排满，而是帮用户在混乱里看清 **现在最值得先顾的事**，并落到一个今天就能开始的最小动作。

当前版本 **v0.2.2**，基于 `0.2.1` 做了一次安全加固：
- **全量 opt-in**：所有本地写入（会话摘要 + 完整结果卡）都必须先获得用户明确同意，未同意不落盘
- **能力边界声明**：SKILL.md 新增"能力与信任边界"一节，明确声明本 skill 不联网、不执行 shell、不读写自身数据目录之外的文件
- **发布包瘦身**：维护者用的迭代监控工具不再随发布包分发（见仓库内 `MAINTAINING.md`）

`0.2.1` 相对 `0.1.2` 的主要变化：
- 从“默认先做 5 问”升级为“先路由、再进入状态”
- 新增 `overwhelmed_mode`，处理太乱、太累、选不动的场景
- 统一 OpenClaw 语境与本地记录路径
- 补齐完整状态脚本、最小记忆 schema 与发布文档

## 它能做什么

### 1. 收拢重点
帮助用户从“很多事缠在一起”里，收成当前最该优先的 1–3 件事。

### 2. 定一个今天可开始的动作
把重点落成一个 10–30 分钟可开始的最小动作，而不是一整份完美计划。

### 3. 陪用户过完整天
支持：
- `cold_start`
- `priority_select`
- `today_plan`
- `morning_start`
- `evening_wrap`
- `habit_checkin`
- `overwhelmed_mode`

### 4. 本地保存结果
仅在用户同意时，保存结果卡到本地，方便下次续上。

## 与 0.1.2 相比的关键变化

- **入口改造**：不再默认所有会话都走完整冷启动，而是先判断用户当下最需要哪种帮助
- **过载降级**：新增低负担模式，不再强迫用户继续选 3 件事
- **脚本更完整**：每个状态都有标准脚本和 next step
- **文档更一致**：统一到 OpenClaw，而不是混用 WorkBuddy 文案
- **记录更稳**：优先写入 `~/.openclaw/data/priority-coach/records.json`，兼容旧版 `~/.workbuddy` 路径

## 目录结构

```text
priority-coach/
├── SKILL.md
├── README.md
├── skill-card.md
├── LICENSE
├── references/
│   ├── router.md
│   ├── states.md
│   ├── cold-start.md
│   ├── daily-flows.md
│   ├── memory-schema.md
│   └── copy-tone.md
└── scripts/
    └── record.py
```

## 在 OpenClaw 中使用

### 安装公开版
```bash
~/.openclaw/bin/openclaw skills install @bonniegeng-max/priority-coach
```

### 查看当前 skill 信息
```bash
~/.openclaw/bin/openclaw skills info priority-coach --json
```

### 本地覆盖 / 调试
如果要让本地版本优先生效，可把本目录内容回写到：

```text
~/.openclaw/workspace/skills/priority-coach
```

## 本地记录

本地记录脚本：
```bash
python3 scripts/record.py list
python3 scripts/record.py latest
python3 scripts/record.py path
```

默认数据路径：
```text
~/.openclaw/data/priority-coach/records.json
```

兼容旧路径：
```text
~/.workbuddy/priority-coach/records.json
```

> 规则：只有在用户明确同意“保存 / 记下来”的情况下，才调用保存。

## 隐私边界

- 默认不分享、不自动上传
- 默认只保存结果卡，不保存完整原始回答
- 分享给他人时，只暴露：3 个重点 + 今天最小行动 +（可选）我需要的支持
- 不暴露：原始回答、完整焦虑来源、敏感情绪细节

## 发布前检查建议

- 跑一遍 `cold_start -> priority_select -> today_plan`
- 跑一遍 `overwhelmed_mode`
- 跑一遍 `morning_start`
- 跑一遍 `evening_wrap`
- 试一次 `record.py add/list/latest/delete`
- 检查 README / skill-card / LICENSE / _meta.json 版本一致性

## License

MIT-0
