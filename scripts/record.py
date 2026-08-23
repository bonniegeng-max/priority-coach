#!/usr/bin/env python3
"""优先级教练 · 本地记录管理

读写 ~/.workbuddy/priority-coach/records.json，让"查看上次结果 / 我的主线变了吗
/ 删除记录"成为确定性可靠的能力，而不是靠模型临时记忆。

用法（在 skill 流程中由 agent 调用）：
  python3 scripts/record.py add    --data '<json>'
  python3 scripts/record.py list
  python3 scripts/record.py latest
  python3 scripts/record.py get    [--date YYYY-MM-DD | --index N]
  python3 scripts/record.py delete [--date YYYY-MM-DD | --index N | --all]
  python3 scripts/record.py export

记录字段（至少包含）：
  date                日期（缺省自动填今天）
  state               Q1 状态：自我修复 / 工作冲刺 / 家庭优先 / 三者都要
  topPriorities      当前 3 个优先事项（字符串数组）
  smallestActionToday 今天最小行动（字符串）
  notNow             先不碰的事（字符串数组）
  candidates         可选：AI 归纳出的候选方向
  rawAnswers         可选：用户原始回答
"""
import argparse
import datetime
import json
import os
import sys

STORE_DIR = os.path.expanduser("~/.workbuddy/priority-coach")
STORE = os.path.join(STORE_DIR, "records.json")


def load():
    if not os.path.exists(STORE):
        return {"records": []}
    try:
        with open(STORE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict) or "records" not in data:
            data = {"records": []}
    except Exception:
        data = {"records": []}
    return data


def save(data):
    os.makedirs(STORE_DIR, exist_ok=True)
    with open(STORE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def cmd_add(args):
    try:
        rec = json.loads(args.data)
    except Exception as e:
        print("ERROR: --data 必须是合法 JSON：%s" % e, file=sys.stderr)
        sys.exit(1)
    if not isinstance(rec, dict):
        print("ERROR: 记录必须是 JSON 对象", file=sys.stderr)
        sys.exit(1)
    rec.setdefault("date", datetime.date.today().isoformat())
    data = load()
    data["records"].insert(0, rec)  # 最新置顶
    save(data)
    print("已保存。当前共 %d 条记录。" % len(data["records"]))
    print(json.dumps(rec, ensure_ascii=False, indent=2))


def cmd_list(args):
    data = load()
    recs = data["records"]
    if not recs:
        print("（暂无记录）")
        return
    for i, r in enumerate(recs):
        date = r.get("date", "?")
        tops = " / ".join(r.get("topPriorities", []) or [])
        act = r.get("smallestActionToday", "")
        print("%d. %s  |  %s  |  最小行动：%s" % (i + 1, date, tops, act))


def cmd_latest(args):
    data = load()
    if not data["records"]:
        print("（暂无记录）")
        return
    print(json.dumps(data["records"][0], ensure_ascii=False, indent=2))


def cmd_get(args):
    data = load()
    recs = data["records"]
    if not recs:
        print("（暂无记录）")
        return
    if args.date:
        for r in recs:
            if r.get("date") == args.date:
                print(json.dumps(r, ensure_ascii=False, indent=2))
                return
        print("未找到日期 %s" % args.date, file=sys.stderr)
        sys.exit(1)
    idx = args.index or 1
    if not (1 <= idx <= len(recs)):
        print("索引越界", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(recs[idx - 1], ensure_ascii=False, indent=2))


def cmd_delete(args):
    data = load()
    recs = data["records"]
    if not recs:
        print("（暂无记录）")
        return
    if args.all:
        data["records"] = []
        save(data)
        print("已清空所有记录。")
        return
    if args.date:
        before = len(recs)
        data["records"] = [r for r in recs if r.get("date") != args.date]
        save(data)
        print("删除了 %d 条。" % (before - len(data["records"])))
        return
    idx = args.index or 1
    if not (1 <= idx <= len(recs)):
        print("索引越界", file=sys.stderr)
        sys.exit(1)
    removed = recs[idx - 1]
    data["records"].pop(idx - 1)
    save(data)
    print("已删除：%s" % removed.get("date", "?"))


def cmd_export(args):
    print(json.dumps(load(), ensure_ascii=False, indent=2))


def main():
    p = argparse.ArgumentParser(description="优先级教练本地记录")
    sub = p.add_subparsers(dest="cmd")
    a = sub.add_parser("add")
    a.add_argument("--data", required=True)
    sub.add_parser("list")
    sub.add_parser("latest")
    g = sub.add_parser("get")
    g.add_argument("--date")
    g.add_argument("--index", type=int)
    d = sub.add_parser("delete")
    d.add_argument("--date")
    d.add_argument("--index", type=int)
    d.add_argument("--all", action="store_true")
    sub.add_parser("export")
    args = p.parse_args()
    if args.cmd == "add":
        cmd_add(args)
    elif args.cmd == "list":
        cmd_list(args)
    elif args.cmd == "latest":
        cmd_latest(args)
    elif args.cmd == "get":
        cmd_get(args)
    elif args.cmd == "delete":
        cmd_delete(args)
    elif args.cmd == "export":
        cmd_export(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
