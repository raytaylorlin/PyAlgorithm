#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import test.util as util
from algorithm.graph.dijkstra_shotest_path import *


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.cases = util.getCases('data', 'dijkstra')

    def testBaseCase(self):
        '''测试正常情况'''

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
        '''测试从起点开始，有个别顶点不可达的情况'''

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
        '''测试从起点开始，所有顶点不可达的情况'''

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


    # def testDijkstraCase(self):
    #     for inputFile, answerFile in self.cases:
    #         print '*' * 20
    #         print 'Test case: ' + inputFile
    #         self.input = getStandardData(inputFile)
    #         self.correct = getStandardData(answerFile)
    #         self.output = mergeSort(self.input)

    #         diff = difflib.context_diff(
    #             map(str, self.correct), map(str, self.output),
    #             fromfile='answer', tofile='result', n=1)
    #         diffResult = '\n'.join(diff)
    #         print diffResult
    #         self.assertTrue(len(diffResult) == 0, 'Wrong answer!')


class DataReader:

    def readStandardInput(inputFile):
        pass

    def readStandardOutput(outputFile):
        pass

if __name__ == '__main__':
    unittest.main()
