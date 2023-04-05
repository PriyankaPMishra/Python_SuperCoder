#Q1 -
"""#q1. WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types – "Two Wheeler" and "Four Wheeler".
Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two-wheelers and 6% of the vehicle cost for four wheelers.
Details of Class :

ClassName: Vehicle
Attributes: vehicle_cost vehicle_type premium_amount vehicle_id
Methods: calculate_premium()
        init(self, vehicle_type, vehicle_id,vehicle_cost)
        display_vehicle_details() : Display the type of vehicle, cost and premium amount.
Write a Python program to implement the class with its attributes and methods.
Note:
Consider all instance variables to be private and methods to be public
Include getter and setter methods for all instance variables
take vehicle type and vehicle cost from the user.
Create an object of the Vehicle and initialize all the details of the object through the constructor and
Calculate the premium amount and display the vehicle details(vehicle type, vehicle cost, and the premium amount ) of the vehicle.
Input1: TwoWheeler 50000
Output1:TwoWheeler 50000 1000
Input2: FourWheeler 500000
Output2: FourWheeler 500000 30000
"""
#a1
import sys
"""
class Vehicle:
    def __init__(self):
        self.__vehicle_cost=None
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__premium_amount=None

    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_type(self,vehicle_type):
        #vehicle_type = ["Two-Wheeler", "Four-Wheeler"]
        if vehicle_type == "Two Wheeler" or vehicle_type == "Four Wheeler":
            self.__vehicle_type = vehicle_type
        else:
            return "invalid"
    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost*0.02
        if self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = self.__vehicle_cost*0.06

    def display_vehicle_details(self):
        print("Vehicle Type:",self.__vehicle_type, #for vehicle type
              "\nVehcile Cost:",self.__vehicle_cost, #for vehicle cost
              "\nPremium Amount:",int(self.__premium_amount)) #for the premium amount

v = Vehicle()
v.set_vehicle_id(int(input("VEHICLE ID: ")))
v.set_vehicle_type(input("VEHICLE TYPE: "))
v.set_vehicle_cost(int(input("VEHICLE COST: ")))
v.calculate_premium()
v.display_vehicle_details()
"""

#q2
"""
A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
    Age is greater than 20
    Marks is between 0 and 100 (both inclusive)
    A student qualifies for admission, if
        Age and marks are valid and
        Marks is 65 or more
Write a python program to represent the students seeking admission in the university.
Class: Student
Methods: __init__(), validate_marks(), validate_age(), check_qualification() 
"""
#a2
"""
courses = {1001: 25575, 1002: 15500}
class Student:
    def __init__(self):
        self.__id = None
        self.__marks = None
        self.__age = None
        self.__courseid = None
        self.__fees = None

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age

    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks

    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def validate_marks(self):
        if self.__marks >= 65 and self.__marks <= 100:
            return True
        else:
            return False

    def check_qual(self):
        if self.validate_age() and self.validate_marks():
            print("Qualified for Admission")
        else:
            print("Disqualified for Admission")
            sys.exit()

    def get_courseid(self):
        return self.__courseid

    def course_choice(self, courseid):
        if courseid in courses.keys():
            self.__courseid = courseid
            if self.__marks >= 85:
                self.__fees = courses[courseid] * 0.75
            else:
                self.__fees = courses[courseid]
            return True
        return False

    def get_fees(self):
        return self.__fees

    def display_details(self):
        print("Student ID: ", self.__id)
        print("Student Marks: ", self.__marks)
        print("Student Age: ", self.__age)
        print("Student Fees: ", self.__fees)

s = Student()
s.set_id(int(input("STUDENT ID: ")))
s.set_marks(float(input("STUDENT MARKS: ")))
s.set_age(int(input("STUDENT AGE: ")))
#s.validate_age()
#s.validate_marks()
s.check_qual()
s.get_courseid()
s.course_choice(int(input("COURSE ID (1001 or 1002): ")))
s.get_fees()
s.display_details() 
"""

#q3
"""PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.

Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
                    If quantity is valid, return true. Else return false

Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
True – additional topping is required, False – additional topping is not required.
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
                       If pizza type is valid, return true. Else return false.
calculate_pizza_cost(): Calculate pizza cost. Validate pizza type and quantity.
                        If valid, Identify pizza cost based on details mentioned in the table.
                        Set attribute, pizza_cost with the calculated pizza cost.
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. 
Example – S101, s102, m103, S104, M105 etc. If invalid, set pizza_cost to -1.
PizzaType Cost/Pizza(in Rs) Additional topping cost/Pizza (in Rs), if applicable
Small 150 35
Medium 200 50

Doordelivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms.
                            If valid, return true. Else, return false.
calculate_pizza_cost(): Calculate pizza cost
Validate distance in kms. If valid, Calculate pizza cost. (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms Delivery Charge in km(in Rs)
For first 5 kms 5
For remaining 5 kms 7
Else, set pizza_cost to -1

Note: Perform case insensitive string comparison  
For testing:
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the details"""
#a3
class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False

class Pizzaservice:
    counter = 100

    def __init__(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = 0
        self.service_id = ''

    def validate_pizza_type(self):
        if self.pizza_type.lower() == 'small' or self.pizza_type.lower() == 'medium':
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            if self.pizza_type.lower() == 'small':
                pizza_cost = self.quantity * 150
                if self.additional_topping:
                    pizza_cost += self.quantity * 35
            elif self.pizza_type.lower() == 'medium':
                pizza_cost = self.quantity * 200
                if self.additional_topping:
                    pizza_cost += self.quantity * 50
            self.pizza_cost = pizza_cost
            Pizzaservice.counter += 1
            self.service_id = self.pizza_type[0].upper() + str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1


class Doordelivery(Pizzaservice):
    def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super().__init__(pizza_type, quantity, additional_topping)
        self.distance_in_kms = distance_in_kms

    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False


# Testing the program
pizza1 = Pizzaservice('small', 3, True)
pizza1.calculate_pizza_cost()
print(f"Service ID: {pizza1.service_id}"
      f"\nPizza Type: {pizza1.pizza_type}"
      f"\nQuantity: {pizza1.quantity}"
      f"\nAdditional Topping: {pizza1.additional_topping}"
      f"\nPizza Cost: {pizza1.pizza_cost}")
print()
pizza2 = Doordelivery('medium', 2, False, 8)
pizza2.calculate_pizza_cost()
print(f"Service ID: {pizza2.service_id}"
      f"\nPizza Type: {pizza2.pizza_type}"
      f"\nQuantity: {pizza2.quantity}"
      f"\nAdditional Topping: {pizza2.additional_topping}"
      f"\nDistance in kms: {pizza2.distance_in_kms}"
      f"\nPizza Cost: {pizza2.pizza_cost}")