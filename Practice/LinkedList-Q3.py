"""Original List: 12 -> 95 -> 140 -> 110-> 40
new number = 100
new list: 12 -> 95 -> 100 -> 110 -> 40"""
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

def replace_max(list):
    max_val = list.data
    temp = list
    curr = list.next
    while curr is not None:
        if curr.data > max_val:
            max_val = curr.data
            temp = curr
        curr = curr.next
    temp.data = 100
    return list

list = Node(12)
list.next = Node(95)
list.next.next = Node(140)
list.next.next.next = Node(1100)
list.next.next.next.next = Node(40)
list.next.next.next.next.next = Node(500)

new = replace_max(list)
while new is not None:
    print(new.data, end="->")
    new = new.next