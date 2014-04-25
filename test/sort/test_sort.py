#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest
import test.util as util

logger = util.getLogger('test.sort')


class TestSorting(util.PyAlgorithmTestCase):
    TEST_CASE_FORMAT = '''
    Input: list = %s
    Result: %s
    '''

    def setUp(self):
        super(TestSorting, self).setUp(logger)
        self.cases = util.getInputAnswerCases('data', 'sort')

    def _testBaseCase(self, sortFunc):
        self.input = range(10)
        random.shuffle(self.input)
        self.correct = range(10)
        self.output = sortFunc(self.input)

        logger.debug(TestSorting.TEST_CASE_FORMAT, self.input, self.output)
        self.assertEqual(self.correct, self.output)

    def _testSortingCase(self, sortFunc):
        def standardizeInput(content):
            return {'data': list(map(int, content.split('\n')))}

        def standardizeAnswer(content):
            return list(map(int, content.split('\n')))

        self._testFileCase(sortFunc, standardizeInput, standardizeAnswer)
