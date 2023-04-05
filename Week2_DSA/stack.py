class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if (self.__top == self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if (self.__top == -1):
            return True
        return False

    def push(self, element):
        if self.is_full():
            print("Stack Full")
        else:
            self.__top+=1
            self.__elements[self.__top]=element

    def pop(self):
        if self.is_empty():
            print("Stack Empty")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if self.is_empty():
            print("Stack Empty")
        else:
            index=self.__top
            while(index >= 0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

ball_stack = Stack(4)
print("is it empty", ball_stack.is_empty())
ball_stack.push(5)
print("is it empty", ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Stack Size: ", ball_stack.get_max_size())
print("Popped: ", ball_stack.pop())
print("Stack after deleting")
ball_stack.display()
print("Stack size: ", ball_stack.get_max_size())