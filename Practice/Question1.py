"""
The owner of a BakeHouse wants to keep track of the tables that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.
BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class.
Represent occupied_table_list using an appropriate data structure.
Note: Table numbers should be maintained in ascending order in the occupied_table_list.
Tables should be allocated and de-allocated as mentioned in the example below:
Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should beallocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2 as it is the first free table.
Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.
"""
class BakeHouse:
    def __init__(self):
        self.__occupied_table_list = []
        
    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        table_num = 1
        while table_num in self.__occupied_table_list:
            table_num+=1
        self.__occupied_table_list.append(table_num)
        self.__occupied_table_list.sort()
        return table_num

    def deallocate_table(self, table_num):
        if table_num in self.__occupied_table_list:
            self.__occupied_table_list.remove(table_num)
            return "Table De-Allocated"
        else:
            return "Table already vacant"

bh = BakeHouse()
print(bh.get_occupied_table_list())
table1 = bh.allocate_table()
table2 = bh.allocate_table()
table3 = bh.allocate_table()
table4 = bh.allocate_table()
print(bh.get_occupied_table_list())
bh.deallocate_table(table3)
bh.deallocate_table(table2)
print(bh.get_occupied_table_list())
new = bh.allocate_table()
print(bh.get_occupied_table_list())