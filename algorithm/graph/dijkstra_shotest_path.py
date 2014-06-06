#!/usr/bin/python
# -*- coding: utf-8 -*-


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
    return graph, len(V)


def dijkstraShortestPath(graph, start):
    # 初始化
    vertexNum = len(graph.keys())
    processed = [start]
    score = {
        start: 0
    }

    while len(processed) < len(graph.keys()):
        minScore = 1000000
        print 'X = ', processed
        for v in processed:
            for w, length in graph[v]:
                if not graph.has_key(w):
                    graph[w] = []
                if w not in processed:
                    print '(v, w) = ', v, w
                if w not in processed and score[v] + length < minScore:
                    minScore = score[v] + length
                    vstar = v
                    wstar = w
                    print 'min, v*, w* = ', minScore, vstar, wstar
        processed.append(wstar)
        score[wstar] = minScore

    return score

if __name__ == '__main__':
    # with open('test.txt') as file:
    with open('dijkstraData.txt') as file:
        graph, vertexNum = getGraph(file)
        print 'graph: ', graph, vertexNum
