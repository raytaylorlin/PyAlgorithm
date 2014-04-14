#!/usr/bin/python
# -*- coding: utf-8 -*-


def mergeSort(data):
    """对给定的数组进行归并排序
    Args:
        data: 要排序的数组
    Returns:
        归并排序后的数组
    """

    def merge(left, right):
        """将两个有序数组合并为一个有序数组
        Args:
            left: 左边的有序数组
            right: 右边的有序数组
        Returns:
            合并完成的有序数组
        """

        result = []
        i, j = 0, 0
        # 合并完的数组的长度肯定是两个分数组的长度之和
        for k in range(len(left) + len(right)):
            # 两个下标均在两个数组范围之内，则取小的填入结果数组
            if i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            # 最后可能其中一个数组还有剩余的部分，将其剩余部分依次填入结果数组
            else:
                result.append(left[i] if i < len(left) else right[j])
                i += 1
                j += 1

        return result

    # 分别归并排序左半部分和右半部分，再合并
    if len(data) > 1:
        left = mergeSort(data[:len(data) / 2])
        right = mergeSort(data[len(data) / 2:])
        return merge(left, right)
    # 递归中止条件：数组只有1个元素
    else:
        return data

if __name__ == '__main__':
    with open('IntegerArray.txt') as file:
        data = map(int, file.readlines())
        result = mergeSort(data)
        with open('result.txt', 'w') as output:
            for num in result:
                output.write(str(num) + '\n')
