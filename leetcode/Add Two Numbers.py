"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""


#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        num1 = 0
        num2 = 0
        temp1 = l1
        temp2 = l2
        while temp1 != None:
            num1 += (temp1.val) * (10 ** i)
            num2 += (temp2.val) * (10 ** i)
            i += 1
            temp1 = temp1.next
            temp2 = temp2.next

        output = num1 + num2
        ele = []
        while output != 0:
            ele.append(output % 10)
            output = int(output / 10)

        output_l = ListNode()
        newnode = ListNode
        for i in ele:
            output_l.val = i
            output_l.next = newnode

        return output_l

output = 1000000000000000000000000000466
ele = []
while output != 0:
    ele.append(output % 10)
    print(output % 10)
    output = output // 10
    print(output)

print(ele)
