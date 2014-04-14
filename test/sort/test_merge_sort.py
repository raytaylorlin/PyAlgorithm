#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from algorithm.sort.merge_sort import mergeSort
from test_sort import TestSorting

class TestMergeSort(TestSorting):
    def test_merge_sort(self):
        self.output = mergeSort(self.input)
        print self.output
        self.assertEqual(self.correct, self.output)

if __name__ == '__main__':
    unittest.main()