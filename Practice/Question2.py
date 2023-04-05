"""A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp,
the teacher rewards them with chocolates. Write a Python function to Find the total number of chocolates received by all the children put together.
Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.
 The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.
If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.
If the given child Id is invalid, an error message "Child id is invalid" should be displayed.
Otherwise, the extra chocolates provided for the child must be added to his/her existing number of chocolates and display the list containing the total number of chocolates received by each child.

child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

functions
calculate_total_chocolates()
reward_child(child_id_rewarded,extra_chocolates)"""

class Teacher:
    def __init__(self, child_id, chocolates_received):
        self.__child_id = child_id
        self.__chocolates_received =chocolates_received
    def calculate_total_chocolates(self):
        return sum(self.__chocolates_received)
    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates<1:
            print("Extra chocolates is less than 1.")
        if child_id_rewarded not in self.__child_id:
            print("Child ID is invalid.")
        else:
            self.__chocolates_received.append(extra_chocolates)
        print(self.__chocolates_received)

child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
print("Chocolates Received:", chocolates_received)
t = Teacher(child_id, chocolates_received)
print("total chocolates rceieved by all children:", end="")
print(t.calculate_total_chocolates())
print("Updated Chocolates Received List: ", t.reward_child(30, 5))
print("Total Chocolates:", t.calculate_total_chocolates())
t.reward_child(10, 0)
t.reward_child(1, 34)