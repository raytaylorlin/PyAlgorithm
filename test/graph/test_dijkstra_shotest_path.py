#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import test.util as util
from algorithm.graph.dijkstra_shotest_path import *

logger = util.getLogger('test.graph.dijkstra')


class TestDijkstra(util.PyAlgorithmTestCase):
    TEST_CASE_FORMAT = '''
    Input: graph = %s
    Input: start vertex = %s
    Result: %s
    '''

    def setUp(self):
        super(TestDijkstra, self).setUp(logger)
        self.cases = util.getInputAnswerCases('data', 'dijkstra')

    def testBaseCase(self):
        u"""测试正常情况"""

        graph = {
            1: [(2, 1), (3, 4)],
            2: [(3, 2), (4, 6)],
            3: [(4, 3)]
        }
        start = 1
        self.correct = {
            1: 0,
            2: 1,
            3: 3,
            4: 6
        }
        self.output = dijkstraShortestPath(graph, start)

        logger.debug(TestDijkstra.TEST_CASE_FORMAT, graph, start, self.output)
        self.assertEqual(self.correct, self.output)

    def testSomeVerticeUnreachable(self):
        u"""测试从起点开始，有个别顶点不可达的情况"""

        graph = {
            1: [(2, 1), (3, 2)],
            4: [(2, 3)]
        }
        start = 1
        self.correct = {
            1: 0,
            2: 1,
            3: 2,
            4: INFINITY
        }
        self.output = dijkstraShortestPath(graph, start)

        logger.debug(TestDijkstra.TEST_CASE_FORMAT, graph, start, self.output)
        self.assertEqual(self.correct, self.output)

    def testAllVerticesUnreachable(self):
        u"""测试从起点开始，所有顶点不可达的情况"""

        graph = {
            1: [(2, 1), (3, 2)],
            4: [(2, 3)]
        }
        start = 2
        self.correct = {
            1: INFINITY,
            2: 0,
            3: INFINITY,
            4: INFINITY
        }
        self.output = dijkstraShortestPath(graph, start)

        logger.debug(TestDijkstra.TEST_CASE_FORMAT, graph, start, self.output)
        self.assertEqual(self.correct, self.output)

    # @unittest.skip('test from file')
    def testDijkstraCase(self):
        u"""测试文件样例"""

        def standardizeInput(content):
            graph = {}
            for line in content.split('\n'):
                data = line.strip().split(' ')
                graph[int(data[0])] = [(int(edge.split(',')[0]), int(edge.split(',')[1]))
                                       for edge in data[1:]]
            # 此处默认起点为顶点1
            return {'graph': graph, 'start': 1}

        def standaradizeAnswer(content):
            pathLength = {}
            for line in content.split('\n'):
                edge = line.split(': ')
                pathLength[int(edge[0])] = int(edge[1])
            return pathLength

        self._testFileCase(
            dijkstraShortestPath, standardizeInput, standaradizeAnswer)


if __name__ == '__main__':
    unittest.main(verbosity=1)
