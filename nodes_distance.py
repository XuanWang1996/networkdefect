import networkx as nx

# 创建图
G = nx.Graph()

# 添加边
edges = [(0, 1), (1, 2), (2, 3), ...]  # 替换为你的边列表
G.add_edges_from(edges)

# 指定起点节点
start_nodes = [0, 1]  # 节点1和节点2

# 计算最短路径长度
shortest_paths = nx.shortest_path_length(G, source=start_nodes)

# 统计距离为1到10000的节点序号
nodes_with_distance = {distance: [] for distance in range(1, 10001)}
for node, dist in shortest_paths.items():
    if dist <= 10000:
        nodes_with_distance[dist].append(node)

# 输出结果
for distance, nodes in nodes_with_distance.items():
    print(f"距离为 {distance} 的节点序号：")
    print(nodes)
