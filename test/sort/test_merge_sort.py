#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import difflib
from algorithm.sort.merge_sort import mergeSort
from test_sort import *


class TestMergeSort(TestSorting):

    def testMergeSort(self):
        self.input = range(10)
        random.shuffle(self.input)
        print 'Sorting unit test data: ', self.input
        self.correct = range(10)

        self.output = mergeSort(self.input)
        print 'Result: ', self.output
        self.assertEqual(self.correct, self.output)

    def testMergeSortCase(self):
        for inputFile, answerFile in self.cases:
            print '*' * 20
            print 'Test case: ' + inputFile
            self.input = self.getStandardData(inputFile)
            self.correct = self.getStandardData(answerFile)
            self.output = mergeSort(self.input)

            diff = difflib.context_diff(
                map(str, self.correct), map(str, self.output),
                fromfile='answer', tofile='result', n=1)
            diffResult = '\n'.join(diff)
            print diffResult
            self.assertTrue(len(diffResult) == 0, 'Wrong answer!')


if __name__ == '__main__':
    unittest.main()
