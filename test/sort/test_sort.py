#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.input = range(10)
        random.shuffle(self.input)
        print 'Sorting unit test data: ', self.input
        self.correct = range(10)
