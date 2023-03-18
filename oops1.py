#constructor, getter, setter
"""
class Example:
    #Using constructor
    def __init__(self, num):
        self.num=num

    #using setter method
    def set_num(self, num):
        self.num=num

    #using getter method
    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
"""

#
"""
class Cust:
    def __init__(self):
        self.cust_id=100
        #cust_id=100 === error
c=Cust()
print(c.cust_id)
"""

#
"""
class Cust:
    def __init__(self, id):
        self.id = id
c=Cust(200)
print(c.id)
"""

#
"""
class Book:
    def __init__(self):
        self.title = None
my_fav=Book()
my_fav.title="Programming"

your_fav=Book()
your_fav.title="Python"
print("My fav:", my_fav.title)
print("Your fav:", your_fav.title)
"""
#
"""
class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

    def __str__(self):
        return "Shoe with material:" + str(self.material) + " Shoe with price:" + str(self.price)
s1=Shoe(999, "Canvas")
s2=Shoe(788, "Formal")
print(s1.material, " ", s1.price)
print(s2.material," ", s2.price)
print("Unique id of the object s1 is:", id(s1))
print("Unique id of the object s2 is:", id(s2))
print(s1)
"""

#
"""
class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying Details")
    def purchase(self):
        self.display()
        print("Calculating price..")

Mobile().purchase()
"""

#
"""
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price- self.price*(discount / 100)
        print("Total price of", self.brand, "mobile is",self.total_price)
mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)
mob1.purchase()
mob2.purchase()
"""

#
"""
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
        #__ before a variable means it is a private variable and cannot be accessed from outside the class.
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
            print("The balance is ",self.__wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
#print(c1.__wallet_balance) --> throws error
"""

#
"""
class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_wallet_balance(self, amount):
        if amount < 1000 and amount>  0:
            self.__wallet_balance = amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
"""

#your code goes here
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None

    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top

    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
"""dining_table=Table()
rate=dining_table.identify_rate(True, False)
print(rate)"""

dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table, back_table, front_table)