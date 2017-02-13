#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv


def print_help():
    print
    print '%s [x] [a0] [a1] [a2] [a3] ...' % argv[0]
    print
    exit()

def get_input_number():
    if len(argv) <= 2:
        print_help()

    argv.pop(0)

    return map(lambda a: float(a), argv)
  

########################################################
#
# Horner's Rule
#（霍纳规则）
#
########################################################


def horner_rule(A):
    n = len(A) - 2
    x = A[0]
    y = .0

    for i in range(n, -1, -1):
        y = A[1 + i] + x * y

    print 'P(%g) = %g' % (x, y)


number_list = get_input_number()
horner_rule(number_list)
