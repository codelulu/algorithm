#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack:

    N = 5

    def __init__(self):
        self.S = [None] * self.N
        self.top = 0

    def STACK_EMPTY(self):
        if self.top == 0:
            return True
        else:
            return False

    def PUSH(self, x):
        if self.top == self.N:
            raise Exception('overflow')

        self.S[self.top] = x
        self.top += 1

    def POP(self):
        if self.STACK_EMPTY():
            raise Exception('underflow')

        x = self.S[self.top - 1]
        self.top -= 1
        return x

    def __str__(self):
        return 'S = %s, top = %d, N = %d' % (str(self.S), self.top, self.N)


if __name__ == '__main__':
    S = Stack()

    print '%s' % S
    print 'S.STACK_EMPTY = %s' % S.STACK_EMPTY()
    S.PUSH(1.2)
    S.PUSH(45)
    print '%s' % S
    print 'S.POP = %s' % S.POP()
    print 'S.POP = %s' % S.POP()

