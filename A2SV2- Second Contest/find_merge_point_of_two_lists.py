# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    set1 = set()
    curr_head = head1
    while curr_head:
        set1.add(curr_head)
        curr_head = curr_head.next
    curr_head = head2
    while curr_head:
        if curr_head in set1:
            return curr_head.data
        curr_head = curr_head.next
