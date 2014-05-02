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
        heap = Heap(self.input)
        self.assertEqual(5, heap.size())

    def testBubbleDown(self):
        u"""测试堆的向下冒泡调整操作"""

        heap = Heap()
        heap._heap = [3, 2, 4, 5, 1]

        # 调整第2个元素
        heap._bubbleDown(1)
        self.assertEqual([3, 1, 4, 5, 2], heap._heap)
        # 调整根元素
        heap._bubbleDown(0)
        self.assertEqual([1, 2, 4, 5, 3], heap._heap)

    def testBuildHeap(self):
        u"""测试堆的初始化并建立最小堆"""

        heap = Heap([3, 2, 6, 4, 1, 5])
        self.assertEqual([1, 2, 5, 4, 3, 6], heap._heap)

if __name__ == '__main__':
    unittest.main()
