#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest
import difflib
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

            diff = difflib.context_diff(
                map(str, self.correct), map(str, self.output),
                fromfile='answer', tofile='result', n=1)
            diffResult = '\n'.join(diff)
            print diffResult
            self.assertTrue(len(diffResult) == 0, 'Wrong answer!')
