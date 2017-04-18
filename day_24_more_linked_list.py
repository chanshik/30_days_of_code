"""
Day 24: More Linked Lists 

https://www.hackerrank.com/challenges/30-linked-list-deletion
"""
import unittest
import contextlib
from io import StringIO


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p

        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        node = head
        while node is not None:
            if node.next is None:
                break
            else:
                if node.data == node.next.data:
                    node.next = node.next.next
                else:
                    node = node.next

        return head


if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    head = mylist.removeDuplicates(head)
    mylist.display(head)


class TestLinkedList(unittest.TestCase):
    def test_remove_duplicates(self):
        mylist = Solution()
        head = None

        for item in [1, 2, 2, 3, 3, 4]:
            head = mylist.insert(head, item)

        head = mylist.removeDuplicates(head)

        out = StringIO()
        with contextlib.redirect_stdout(out):
            mylist.display(head)

        self.assertEqual(
            "1 2 3 4",
            out.getvalue().strip()
        )
