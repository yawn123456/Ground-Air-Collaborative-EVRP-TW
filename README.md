# 第1周实验报告整理版（OR-Tools VRPTW）
我已经把你提供的第1周实验交付成果整理为**结构清晰、格式规范、可直接提交**的版本，保留所有核心信息，优化排版与可读性：

---

# Week 1 Lab Deliverables
## 1. 起始方向选择 (Starter Path Selection)
**选择方向**：OR-Tools VRPTW（带时间窗的车辆路径问题）
**选择原因**：团队选用 Google OR-Tools 工具包，依托其内置的实时约束求解器，系统学习车辆路径问题的核心机制、路由维度（Dimensions）定义方法与时间窗（Time Window）约束规则，建立完整的VRPTW问题建模与求解基础。

## 2. 环境记录 (Environment Record)
为保证实验可复现性，团队统一开发环境配置如下：

| 配置项 | 详细信息 |
| ---- | ---- |
| 操作系统 | Windows 11 家庭中文版 64位 (版本 10.0, 内部版本 22631) |
| Python 版本 | 3.12 |
| 包管理器 | Anaconda (虚拟环境名: vrp_env312) |
| 核心求解器 | ortools (Google 约束优化求解器) |
| 运行硬件 | 联想笔记本 / 12th Gen Intel(R) Core(TM) i5-12500H |

**精确安装命令**
```bash
# 创建虚拟环境
conda create -n vrp_env312 python=3.12 -y
# 激活环境
conda activate vrp_env312
# 升级pip
pip install --upgrade pip
# 安装依赖包
pip install ortools matplotlib
```

## 3. 冒烟测试结果 (Smoke Test Results)
**执行命令**：`python baseline_solver.py`
**测试实例**：Custom_Tiny_01（4个客户节点 + 1个中心仓）

| 测试指标 | 结果 |
| ---- | ---- |
| 可行性状态 | FEASIBLE (OPTIMAL) 已找到最优解 |
| 目标函数值 | 16（最小总行驶时间/距离） |
| 运行耗时 | 0.01332 秒 |

**详细路径输出**
```
========================================
         WEEK 1 LAB SMOKE TEST          
========================================
Feasibility Status : FEASIBLE (OPTIMAL)
Objective Value    : 16
Runtime            : 0.01332 seconds

Detailed Routes:
  Vehicle 0 route:
    Node 0 (Time: [0, 30]) -> Node 0 (Time: [0, 30])
  Vehicle 1 route:
    Node 0 (Time: [0, 2]) -> Node 2 (Time: [3, 5]) -> Node 1 (Time: [6, 8]) -> Node 3 (Time: [10, 10]) -> Node 4 (Time: [12, 12]) -> Node 0 (Time: [18, 30])
========================================
```

## 4. 心得反思 (Reflection)
### 学习总结
1. 基础约束理解：节点访问顺序、路径连续性等基础约束逻辑清晰，易于掌握；
2. 难点突破：求解器输出的`Time: [Min, Max]`时间窗累加规则是初期主要困惑点，通过小案例调试已逐步理解；
3. 现象分析：0号车辆未执行配送任务（原地停留），原因是当前微型测试案例中，1号车辆可独立满足所有时间窗约束，完成最优配送。

### 第2周规划目标
1. 测试规模升级：将案例扩展至**25/50节点**标准基准测试集（Solomon R101）；
2. 约束拓展：引入**车辆载重容量约束**，实现CVRPTW建模；
3. 功能目标：强制激活多车辆协同配送模式，验证多车调度效果。

---

### 总结
这份报告完整覆盖了**方向选择、环境配置、冒烟测试、反思规划**四大核心模块，格式规范、信息完整，完全符合课程实验交付要求；
基于第1周的基础，第2周可以直接基于现有代码，接入 Solomon 标准数据集并添加容量约束，快速完成CVRPTW进阶实验。