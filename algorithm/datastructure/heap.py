#!/usr/bin/python
# -*- coding: utf-8 -*-


class Heap():

    def __init__(self, heap=[]):
        """Heap类构造方法，对给定的数组建立最小堆
        Args:
            [heap]: 要建立最小堆的初始化数组，若为空则建立一个空堆
        """
        self._heap = heap
        for i in reversed(xrange(len(self._heap) / 2)):
            self._bubbleDown(i)

    def size(self):
        """获取堆的大小"""
        return len(self._heap)

    def insert(self, data):
        """在堆中插入一个元素"""
        self._heap.append(data)
        self._bubbleUp(len(self._heap) - 1)

    def _bubbleUp(self, i):
        """对指定下标的元素向上进行调整，以维护堆的性质"""
        parent = (i - 1) / 2
        while parent >= 0:
            if self._heap[i] < self._heap[parent]:
                self._heap[i], self._heap[parent] = \
                    self._heap[parent], self._heap[i]
                i = parent
                parent = (i - 1) / 2
            else:
                break

    def _bubbleDown(self, i):
        """对指定下标的元素向下进行调整，以维护堆的性质"""

        smallest = i
        # 注意此处左右孩子的算法和教科书不太一样，因为实际数组下标是从0开始
        left, right = 2 * i + 1, 2 * i + 2
        # 找出i，left，right三个元素最小的一个
        if left < self.size() and self._heap[left] < self._heap[smallest]:
            smallest = left
        if right < self.size() and self._heap[right] < self._heap[smallest]:
            smallest = right
        if smallest != i:
            # 交换位置，并向继续向下冒泡调整
            self._heap[i], self._heap[smallest] = \
                self._heap[smallest], self._heap[i]
            self._bubbleDown(smallest)
