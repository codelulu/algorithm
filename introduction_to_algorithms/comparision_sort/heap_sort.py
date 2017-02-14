#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *


########################################################
#
# HEAP-SORT
#（堆排序 - 升序）
# O(nlgn)
#
########################################################


def parent(i):
    return i / 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    heap_size = len(A)
    for i in range(len(A) / 2, -1, -1):
        max_heapify(A, i, heap_size)

def heap_sort(A):
    build_max_heap(A)

    heap_size = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)
        

number_list = get_input_number()
heap_sort(number_list)
print number_list
