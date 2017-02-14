#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(self):
        self.S = []

    def top(self):
        return len(self.S)

    def STACK_EMPTY(self):
        if self.top() == 0:
            return True
        else:
            return False

    def PUSH(self, x):
        self.S.append(x)

    def POP(self):
        if self.STACK_EMPTY():
            raise Exception('underflow')
        return self.S.pop(self.top() - 1)

    def __str__(self):
        return str(self.S)


if __name__ == '__main__':
    S = Stack()

    print 'S = %s' % S
    print 'S.STACK_EMPTY = %s' % S.STACK_EMPTY()
    S.PUSH(1.2)
    S.PUSH(45)
    print 'S = %s' % S
    print 'S.POP = %s' % S.POP()
    print 'S.POP = %s' % S.POP()

