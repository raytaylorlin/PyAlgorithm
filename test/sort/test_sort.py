#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest
from test.util import getCases


TEST_CASE_DIR = 'data'

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.cases = getCases(TEST_CASE_DIR)
        # print self.cases
