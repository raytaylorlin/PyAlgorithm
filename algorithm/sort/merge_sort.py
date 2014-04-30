#!/usr/bin/python
# -*- coding: utf-8 -*-


def mergeSort(data):
    """对给定的数组进行归并排序
    Args:
        data: 要排序的数组
    Returns:
        归并排序后的数组
    """

    # 分别归并排序左半部分和右半部分，再合并
    if len(data) > 1:
        leftList = mergeSort(data[:len(data) / 2])
        rightList = mergeSort(data[len(data) / 2:])
        return merge(leftList, rightList)
    # 递归中止条件：数组只有1个元素
    else:
        return data


def merge(leftList, rightList):
    """将两个有序数组合并为一个有序数组
    Args:
        leftList: 左边的有序数组
        rightList: 右边的有序数组
    Returns:
        合并完成的有序数组
    """

    result = []
    i, j = 0, 0
    # 合并完的数组的长度肯定是两个子数组的长度之和
    for k in range(len(leftList) + len(rightList)):
        # 两个下标均在两个数组范围之内，则取小的填入结果数组
        if i < len(leftList) and j < len(rightList):
            if leftList[i] <= rightList[j]:
                result.append(leftList[i])
                i += 1
            else:
                result.append(rightList[j])
                j += 1
        # 最后可能其中一个数组还有剩余的部分，将其剩余部分依次填入结果数组
        else:
            result.append(leftList[i] if i < len(leftList) else rightList[j])
            i += 1
            j += 1

    return result
