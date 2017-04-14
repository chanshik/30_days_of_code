import unittest


class Node(object):
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution(object):
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

    def getHeight(self, root):
        if root is None:
            return 0

        max_height = 0
        stk = [(root, 0)]

        while len(stk) > 0:
            node, node_height = stk.pop(-1)
            if max_height < node_height:
                max_height = node_height

            if node.left is not None:
                stk.append((node.left, node_height + 1))
            if node.right is not None:
                stk.append((node.right, node_height + 1))

        return max_height


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)

    height = myTree.getHeight(root)

    print(height)


class TestSolution(unittest.TestCase):
    def test_get_height(self):
        myTree = Solution()
        root = None
        inputs = [3, 5, 2, 1, 4, 6, 7]
        for i in inputs:
            root = myTree.insert(root, i)

        height = myTree.getHeight(root)

        self.assertEqual(
            3,
            height
        )
