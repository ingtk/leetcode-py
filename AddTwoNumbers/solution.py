class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = int(self.to_num(l1))
        n2 = int(self.to_num(l2))
        n3 = str(n1 + n2)
        answer = None
        cur = None
        for i in range(len(n3)):
            k = len(3) - (i + 1)
            if answer is None:
                answer = ListNode(n3[k])
                cur = answer
            else:
                cur.next = ListNode(n3[k])
                cur = cur.next
        return answer

    def to_num(self, l: ListNode) -> str:
        if l.next is None:
            return str(l.val)
        return self.to_num(l.next) + str(l.val)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1, l2))
