#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


def chooseFirstPivotIndex(left, right):
    """选择最左边的元素索引"""
    return left


def chooseLastPivotIndex(left, right):
    """选择最右边的元素索引"""
    return right


def chooseMedianOfThreePivotIndex(data, left, right):
    """选择左边元素，右边元素和中间元素三者的中位数索引"""
    a, l, r, m = data, left, right, (right + left) / 2
    if (a[r] < a[l] and a[l] < a[m]) or (a[m] < a[l] and a[l] < a[r]):
        return l
    elif (a[l] < a[r] and a[r] < a[m]) or (a[m] < a[r] and a[r] < a[l]):
        return r
    else:
        return m


def chooseRandomPivotIndex(left, right):
    """随机选择索引"""
    return random.choice(range(left, right + 1))


def _quickSort(data, left, right):
    """
    对给定的数组和给定范围进行快速排序
    Args:
        data: 要排序的数组
        left: 数组的左边界索引
        right: 数组的右边界索引
    Return:
        data: 排序完的数组
    """

    def partition(data, left, right):
        """
        围绕基准数分割指定左右边界的数组
        最后data[left:right]会呈现[<p, p, >p]的形式
        """

        # 选择基准
        # pivotIndex = chooseFirstPivotIndex(left, right)
        # pivotIndex = chooseLastPivotIndex(left, right)
        # pivotIndex = chooseMedianOfThreePivotIndex(data, left, right)
        pivotIndex = chooseRandomPivotIndex(left, right)

        pivot = data[pivotIndex]
        # 预处理：将基准放到数组第一个位置
        data[left], data[pivotIndex] = data[pivotIndex], data[left]

        i, j = left + 1, left + 1
        while j <= right:
            # 发现比基准小的元素，则将其交换到前面的位置
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
            j += 1
        # 记住基准数一直都位于左边界，最后要把它放到合适的中间位置
        pivotLastIndex = i - 1
        data[left], data[pivotLastIndex] = data[pivotLastIndex], data[left]
        return pivotLastIndex

    # 递归中止条件：数组只有1个元素
    if right - left <= 0:
        return 0

    pivotLastIndex = partition(data, left, right)
    _quickSort(data, left, pivotLastIndex - 1)
    _quickSort(data, pivotLastIndex + 1, right)
    return data


def quickSort(data):
    # 因为快速排序所有操作均在原地进行，所以此处复制一份列表，避免破坏原数组
    return _quickSort(data[:], 0, len(data) - 1)
