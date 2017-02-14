#!/usr/bin/python
# -*- coding: utf-8 -*-

class Queue:

    N = 5

    def __init__(self):
        self.Q = [None] * self.N
        self.head = self.tail = 0
        self.size = 0

    def ENQUEUE(self, x):
        if self.size == self.N:
            raise Exception('overflow')

        self.Q[self.tail] = x
        if self.tail == self.N - 1:
            self.tail = 0
        else:
            self.tail += 1

        self.size += 1

    def DEQUEUE(self):
        if self.size == 0:
            raise Exception('underflow')

        x = self.Q[self.head]
        if self.head == self.N - 1:
            self.head = 0
        else:
            self.head += 1

        self.size -= 1

        return x

    def __str__(self):
        return 'Q = %s, N = %d, head = %d, tail = %d, size = %d' % (str(self.Q), self.N, self.head, self.tail, self.size)

if __name__ == '__main__':
    Q = Queue()

    print Q
    Q.ENQUEUE(1)
    Q.ENQUEUE(2)
    print Q
    print 'Q.DEQUEUE = %s' % Q.DEQUEUE()
    print Q
    print 'Q.DEQUEUE = %s' % Q.DEQUEUE()
    print Q
    for x in range(Q.N):
        Q.ENQUEUE(x + 3)
        print Q
    for x in range(Q.N):
        print 'Q.DEQUEUE = %s' % Q.DEQUEUE()
        print Q
        



