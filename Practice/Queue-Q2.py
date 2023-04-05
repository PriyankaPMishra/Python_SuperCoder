"""Queue- 2 7 9 4 6 5 10
Odd Queue- 7 9 5
Even Queue - 2 4 6 10"""

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

def check_even_odd(numQ):
    size = numQ.get_max_size()
    evenQ = Queue(size)
    oddQ = Queue(size)
    while size > 0:
        ele = numQ.dequeue()  #
        print("Elements: ", ele)
        if ele%2 == 0:
            evenQ.enqueue(ele)
        else:
            oddQ.enqueue(ele)
        size -= 1
    print("ODD Queue:")
    while not oddQ.is_empty():
        print(oddQ.dequeue())

    print("EVEN Queue:")
    while not evenQ.is_empty():
        print(evenQ.dequeue())

numQ = Queue(7)
numQ.enqueue(2)
numQ.enqueue(7)
numQ.enqueue(9)
numQ.enqueue(4)
numQ.enqueue(6)
numQ.enqueue(5)
numQ.enqueue(10)
check_even_odd(numQ)
