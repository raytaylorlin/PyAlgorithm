#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

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
        归并排序后的数组

    '''

    # 初始化
    vertexNum = len(graph.keys())
    processed = [start]
    pathLength = {}
    # 将起点到其它点的路径长初始化为无穷大
    for u, vList in graph.iteritems():
        pathLength[u] = INFINITY
        for v in vList:
            pathLength[v[0]] = INFINITY
    # 起点到自身的长为0
    pathLength[start] = 0

    for i in range(len(pathLength.keys()) - 1):
        minPathLength = INFINITY
        # print processed
        for v in processed:
            if not graph.has_key(v):
                graph[v] = []
            for w, length in graph[v]:
                # 防止出度为0的点在图graph中没有被记录下来
                if not graph.has_key(w):
                    graph[w] = []
                if w not in processed and pathLength[v] + length < minPathLength:
                    minPathLength = pathLength[v] + length
                    vstar = v
                    wstar = w
                    # print 'v, w =', v, w
                    # print 'minPathLength = ', minPathLength
        if minPathLength < INFINITY:
            processed.append(wstar)
            # print 'wstar, min = ', wstar, minPathLength
            pathLength[wstar] = minPathLength

    return pathLength
