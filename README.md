📋 第 1 周实验交付成果 (Week 1 Lab Deliverables)1. 起始方向选择 (Starter Path Selection)选择的方向： OR-Tools VRPTW 方向选择原因： 我们团队选择了 Google OR-Tools，以便通过其实时约束求解器，建立对车辆路径问题机制、路由维度（Dimensions）以及时间窗（Time Window）约束的扎实理解。2. 环境记录 (Environment Record)以下是团队开发环境的精确配置，以确保实验结果的严格可复现性：配置项详细信息操作系统 (OS)Windows 11 家庭中文版 64位 (版本 10.0, 内部版本 22631)Python 版本3.12包管理器Anaconda (虚拟环境名: vrp_env312)求解器及版本ortools (Google Constraint Optimization 求解器)运行硬件联想笔记本电脑 / 12th Gen Intel(R) Core(TM) i5-12500H精确的安装命令：Bashconda create -n vrp_env312 python=3.12 -y
conda activate vrp_env312
pip install --upgrade pip
pip install ortools matplotlib
3. 冒烟测试结果 (Smoke Test Results)执行命令： python baseline_solver.py实例名称与规模： Custom_Tiny_01 (4个客户节点，1个中心仓)可行性状态： FEASIBLE (OPTIMAL) —— 求解器成功找到最优解目标函数值 (Objective Value)： 16 (代表完成所有配送所需的最小总行驶时间/距离)运行耗时 (Runtime)： 0.01332 秒路径文本输出 (Route Text)：Plaintext========================================
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
4. 心得反思 (Reflection)在各项约束中，最容易理解的是基础的节点访问顺序和路径连续性。然而，求解器输出的 Time: [Min, Max] 累加时间窗口在刚开始时有些令人困惑。我们观察到 0 号车直接留在了中心仓（Node 0 -> Node 0），这是因为在当前的微型数据下，1 号车一辆车就足以在严格的时间窗内，以最优的路径访问完所有节点。在第 2 周，我们的基准目标是将测试规模扩展到标准的 25 或 50 节点基准测试集（如 Solomon R101 实例），并尝试引入车辆载重容量约束（CVRPTW），从而强制激活并利用多辆车协同配送。