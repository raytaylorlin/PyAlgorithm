#!/usr/bin/python
# -*- coding: utf-8 -*-


from algorithm.datastructure.heap import Heap


def heapSort(data):
    """对给定的数组进行堆排序
    Args:
        data: 要排序的数组
    Returns:
        堆排序后的数组
    """

    result = []
    heap = Heap(data)
    # 堆的根元素总是最小的，所以只要执行len(data)次提取最值（包括调整堆）即可
    for i in xrange(len(data)):
        result.append(heap.extract())
    return result
