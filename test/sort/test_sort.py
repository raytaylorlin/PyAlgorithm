#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest
import test.util as util


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.cases = util.getInputAnswerCases('data', 'sort')

    def _testSortingCase(self, sortFunc):
        def standardize(content):
            return list(map(int, content.split('\n')))

        for inputFile, answerFile in self.cases:
            print '*' * 20
            print 'Test case: ' + inputFile
            self.input = util.readFileAndStandardize(inputFile, standardize)
            self.correct = util.readFileAndStandardize(answerFile, standardize)
            self.output = sortFunc(self.input)

            diffResult = util.compareAnswerOutput(self.correct, self.output)
            print diffResult
            self.assertTrue(len(diffResult) == 0, 'Wrong answer!')
