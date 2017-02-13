#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *

MIN = -9999999

########################################################
#
# PRIORITY-QUEUE
#（优先级队列 - 最大堆）
# O(nlgn)
#
########################################################

class Node:

    def __init__(self, element, key = MIN):
        self.element = element
        self.key = key

    def __cmp__(self, y):
        if isinstance(y, Node):
            return self.key - y.key
        return self.key - y

    def __str__(self):
        return '[ element = %s, key = %d ]' % (self.element, self.key)

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


def heap_maximum(A):
    if len(A) == 0:
        return None

    return A[0]

def heap_extract_max(A):
    heap_size = len(A)
    if heap_size < 1:
        raise Exception('heap underflow')

    max = A[0]
    A[0] = A[heap_size - 1]
    heap_size -= 1
    A.pop(heap_size)
    max_heapify(A, 0, heap_size)

    return max

def heap_increase_key(A, i, key):
    if A[i] > key:
        raise Exception('new key is smaller than current key')

    A[i].key = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
        
def max_heap_insert(A, element, key):
    heap_size = len(A)
    A.append(Node(element))
    heap_increase_key(A, heap_size, key)



A = []

max_heap_insert(A, '元素1', 4)
max_heap_insert(A, '元素2', 7)
max_heap_insert(A, '元素3', 5)
max_heap_insert(A, '元素4', 5)
max_heap_insert(A, '元素6', 5)

for x in A:
    print x

print '-- max maximum', heap_maximum(A)

print '-- after heap_extract_max'
print '-- extract_max =', heap_extract_max(A)

for x in A:
    print x

