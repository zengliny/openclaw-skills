# hybrid-optimizer-plus Skill

> 结合 claw-code 任务编排 + agency-agents 角色能力 + claw-code 源码深度集成

## 描述
混合优化器增强版，深度集成 claw-code 源码能力：
- 直接调用 claw-code 的 Python 模块（通过 wrapper）
- 利用 claw-code 的任务分析能力
- 支持代码分析和安全扫描

## 触发词
- "复杂任务"
- "多步骤处理"
- "深度优化"
- "用 claw-code"
- "完整方案"

## 新增能力

### 1. claw-code 集成
```python
# 可直接调用 claw-code 核心功能
from claw_wrapper import analyze_code, run_claw_code

# 代码分析
result = analyze_code("/path/to/code.py")

# 任务执行
result = run_claw_code("分析这段代码的安全问题")
```

### 2. 增强的任务分析
- 使用 claw-code 的 query_engine 进行意图分析
- 自动选择最优的执行路径
- 支持多轮对话上下文

### 3. 高级代码审查
- 结合 claw-code 的安全检测能力
- 使用 agency-agents 的 Code_Reviewer 角色
- 生成更详细的修复建议

## 与原版 hybrid-optimizer 的区别

| 功能 | 原版 | Plus 版 |
|------|------|---------|
| 角色调用 | agency-agents | agency-agents + claw-code |
| 代码分析 | 基础正则 | claw-code 深度分析 |
| 任务编排 | 简单队列 | query_engine 智能编排 |
| 安全扫描 | 基础规则 | 多引擎组合 |

## 使用示例

### 示例 1：深度代码审查
```
用户：用 claw-code 深度审查这段代码
↓
hybrid-optimizer-plus:
  1. 调用 claw_wrapper.analyze_code() 基础分析
  2. 调用 agency Code_Reviewer 角色深度审查
  3. 合并结果，生成修复建议
↓
输出：详细的代码问题报告 + 修复代码
```

### 示例 2：智能任务拆分
```
用户：帮我做一个用户认证系统
↓
hybrid-optimizer-plus:
  1. 使用 claw-code query_engine 分析任务
  2. 识别需要的后端组件：Login, Register, PasswordReset
  3. 依次调用：
     - Backend Architect → API 设计
     - Security Engineer → 安全审查
     - Frontend Developer → 前端实现
↓
输出：完整的系统设计方案
```

## 配置文件

```yaml
# ~/.openclaw/config.yaml

hybrid_optimizer_plus:
  # claw-code 源码路径
  claw_code_path: /root/.openclaw/workspace/claw-code
  
  # claw-code wrapper 脚本
  claw_wrapper: /root/.openclaw/workspace/claw-code-integration/claw_wrapper.py
  
  # 启用深度分析
  deep_analysis: true
  
  # 最大并发任务
  max_parallel: 5
  
  # 超时时间（秒）
  timeout: 300
```

## 依赖

```bash
# 安装依赖
pip install openai anthropic

# 或者通过 npx 运行 claw-code
npm install -g claw-code
```

---

*版本：v1.1 | 更新：2026-04-01 | 特性：claw-code 深度集成*