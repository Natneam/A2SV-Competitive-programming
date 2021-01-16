# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    curr_head = head
    hash_set = set()
    while curr_head:
        if curr_head in hash_set:
            return 1
        hash_set.add(curr_head)
        curr_head = curr_head.next
    return 0
        
        