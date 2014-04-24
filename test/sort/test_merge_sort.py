#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from algorithm.sort.merge_sort import mergeSort
from test_sort import *


class TestMergeSort(TestSorting):

    def testBaseCase(self):
        u"""测试正常情况（随机产生10个数）"""

        self.input = range(10)
        random.shuffle(self.input)
        print 'Sorting unit test data: ', self.input
        self.correct = range(10)

        self.output = mergeSort(self.input)
        print 'Result: ', self.output
        self.assertEqual(self.correct, self.output)

    def testMergeSortCase(self):
        u"""测试文件样例"""

        self._testSortingCase(mergeSort)


if __name__ == '__main__':
    unittest.main()
