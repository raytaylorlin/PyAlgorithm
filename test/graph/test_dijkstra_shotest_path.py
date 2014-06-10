#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import test.util as util
import difflib
from algorithm.graph.dijkstra_shotest_path import *


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.cases = util.getInputAnswerCases('data', 'dijkstra')
        print "\n[TEST]", self.shortDescription()

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

        print 'Input: graph = {0}'.format(graph)
        print 'Input: start vertex = {0}'.format(start)
        self.output = dijkstraShortestPath(graph, start)
        print 'Result: ', self.output
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

        print 'Input: graph = {0}'.format(graph)
        print 'Input: start vertex = {0}'.format(start)
        self.output = dijkstraShortestPath(graph, start)
        print 'Result: ', self.output
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
            return graph

        def standaradizeAnswer(content):
            pathLength = {}
            for line in content.split('\n'):
                edge = line.split(': ')
                pathLength[int(edge[0])] = int(edge[1])
            return pathLength

        for inputFile, answerFile in self.cases:
            print '*' * 20
            print 'Test case: ' + inputFile
            self.input = util.readFileAndStandardize(
                inputFile, standardizeInput)
            self.correct = util.readFileAndStandardize(
                answerFile, standaradizeAnswer)
            self.output = dijkstraShortestPath(self.input, 1)

            diff = difflib.context_diff(
                map(str, self.correct), map(str, self.output),
                fromfile='answer', tofile='result', n=1)
            diffResult = '\n'.join(diff)
            print diffResult
            self.assertTrue(len(diffResult) == 0, 'Wrong answer!')


if __name__ == '__main__':
    unittest.main()
