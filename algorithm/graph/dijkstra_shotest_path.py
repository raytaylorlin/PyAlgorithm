#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

INFINITY = float('inf')


def getGraph(file):
    graph = {}
    for line in file.readlines():
        data = line.strip().split(' ')
        source = int(data[0])
        graph[source] = []
        for edge in data[1:]:
            target = int(edge.split(',')[0])
            length = int(edge.split(',')[1])
            graph[source].append((target, length))
    return graph


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
    score = {}
    # 将起点到其它点的路径长初始化为无穷大
    for u, vList in graph.iteritems():
        score[u] = INFINITY
        for v in vList:
            score[v[0]] = INFINITY
    # 起点到自身的长为0
    score[start] = 0

    for i in range(len(score.keys()) - 1):
        minScore = INFINITY
        print processed
        for v in processed:
            for w, length in graph[v]:
                # 防止出度为0的点在图graph中没有被记录下来
                if not graph.has_key(w):
                    graph[w] = []
                if w not in processed and score[v] + length < minScore:
                    minScore = score[v] + length
                    vstar = v
                    wstar = w
                    print 'v, w =', v, w
                    print 'minScore = ', minScore
        if minScore < INFINITY:
            processed.append(wstar)
            print 'wstar, min = ', wstar, minScore
            score[wstar] = minScore

    return score

if __name__ == '__main__':
    with open('dijkstra5.in') as file:
    # with open('3.txt') as file:
        graph = getGraph(file)
        # print 'graph: ', graph
        result = dijkstraShortestPath(graph, 1)

        for k, v in result.iteritems():
            print '{0}: {1}'.format(k, v)
