#!/bin/bash
# auto-sync.sh - 自动同步 OpenClaw Skills 到 GitHub
# 用法: ./auto-sync.sh [commit message]

REPO_DIR="/root/.openclaw/workspace/openclaw-skills"
GIT_REPO="https://github.com/zengliny/openclaw-skills.git"

cd "$REPO_DIR" || exit 1

# 默认提交信息
MSG="${1:-Auto sync: $(date '+%Y-%m-%d %H:%M')}"

# 添加所有更改
git add -A

# 检查是否有更改
if git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
fi

# 提交
git commit -m "$MSG"

# 推送
git push origin main

echo "✅ Synced to GitHub: $MSG"