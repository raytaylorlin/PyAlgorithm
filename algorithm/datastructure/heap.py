#!/usr/bin/python
# -*- coding: utf-8 -*-


class Heap():

    def __init__(self, heap=[]):
        self._heap = heap

    def size(self):
        """获取堆的大小"""
        return len(self._heap)

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
