#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class NODE:

    def __init__(self, key = None):
        self.left = self.right = self.p = None
        self.key = key

    def __str__(self):
        S = lambda n: 'NIL' if n is None else str(n.key)

        return '%s[%s,%s]' % (self.key, S(self.left), S(self.right))


class BINARY_SEARCH_TREE:

    def __init__(self):
        self.root = None

    def INORDER_TREE_WALK(self, x = None, key_list = []):
        if x != None:
            self.INORDER_TREE_WALK(x.left, key_list)
            key_list.append(str(x))
            self.INORDER_TREE_WALK(x.right, key_list)
        return key_list

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
        z.left = z.right = None
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
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def TREE_DELETE(self, z):
        # y: the child to delete
        if z.left == None or z.right == None:
            y = z
        else:
            y = self.TREE_SUCCESSOR(z)

        # x: the child to keep
        if y.left != None:
            x = y.left
        else:
            x = y.right

        if x != None:
            x.p = y.p

        if y.p == None:
            self.root = x
        else:
            if y == y.p.left:
                y.p.left = x
            else:
                y.p.right = x

        if y != z:
            z.key = y.key

        return y
        

def show_tree(t):
    key_list = t.INORDER_TREE_WALK(t.root, [])
    print 'INORDER_TREE_WALK: { %s }' % ', '.join(key_list)
   
def add_node(node_list, t, v):
    node_list[v] = NODE(v)
    t.TREE_INSERT(node_list[v])
    
def test1(t):
    node_list = {}

    c = 0
    while True:
        v = random.randint(0, 100)
        if len(node_list) == 10:
            break

        found = False
        for x in node_list:
            if node_list[x] == v:
                found = True
                break
        if found:
            continue

        node_list[c] = v
        c += 1

    for x in node_list:
        t.TREE_INSERT(NODE(node_list[x]))

    show_tree(t)
    print 'ROOT =', t.root
    k = node_list[6]
    print 'TREE_SEARCH(%s) = %s' % (k, t.TREE_SEARCH(t.root, k))
    print 'ITERATIVE_TREE_SEARCH(%s) = %s' % (k, t.ITERATIVE_TREE_SEARCH(t.root, k))
    print 'TREE_MINIMUM() = %s' % (t.TREE_MINIMUM(t.root))
    print 'TREE_MAXIMUM() = %s' % (t.TREE_MAXIMUM(t.root))
    print 'TREE_SUCCESSOR(%s) = %s' % (t.root, t.TREE_SUCCESSOR(t.root))

    tree_node_number = len(node_list)
    for x in range(tree_node_number):
        print '-----------------------------  %s' % x
        node = t.TREE_SEARCH(t.root, node_list[x])

        node_key = node.key

        show_tree(t)
        old_key_list = t.INORDER_TREE_WALK(t.root, [])

        print 'DELETE(%s)' % node_key
        t.TREE_DELETE(node)

        key_list = t.INORDER_TREE_WALK(t.root, [])

        if len(key_list) != len(old_key_list) - 1:
            print '---- ERROR DELETE(%s)' % node_key
            show_tree(t)
            exit(0)
        
        print 'DELETE(%s) OK!' % node_key
        show_tree(t)

        node = NODE(node_key)
        print 'INSERT(%s) OK!' % node_key
        t.TREE_INSERT(node)
        show_tree(t)


def test2(t):
    node_list = {}
    add_node(node_list, t, 3)
    add_node(node_list, t, 1)
    add_node(node_list, t, 2)
    add_node(node_list, t, 0)
    add_node(node_list, t, 5)
    add_node(node_list, t, 4)
    add_node(node_list, t, 6)

    print '-----------------------'
    show_tree(t)
    print '-----------------------'
    n = 7
    print 'TREE_DELETE(%s)' % node_list[n]
    t.TREE_DELETE(node_list[n])
    show_tree(t)
   
if __name__ == '__main__':
    t = BINARY_SEARCH_TREE()
    test1(t)
