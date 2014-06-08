#!/usr/bin/python
# -*- coding: utf-8 -*-

INFINITY = float('inf')


def dijkstraShortestPath(graph, start=1):
    '''使用Dijkstra算法求单源最短路径
    Args:
        graph: 图字典数据（邻接表表示形式，包含边和边长信息）
        例子：graph = {
            1: [(2, 1), (3, 5)],
            4: [(2, 7)]
        } 表示边(1,2)长为1，边(1,3)长为5，边(4,2)长为7
        start: 起点（默认为顶点1）
    Returns:
        从start到图中其它各点的最短距离字典
    '''

    # 初始化
    processed = set([start])
    distance = {}
    # 不能到点的路径长设为无穷大
    for u, vList in graph.iteritems():
        distance[u] = INFINITY
        for v in vList:
            distance[v[0]] = INFINITY
    # 补齐邻接表表示的图缺少的key
    for v in distance.keys():
        if not v in graph:
            graph[v] = []
    # 将起点到它能到的点设为其距离
    for v, l in graph[start]:
        distance[v] = l
    distance[start] = 0

    # 算法主循环
    for i in range(len(distance.keys()) - 1):
        minDistance = INFINITY
        selected = None
        # 找出离起点最近且没有被处理过的点
        for j in distance.keys():
            if j not in processed and distance[j] < minDistance:
                minDistance = distance[j]
                selected = j

        if selected != None:
            # 标记该点已处理过
            processed.add(selected)
            # 更新剩余的点：若经过selected可以使路径更短，则更新
            for target, length in graph[selected]:
                distance[target] = min(
                    distance[target], distance[selected] + length)

    return distance
