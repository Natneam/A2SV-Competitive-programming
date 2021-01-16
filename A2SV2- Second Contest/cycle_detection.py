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
    max_list_size = 1000
    index = 1
    curr_head = head
    while curr_head:
        if index > max_list_size:
            return 1
        curr_head = curr_head.next
        index += 1
    return 0