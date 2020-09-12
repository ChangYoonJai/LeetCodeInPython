# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Runtime: 68 ms, faster than 90.84% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.8 MB, less than 58.15% of Python3 online submissions for Add Two Numbers.
        '''
        root = s = ListNode()
        while(l1 is not None or l2 is not None):
            s.val += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if s.val < 10:
                s.next = ListNode()
            else:
                s.val -= 10
                s.next = ListNode(1)
            prev_s = s
            s = s.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if s.val == 0:
            prev_s.next = None
        return root

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
def print_node(node:ListNode):
    print(node, end=' ')
    if node.next is None:
        print()
        return
    print('->', end=' ')
    print_node(node.next)

def solve_sample(l1, l2):
    print_node(l1)
    print_node(l2)
    sol = Solution().addTwoNumbers(l1, l2)
    print_node(sol)
    print()

solve_sample(
    ListNode(2, ListNode(4, ListNode(3))),
    ListNode(5, ListNode(6, ListNode(4)))
)

solve_sample(
    ListNode(1),
    ListNode(9, ListNode(9))
)

solve_sample(
    ListNode(9, ListNode(9)),
    ListNode(1)
)

solve_sample(
    ListNode(1, ListNode(8)),
    ListNode(0)
)







