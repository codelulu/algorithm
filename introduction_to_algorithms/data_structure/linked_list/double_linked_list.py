#!/usr/bin/python
# -*- coding: utf-8 -*-


class NODE:

    def __init__(self, key = None):
        self.prev = self.next = None
        self.key = key

    def __str__(self):
        prev = ''
        if self.prev != None:
            prev = self.prev.key
        else:
            prev = 'NIL'

        next = ''
        if self.next != None:
            next = self.next.key
        else:
            next = 'NIL'

        return '[ prev = %s, key = %s, next = %s ]' % (prev, self.key, next)


class DOUBLE_LINKED_LIST:

    def __init__(self):
        self.head = None

    def LIST_SEARCH(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

    def LIST_INSERT(self, x):
        n = NODE(x)
        n.next = self.head
        n.prev = None
        if self.head != None:
            self.head.prev = n
        self.head = n

    def LIST_DELETE(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next != None:
            x.next.prev = x.prev

    def __str__(self):
        s = 'head(L)'
        next = self.head
        while next != None:
            s += ' -> %s' % next.key
            next = next.next
        s += ' -> NIL'

        return s

if __name__ == '__main__':
    L = DOUBLE_LINKED_LIST()
    print L
    for x in range(10):
        L.LIST_INSERT(x + 1)
        print L

    k = 6
    n = L.LIST_SEARCH(k)
    print 'LIST_SEARCH(%s) = %s' % (k, n)

    L.LIST_DELETE(n)
    print 'after LIST_DELETE(%s),' % k, L
