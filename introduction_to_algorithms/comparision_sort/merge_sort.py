#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# MERGE-SORT
#（合并排序 - 升序）
# O(nlgn)
#
# 递归执行：排序左右数组，按升序重排两数组中的元素。
#
########################################################


# a >= b?
def le(a, b):
    if a is None:
        return False
    elif b is None:
        return True

    # 忽略a与b都为None的情形
    return a <= b

# p <= q < r
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in range(1, n1 + 1):
        L.append(A[p + i - 1])

    for j in range(1, n2 + 1):
        R.append(A[q + j])

    L.append(None)
    R.append(None)

    i = 0
    j = 0

    for k in range(p, r + 1):
        if le(L[i], R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort2(A, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort2(A, p, q)
        merge_sort2(A, q + 1, r)
        merge(A, p, q, r)

def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)


number_list = get_input_number()
merge_sort(number_list)
print number_list
