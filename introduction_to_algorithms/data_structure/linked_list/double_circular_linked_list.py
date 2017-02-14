#!/usr/bin/python
# -*- coding: utf-8 -*-


class NODE:

    def __init__(self, key = None):
        self.prev = self.next = self
        self.key = key

    def __str__(self):
        if self.prev == self:
            return 'NIL'
        else:
            return str(self.key)


class DOUBLE_CIRCULAR_LINKED_LIST:

    def __init__(self):
        self.nil = NODE()

    def LIST_SEARCH(self, k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        return x

    def LIST_INSERT(self, x):
        n = NODE(x)
        n.next = self.nil.next
        n.next.prev = n
        n.prev = self.nil
        self.nil.next = n

    def LIST_DELETE(self, x):
        x.next.prev = x.prev
        x.prev.next = x.next

    def __str__(self):
        s = 'head(L)'
        next = self.nil.next
        while next != self.nil:
            s += ' -> %s' % next.key
            next = next.next
        s += ' -> NIL'

        return s

if __name__ == '__main__':
    L = DOUBLE_CIRCULAR_LINKED_LIST()
    print L
    for x in range(10):
        L.LIST_INSERT(x + 1)
        print L

    k = 6
    n = L.LIST_SEARCH(k)
    print 'LIST_SEARCH(%s) = %s' % (k, n)

    L.LIST_DELETE(n)
    print 'after LIST_DELETE(%s),' % k, L
