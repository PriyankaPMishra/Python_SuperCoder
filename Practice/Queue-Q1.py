"""Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder.
Consider the range to be from 1 to 10 (both inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.
Example:
Input Queue: 13983, 10080, 7113, 2520, 2500 (front - rear)
Output Queue: 10080, 2520(front-rear)"""

class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front= 0

    def is_full(self):
        if (self.__rear == self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if (self.__front > self.__rear):
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue Full!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

def check_divisibility(numQ):
    size = numQ.get_max_size()
    solQ = Queue(size)
    while size>0:
        ele = numQ.dequeue() #
        print("Elements: ", ele)
        count=0
        # if all(ele%i == 0 for i in range(1, 11)):
        #     solQ.enqueue(ele)

        #same as above loop - alternate to all()
        for i in range(1, 11):
            if ele%i == 0:
                count+=1
        if count==10:
            solQ.enqueue(ele)

        size -= 1
    return solQ

numQ = Queue(5)
numQ.enqueue(13983)
numQ.enqueue(10080)
numQ.enqueue(7113)
numQ.enqueue(2520)
numQ.enqueue(2500)
check_divisibility(numQ).display()