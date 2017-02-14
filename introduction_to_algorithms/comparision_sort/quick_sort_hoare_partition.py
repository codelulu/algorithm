#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *
import random


########################################################
#
# QUICK-SORT
#（快速排序 - 升序）
# 最差，O(n^2)，平均 O(nlgn)
#
# 快速执行：先按左小右大的方式拆分数组为左右两组，再对每组进行排序。
# 随机分区
#
########################################################


def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while A[j] > x:
            j -= 1

        i += 1
        while A[i] < x:
            i += 1

        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

def quick_sort2(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        quick_sort2(A, p, q - 1)
        quick_sort2(A, q + 1, r)

def quick_sort(A):
    quick_sort2(A, 0, len(A) - 1)


number_list = get_input_number()
quick_sort(number_list)
print number_list
