#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import test.util as util
from algorithm.datastructure.heap import Heap


logger = util.getLogger('test.datastructure')


class TestHeap(util.PyAlgorithmTestCase):

    def setUp(self):
        super(TestHeap, self).setUp(logger)

    def testSize(self):
        u"""测试堆的获取尺寸方法"""

        self.input = range(5)
        self.correct = 5
        heap = Heap(self.input)
        self.output = heap.size()

        self.assertEqual(self.correct, self.output)


if __name__ == '__main__':
    unittest.main()
