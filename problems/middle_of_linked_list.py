# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
    """
    def middle_node(self, head: [ListNode]) -> [ListNode]:
        middle = head
        end = head
        while end and end.next:
            middle = middle.next
            end = end.next.next
        return middle


def main():
    check = Solution()
    lst = [1, 2, 3, 4, 5, 6]
    head = None
    for i in lst:
        head = ListNode(i, next=head)
    print(check.middle_node(head).val)


if __name__ == "__main__":
    main()
