
def reverseList(head):
    reversed_list = []
    for i in head[::-1]:
        reversed_list.append(i)
    return reversed_list
print(reverseList([1, 2, 3, 4, 5]))
reverseList([1, 2, 3, 4, 5])


"""
Leet code version:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        # head = tail
        # tail = temp
        # after = temp.next
        before = None

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before

"""