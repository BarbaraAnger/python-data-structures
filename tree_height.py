#!/bin/python3
from types.binary_tree import BinarySearchTree


def height(root):
    if root is None or root.info is None:
        return -1
    else:
        rightDepth = height(root.left)
        leftDepth = height(root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1


def authentication(n, data):
    nodeList = []
    if data:
        for nodeData in n.split():
            if 1 <= int(nodeData) <= 20:
                nodeList.append(nodeData)
            else:
                print("not a allowed value")
                return -1
    else:
        if 1 <= n <= 20:
            return n
    return nodeList


tree = BinarySearchTree()
print("type the number of nodes in the tree")
t = authentication(int(input()), False)

print("data for the nodes")
arr = authentication(input(), True)

for i in range(arr.__len__()):
    tree.create(arr[i])

print(height(tree.root))
