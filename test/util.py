#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

CASE_FILE_SUFFIX = '.in'
ANSWER_FILE_SUFFIX = '.ans'


def getCases(directory, algoName):
    fileMap = {}
    caseAnswerList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(CASE_FILE_SUFFIX) and file.startswith(algoName):
                filename = file.replace(CASE_FILE_SUFFIX, '')
                inputFile = directory + '/' + filename + CASE_FILE_SUFFIX
                answerFile = directory + '/' + filename + ANSWER_FILE_SUFFIX
                caseAnswerList.append((inputFile, answerFile))
    return caseAnswerList


def readFileAndStandardize(filename, standardizeFunc):
    with open(filename) as file:
        data = file.read()
        return standardizeFunc(data)
