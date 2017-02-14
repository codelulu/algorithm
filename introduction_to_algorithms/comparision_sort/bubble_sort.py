#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# BUBBLE-SORT
#（冒泡排序 - 升序）
# O(n^2)
#
# 从待排序的元素中，选择最小的，放入到已排序的数组的最后。
#
########################################################


def bubble_sort(A):
    n = len(A)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j - 1], A[j] = A[j], A[j - 1]


number_list = get_input_number()
bubble_sort(number_list)
print number_list
