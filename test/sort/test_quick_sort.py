#!/usr/bin/python
# -*- coding: utf-8 -*-

from algorithm.sort.quick_sort import quickSort
from test_sort import *


class TestQuickSort(TestSorting):

    def testBaseCase(self):
        u"""测试正常情况（随机产生10个数）"""
        self._testBaseCase(quickSort)

    def testQuickSortCase(self):
        u"""测试文件样例"""
        self._testSortingCase(quickSort)


if __name__ == '__main__':
    unittest.main()
