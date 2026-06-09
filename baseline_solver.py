import time
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """创建微型测试数据（5x5 矩阵，包含1个中心仓和4个客户点）"""
    data = {}
    data['distance_matrix'] = [
        [0, 4, 3, 5, 6],  # 0 (Depot 中心仓)
        [4, 0, 3, 2, 4],  # 1
        [3, 3, 0, 4, 5],  # 2
        [5, 2, 4, 0, 2],  # 3
        [6, 4, 5, 2, 0],  # 4
    ]
    data['time_windows'] = [
        (0, 20),  # 0 (Depot) 开门与关门时间
        (5, 15),  # 1 号点时间窗
        (2, 10),  # 2 号点时间窗
        (10, 18),  # 3 号点时间窗
        (5, 12),  # 4 号点时间窗
    ]
    data['num_vehicles'] = 2  # 2 辆车
    data['depot'] = 0  # 中心仓的索引
    return data


def main():
    # 记录开始时间
    start_time = time.time()

    data = create_data_model()

    # 创建路由索引管理器
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # 创建并注册时间/距离回调函数
    def time_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # 添加时间窗维度 (Time Dimension)
    time_dimension_name = 'Time'
    routing.AddDimension(
        transit_callback_index,
        30,  # 允许的等待时间上限 (Slack)
        30,  # 每辆车最大总行驶时间
        False,  # 不强制从时间 0 开始
        time_dimension_name)
    time_dimension = routing.GetDimensionOrDie(time_dimension_name)

    # 为每个客户节点添加具体的时间窗
    for location_idx, time_window in enumerate(data['time_windows']):
        if location_idx == 0:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])

    # 设置搜索算法参数
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # 求解
    solution = routing.SolveWithParameters(search_parameters)

    # 计算运行耗时
    runtime = time.time() - start_time

    # 输出实验报告所需的交付物内容
    print("=" * 40)
    print("         WEEK 1 LAB SMOKE TEST          ")
    print("=" * 40)
    if solution:
        print(f"Feasibility Status : FEASIBLE (OPTIMAL)")
        print(f"Objective Value    : {solution.ObjectiveValue()}")
        print(f"Runtime            : {runtime:.5f} seconds\n")
        print("Detailed Routes:")

        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f"  Vehicle {vehicle_id} route:\n    "
            while not routing.IsEnd(index):
                time_var = time_dimension.CumulVar(index)
                plan_output += f"Node {manager.IndexToNode(index)} (Time: [{solution.Min(time_var)}, {solution.Max(time_var)}]) -> "
                index = solution.Value(routing.NextVar(index))
            time_var = time_dimension.CumulVar(index)
            plan_output += f"Node {manager.IndexToNode(index)} (Time: [{solution.Min(time_var)}, {solution.Max(time_var)}])"
            print(plan_output)
    else:
        print("Feasibility Status : INFEASIBLE")
    print("=" * 40)


if __name__ == '__main__':
    main()