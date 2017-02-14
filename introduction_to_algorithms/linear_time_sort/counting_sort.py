#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# COUNTING-SORT
#（计数排序 - 升序）
#
########################################################

def counting_sort(k, A, B):
    print A
    C = {}
    for i in range(k + 1):
        C[i] = 0

    for j in range(0, len(A)):
        C[A[j]] += 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

k, number_list = get_input_number(MODE_LINEAR_TIME_SORT)
B = [None] * len(number_list)
counting_sort(k, number_list, B)
print 'k = %d' % k
print B

