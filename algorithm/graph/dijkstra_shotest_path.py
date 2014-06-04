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
    return graph


def dijkstraShotestPath(graphOrigin, graphReverse):
    pass


if __name__ == '__main__':
    # with open('test.txt') as file:
    with open('dijkstraData.txt') as file:
        graph = getGraph(file)
        print 'graph: ', graph
