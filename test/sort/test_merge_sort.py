#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
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
            with open(inputFile) as file:
                self.input = file.read()
            with open(answerFile) as file:
                self.correct = file.read()
            self.input = map(int, self.input.split('\n'))
            self.output = mergeSort(self.input)
            self.correct = map(int, self.correct.split('\n'))
            self.assertEqual(self.correct, self.output)


if __name__ == '__main__':
    unittest.main()