class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
            return head

        cur_node = head
        while cur_node.next is not None:
            cur_node = cur_node.next

        node = Node(data)
        cur_node.next = node

        return head

if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None

    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)

    mylist.display(head)
