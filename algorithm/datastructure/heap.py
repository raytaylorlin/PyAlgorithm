#!/usr/bin/python
# -*- coding: utf-8 -*-


class Heap():

    def __init__(self, heap=[]):
        self._heap = heap

    def size(self):
        return len(self._heap)
