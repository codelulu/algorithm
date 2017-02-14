#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class NODE:

    def __init__(self, key = None):
        self.left = self.right = self.p = None
        self.key = key

    def __str__(self):
        return '[ key = %s ]' % str(self.key)


class BINARY_SEARCH_TREE:

    def __init__(self):
        self.root = None

    def INORDER_TREE_WALK(self, x = None):
        if x != None:
            self.INORDER_TREE_WALK(x.left)
            print x.key,
            self.INORDER_TREE_WALK(x.right)


    def TREE_SEARCH(self, x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.TREE_SEARCH(x.left, k)
        else:
            return self.TREE_SEARCH(x.right, k)

    def ITERATIVE_TREE_SEARCH(self, x, k):
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right

        return x

    def TREE_MINIMUM(self, x):
        while x != None and x.left != None:
            x = x.left
        return x

    def TREE_MAXIMUM(self, x):
        while x != None and x.right != None:
            x = x.right
        return x

    def TREE_SUCCESSOR(self, x):
        if x == None:
            return None
        if x.right != None:
            return self.TREE_MINIMUM(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def TREE_INSERT(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def TREE_DELETE(self, z):
        pass
        

if __name__ == '__main__':
    t = BINARY_SEARCH_TREE()
    node_list = {}

    c = 0
    while True:
        v = random.randint(0, 100)
        if len(node_list) == 10:
            break

        found = False
        for x in node_list:
            if node_list[x].key == v:
                found = True
                break
        if found:
            continue

        node_list[c] = NODE(v)
        c += 1

    for x in node_list:
        print 'TREE_INSERT(%s)' % node_list[x]
        t.TREE_INSERT(node_list[x])

    print 'INORDER_TREE_WALK =',
    t.INORDER_TREE_WALK(t.root)
    print
    print 'ROOT =', t.root
    k = node_list[6]
    print 'TREE_SEARCH(%s) = %s' % (k, t.TREE_SEARCH(t.root, k))
    print 'ITERATIVE_TREE_SEARCH(%s) = %s' % (k, t.ITERATIVE_TREE_SEARCH(t.root, k))
    print 'TREE_MINIMUM() = %s' % (t.TREE_MINIMUM(t.root))
    print 'TREE_MAXIMUM() = %s' % (t.TREE_MAXIMUM(t.root))
    print 'TREE_SUCCESSOR() = %s' % (t.TREE_SUCCESSOR(t.root))
