#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import unittest
import difflib
import logging

CASE_FILE_SUFFIX = '.in'
ANSWER_FILE_SUFFIX = '.ans'


class PyAlgorithmTestCase(unittest.TestCase):

    """公共的TestCase父类"""

    def setUp(self, logger):
        logger.info('%s', self.shortDescription())

    def _testFileCase(self, algoFunc, standardizeInput, standaradizeAnswer):
        for inputFile, answerFile in self.cases:
            print '*' * 20
            print 'Test case:', inputFile
            self.input = readFileAndStandardize(
                inputFile, standardizeInput)
            self.correct = readFileAndStandardize(
                answerFile, standaradizeAnswer)
            self.output = algoFunc(**self.input)

            diffResult = compareAnswerOutput(self.correct, self.output)
            print diffResult
            self.assertTrue(len(diffResult) == 0, 'Wrong answer!')


def getInputAnswerCases(directory, algoName):
    """获取测试输入和答案文件列表
    Args:
        directory: 要扫描测试文件的目录
        algoName: 算法的名称，扫描的文件将以该名称为前缀
    Return:
        测试输入和答案文件名元组列表，列表项格式为(input, answer)
    """
    fileMap = {}
    inputAnswerCaseList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(CASE_FILE_SUFFIX) and file.startswith(algoName):
                filename = file.replace(CASE_FILE_SUFFIX, '')
                inputFile = directory + '/' + filename + CASE_FILE_SUFFIX
                answerFile = directory + '/' + filename + ANSWER_FILE_SUFFIX
                inputAnswerCaseList.append((inputFile, answerFile))
    return inputAnswerCaseList


def readFileAndStandardize(filename, standardizeFunc):
    """读取数据文件，并转换成标准格式
    Args:
        filename: 要读取的文件名
        standardizeFunc: 标准化函数，输入为文件完整内容，输出为标准化后的对象（如list、map等）
    """
    with open(filename) as file:
        data = file.read()
        return standardizeFunc(data)


def compareAnswerOutput(answer, output):
    """比较答案和输出的差异
    Args:
        answer: 答案对象
        output: 输出对象
    Return:
        两者比较的差异
    """
    diff = difflib.context_diff(
        map(str, answer), map(str, output),
        fromfile='answer', tofile='result', n=1)
    diffResult = '\n'.join(diff)
    return diffResult


def getLogger(name):
    """获取一个日志记录器
    Args:
        name: 日志记录器的名称
    """
    logging.basicConfig(
        format='\n[%(levelname)s] %(message)s', level=logging.DEBUG)
    return logging.getLogger(name)
