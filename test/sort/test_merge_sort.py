#!/usr/bin/python
# -*- coding: utf-8 -*-

from algorithm.sort.merge_sort import mergeSort
from test_sort import *


class TestMergeSort(TestSorting):

    def testBaseCase(self):
        self._testBaseCase(mergeSort)

    def testMergeSortCase(self):
        u"""测试文件样例"""

        self._testSortingCase(mergeSort)


if __name__ == '__main__':
    unittest.main()
