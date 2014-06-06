#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from algorithm.graph.dijkstra_shotest_path import dijkstraShortestPath


class TestDijkstra(unittest.TestCase):

    def testDijkstra(self):
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


if __name__ == '__main__':
    unittest.main()
