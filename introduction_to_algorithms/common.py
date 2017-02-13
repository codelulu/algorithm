# -*- coding: utf-8 -*-

from sys import argv


def print_help():
    print
    print '%s [a1] [a2] [a3] ...' % argv[0]
    print
    exit()

def get_input_number():
    if len(argv) <= 1:
        print_help()

    argv.pop(0)

    return map(lambda a: int(a), argv)
  
