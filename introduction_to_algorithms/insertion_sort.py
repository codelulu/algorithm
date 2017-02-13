#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# INSERTION-SORT
#（插入排序 - 升序）
# O(n^2)
#
# 将下一个待排序的元素，按升序将其放入到已排序的数组中。
#
########################################################


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

number_list = get_input_number()

insertion_sort(number_list)
print number_list
