class Solution(object):
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, item):
        self.stack.append(item)

    def popCharacter(self):
        item = self.stack[-1]
        self.stack.__delitem__(-1)

        return item

    def enqueueCharacter(self, item):
        self.queue.append(item)

    def dequeueCharacter(self):
        item = self.queue[0]
        self.queue.__delitem__(0)

        return item


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
