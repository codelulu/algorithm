# -*- coding: utf-8 -*-

from sys import argv


MODE_COMPARING_SORT = 1
MODE_LINEAR_TIME_SORT = 2


def print_help(mode = MODE_COMPARING_SORT):
    print
    if mode == MODE_COMPARING_SORT:
        print '%s [a1] [a2] [a3] ...' % argv[0]
    elif mode == MODE_LINEAR_TIME_SORT:
        print '%s [k] [a1] [a2] [a3] ...' % argv[0]
    print
    exit()

def get_input_number(mode = MODE_COMPARING_SORT):
    if mode == MODE_COMPARING_SORT:
        if len(argv) <= 1:
            print_help(mode)

        argv.pop(0)
        return map(lambda a: int(a), argv)
    elif mode == MODE_LINEAR_TIME_SORT:
        if len(argv) <= 2:
            print_help(mode)

        argv.pop(0)
        k = int(argv.pop(0))
        lst = map(lambda a: int(a), argv)
        for x in lst:
            if x < 0 or x > k:
                print 'number %d is invalid' % x
                exit(0)
        return k, lst
    else:
        return None
  
