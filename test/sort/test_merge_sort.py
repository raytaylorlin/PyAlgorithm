#!/usr/bin/python
# -*- coding: utf-8 -*-

from algorithm.sort.merge_sort import *
from test_sort import *


class TestMergeSort(TestSorting):
    TEST_MERGE_FORMAT = '''
    Input: leftList = %s rightList = %s
    Result: %s
    '''

    def testMerge(self):
        u"""测试合并两个有序数组"""

        self.input = {
            'leftList': [1, 3, 5],
            'rightList': [2, 4, 6]
        }
        self.correct = [1, 2, 3, 4, 5, 6]
        self.output = merge(**self.input)

        logger.debug(TestMergeSort.TEST_MERGE_FORMAT, self.input[
                     'leftList'], self.input['rightList'], self.output)
        self.assertEqual(self.correct, self.output)

    def testBaseCase(self):
        u"""测试正常情况（随机产生10个数）"""
        self._testBaseCase(mergeSort)

    def testMergeSortCase(self):
        u"""测试文件样例"""
        self._testSortingCase(mergeSort)


if __name__ == '__main__':
    unittest.main()
