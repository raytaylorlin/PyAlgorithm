#!/usr/bin/python
# -*- coding: utf-8 -*-

from algorithm.sort.insertion_sort import *
from test_sort import *


class TestInsertionSort(TestSorting):

    def testBaseCase(self):
        u"""测试正常情况（随机产生10个数）"""
        self._testBaseCase(insertionSort)

    def testMergeSortCase(self):
        u"""测试文件样例"""
        self._testSortingCase(insertionSort)


if __name__ == '__main__':
    unittest.main()
