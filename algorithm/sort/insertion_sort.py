#!/usr/bin/python
# -*- coding: utf-8 -*-


def insertionSort(data):
    """对给定的数组进行插入排序
    Args:
        data: 要排序的数组
    Returns:
        插入排序后的数组
    """

    # 初始化结果为第一个数
    result = [data[0]]
    # 从第二个数开始，从后往前找应该插入的位置
    for num in data[1:]:
        index = len(result) - 1
        while index >= 0 and result[index] > num:
            index -= 1
        else:
            result.insert(index + 1, num)
    return result
