#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest
import test.util as util

logger = util.getLogger('test.sort')


class TestSorting(util.PyAlgorithmTestCase):

    def setUp(self):
        super(TestSorting, self).setUp(logger)
        self.cases = util.getInputAnswerCases('data', 'sort')

    def _testSortingCase(self, sortFunc):
        def standardizeInput(content):
            return {'data': list(map(int, content.split('\n')))}

        def standardizeAnswer(content):
            return list(map(int, content.split('\n')))

        self._testFileCase(sortFunc, standardizeInput, standardizeAnswer)
