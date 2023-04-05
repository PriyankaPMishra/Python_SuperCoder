# Node definition
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# Single Linked List definition
class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def atBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def atEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last_ele = self.headval
        while (last_ele.nextval):
            last_ele = last_ele.nextval
        last_ele.nextval = NewNode

    def inBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent.")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def deleteAtStart(self):
        if self.headval is None:
            print("list has no element")
            return
        else:
            temp = self.headval
            self.headval = self.headval.nextval
            temp.next = None

    def deleteAtEnd(self):
        if self.headval is None:
            print("List has no element")
            return
        else:
            n = self.headval
            while n.nextval.nextval is not None:
                n = n.nextval
            n.nextval = None

    def deleteByValue(self, x):
        if self.headval is None:
            print("list has no element")
            return
        # dleting first node
        if self.headval.dataval == x:
            self.headval = self.headval.nextval
            return

        n = self.headval
        while n.nextval is not None:
            if n.nextval.dataval == x:
                break
            n = n.nextval

        if n.nextval is None:
            print("Item not found in list")
        else:
            n.nextval = n.nextval.nextval

    def getCount(self):
        if self.headval is None:
            return 0
        n = self.headval
        count = 1
        while n is not None:
            count += 1
            n = n.nextval
        return count

    def insertAtIndex(self, index, data):
        if index == 1:
            NewNode = Node(data)
            NewNode.nextval = self.headval
            self.headval = NewNode
        i = 1
        n = self.headval
        while i < index-1 and n is not None:
            n = n.nextval
            i += 1
        if n is None:
            print("Index out of Bound")
        else:
            NewNode = Node(data)
            NewNode.nextval = n.nextval
            n.nextval = NewNode

    def reverse(self):
        prev = None
        curr = self.headval
        while (curr is not None):
            next = curr.nextval
            curr.nextval = prev
            prev = curr
            curr = next
        self.headval = prev


list = SLinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
e4 = Node("Thursday")
# creating links
list.headval.nextval = e2
e2.nextval = e3
# list.listprint()
e3.nextval = e4
print("Linked List elements:")
list.listprint()
print("---")
print("Insertion at Beginning:")
list.atBeginning("Sunday")
list.listprint()
print("---")
print("Insertion at End:")
list.atEnd("Friday")
list.listprint()
print("---")
print("Deleting at Start: ")
list.deleteAtStart()
list.listprint()
print("---")
print("Deleting at End: ")
list.deleteAtEnd()
list.listprint()
print("---")
print("Deleting by value:")
list.deleteByValue("Tuesday")
list.listprint()
print("---")
print("Count:", list.getCount())
print("---")
list.insertAtIndex(2, "NewDay")
list.listprint()
print("---")
list.reverse()
list.listprint()
print("---")
