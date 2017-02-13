#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# QUICK-SORT
#（快速排序 - 升序）
# 最差，O(n^2)，平均 O(nlgn)
#
# 快速执行：先按左小右大的方式拆分数组为左右两组，再对每组进行排序。
#
########################################################


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort2(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort2(A, p, q - 1)
        p = q + 1

def quick_sort(A):
    quick_sort2(A, 0, len(A) - 1)


number_list = get_input_number()
quick_sort(number_list)
print number_list
