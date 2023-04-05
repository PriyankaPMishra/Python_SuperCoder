"""Write a python function which accepts two linked lists containing integer data and
an integer, n and merges the two linked lists, such that list2 is merged with list1 after n number of nodes.
Assume that value of n will always be less than or equal to the number of nodes in list1.

input:
list1 1->2->4->3->5
list2 9->8->11
n-2
output: 1->2->9->8->11->4->3->5
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_lists(list1, list2, n):
    if n == 0:
        list2_tail = list2
        while list2_tail.next is not None:
            list2_tail = list2_tail.next
        list2_tail.next = list1
        return list2
    else:
        curr1 = list1
        for i in range(n-1):
            curr1 = curr1.next
        curr2 = list2
        while curr2.next is not None:
            curr2 = curr2.next
        curr2.next = curr1.next
        curr1.next = list2
        return list1

#LIST1
list1 = Node(1)
e2 = Node(2)
e3 = Node(4)
e4 = Node(3)
e5 = Node(5)
list1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

#LIST 2 - CAN ALSO BE DECLARED LIKE THIS
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)

merged = merge_lists(list1, list2, 2)

while merged is not None:
    print(merged.data, end="->")
    merged=merged.next