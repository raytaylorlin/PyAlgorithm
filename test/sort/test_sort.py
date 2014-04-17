#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import unittest
import test.util as util


TEST_CASE_DIR = 'data'


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.cases = util.getCases(TEST_CASE_DIR)

    def getStandardData(self, dataFile):
        """读取文件内容，并将数据转换为标准形式
        Args:
            dataFile: 存放数据的文件（在排序测试中，文件应该是每行1个整数）
        Return:
            一个整数列表
        """
        with open(dataFile) as file:
            data = file.read()
        return self.__standardize(data)

    def __standardize(self, data):
        return list(map(int, data.split('\n')))
