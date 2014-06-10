#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from algorithm.sort.merge_sort import mergeSort
from test_sort import *


class TestMergeSort(TestSorting):

    def testBaseCase(self):
        self.input = range(10)
        random.shuffle(self.input)
        print 'Sorting unit test data: ', self.input
        self.correct = range(10)

        self.output = mergeSort(self.input)
        print 'Result: ', self.output
        self.assertEqual(self.correct, self.output)

    def testMergeSortCase(self):
        self._testSortingCase(mergeSort)


if __name__ == '__main__':
    unittest.main()
