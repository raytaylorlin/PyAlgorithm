#!/usr/bin/python
# -*- coding: utf-8 -*-

from algorithm.sort.heap_sort import heapSort
from test_sort import *


class TestQuickSort(TestSorting):

    def testBaseCase(self):
        u"""测试正常情况（随机产生10个数）"""
        self._testBaseCase(heapSort)

    def testQuickSortCase(self):
        u"""测试文件样例"""
        self._testSortingCase(heapSort)


if __name__ == '__main__':
    unittest.main()
