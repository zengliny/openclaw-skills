# OpenClaw Skills 自动化同步指南

## 🎯 目标
实现本地修改 → 自动 push → GitHub 仓库同步

---

## 📂 目录结构

```
openclaw-skills/
├── skills/                 # Skills 目录
│   ├── claw-code-review/
│   ├── agency-caller/
│   └── hybrid-optimizer/
├── cron-scripts/           # 定时脚本
│   └── auto-code-review.sh
├── scripts/                # 自动化脚本
│   └── auto-sync.sh        # ⭐ 自动同步脚本
├── claw_wrapper.py         # claw-code 封装器
├── hybrid-optimizer-plus/  # 增强版
└── README.md
```

---

## 🚀 快速开始

### 方式一：本地修改后自动同步

```bash
# 进入工作目录
cd /root/.openclaw/workspace/openclaw-skills

# 修改文件后执行
./scripts/auto-sync.sh "更新内容描述"
```

### 方式二：通过 AI Agent 直接创建

```
告诉 Agent：帮我创建一个新的 Skill
↓
Agent 写文件 → 自动 push → 完成
```

---

## 🔧 手动同步命令

```bash
# 添加所有更改
git add -A

# 提交
git commit -m "your message"

# 推送
git push origin main
```

---

## ⏰ 自动同步 Cron（可选）

```bash
# 每天早上 6 点自动同步
crontab -e
0 6 * * * /root/.openclaw/workspace/openclaw-skills/scripts/auto-sync.sh "Daily auto sync"
```

---

## 📋 常用操作

| 操作 | 命令 |
|------|------|
| 拉取最新 | `git pull origin main` |
| 查看状态 | `git status` |
| 查看历史 | `git log --oneline` |
| 强制推送 | `git push -f origin main` |

---

*更新时间: 2026-04-01*