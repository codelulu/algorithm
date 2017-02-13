#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# BUCKET-SORT
#（桶排序 - 升序）
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

def bucket_sort(A):
    n = len(A)

    B = [None] * len(number_list)
    for x in range(len(B)):
        B[x] = []

    for i in range(0, n):
        B[int(n * A[i])].append(A[i])

    for i in range(0, n):
        insertion_sort(B[i])

    C = []
    for x in range(0, n):
        for y in range(0, len(B[x])):
            C.append(B[x][y])
    return C
        
number_list = get_input_number(MODE_BUCKET_SORT)

B = bucket_sort(number_list)
for x in B:
    print '%g' % x,
print
