"""
Day 23: BST Level-Order Traversal

https://www.hackerrank.com/challenges/30-binary-trees
"""
import unittest
import contextlib
import sys
from io import StringIO
from unittest.mock import patch


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        if root is None:
            return

        q = [root]
        while len(q) > 0:
            node = q.pop(0)

            print(node.data, end=' ')
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)

    myTree.levelOrder(root)


class TestLevelOrderTraversal(unittest.TestCase):
    def test_level_order(self):
        my_tree = Solution()
        root = None
        for item in [3, 5, 4, 7, 2, 1]:
            root = my_tree.insert(root, item)

        output = StringIO()
        with contextlib.redirect_stdout(output):
            my_tree.levelOrder(root)

        answer = output.getvalue().strip()

        self.assertEqual(
            "3 2 5 1 4 7",
            answer)
