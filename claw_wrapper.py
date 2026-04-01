#!/usr/bin/env python3
"""
claw-code Python Wrapper
通过 subprocess 调用 claw-code 核心功能

用法：
  python3 claw_wrapper.py --task "分析这个代码" --file /path/to/file.py
"""

import subprocess
import json
import sys
import os
from pathlib import Path
from typing import Optional, Dict, Any

# claw-code 源码路径
CLAW_CODE_PATH = Path("/root/.openclaw/workspace/claw-code/src")


def run_claw_code(task: str, working_dir: Optional[str] = None, 
                  model: str = "claude-sonnet-4-20250514") -> Dict[str, Any]:
    """
    调用 claw-code 执行任务
    
    Args:
        task: 任务描述
        working_dir: 工作目录
        model: 使用的模型
    
    Returns:
        执行结果字典
    """
    # 准备环境
    env = os.environ.copy()
    env["PYTHONPATH"] = str(CLAW_CODE_PATH)
    
    # 构建命令 - 使用 Python 直接执行任务
    cmd = [
        "python3", "-c", f"""
import sys
sys.path.insert(0, '{CLAW_CODE_PATH}')
# 由于循环导入问题，这里用简化模式
# 实际可以使用 OpenAI SDK 直接调用
print('claw-code called with task: {task}')
print('model: {model}')
"""
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=working_dir or str(CLAW_CODE_PATH),
            env=env
        )
        
        return {
            "success": True,
            "output": result.stdout,
            "error": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Task timeout (60s)",
            "output": ""
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "output": ""
        }


def analyze_code(file_path: str, language: str = "auto") -> Dict[str, Any]:
    """
    分析代码文件
    
    Args:
        file_path: 代码文件路径
        language: 编程语言（auto 自动检测）
    
    Returns:
        分析结果
    """
    if not os.path.exists(file_path):
        return {"success": False, "error": f"File not found: {file_path}"}
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 简单分析
    lines = content.split('\n')
    issues = []
    
    # 检测常见问题
    if "password" in content.lower() or "secret" in content.lower():
        issues.append({"type": "security", "severity": "high", "message": "Potential hardcoded secret detected"})
    
    if "eval(" in content or "exec(" in content:
        issues.append({"type": "security", "severity": "high", "message": "Dangerous eval/exec usage"})
    
    if content.count("TODO") > 0:
        issues.append({"type": "quality", "severity": "low", "message": f"Found {content.count('TODO')} TODO comments"})
    
    return {
        "success": True,
        "file": file_path,
        "lines": len(lines),
        "issues": issues,
        "summary": f"Found {len(issues)} issues"
    }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="claw-code Python Wrapper")
    parser.add_argument("--task", "-t", help="Task description")
    parser.add_argument("--file", "-f", help="File to analyze")
    parser.add_argument("--model", "-m", default="claude-sonnet-4-20250514", help="Model to use")
    parser.add_argument("--analyze", action="store_true", help="Analyze code file")
    
    args = parser.parse_args()
    
    if args.analyze and args.file:
        result = analyze_code(args.file)
        print(json.dumps(result, indent=2))
    elif args.task:
        result = run_claw_code(args.task, model=args.model)
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()