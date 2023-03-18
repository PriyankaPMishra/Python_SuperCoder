"""
#LOOPING
print("between 1-100")
for i in range(1, 101):
    print(i, end = " ")
print("\nEvens between 1-100")
for i in range(1, 101):
    if(i%2 == 0): print(i, end= " ")
print("\nOdds between 1-100")
for i in range(1, 101):
    if(i%2 != 0): print(i, end=" ")
print("\nbetween 100-1")
for i in range(100,0,-1):
    print(i, end= " ")
print("\nreverse evens")
for i in range(100,1,-2):
    print(i, end=" ")
print("\nreverse odds")
for i in range(99,0,-2):
    print(i, end=" ")
print("\nBreak")
for i in range(1,100):
    if(i == 50):
        break
    print(i, end=" ")
print("\nContinue")
for i in range(1,101):
    if(i == 50):
        continue
    print(i, end=" ")
print("\nPass")
for i in range(1,101):
    if(i == 50):
        pass
    print(i, end=" ")
"""

#functions
def function1():
    print("Func1")
function1()
def function2(num1, num2):
    print("num1=",num1,"num2=",num2)
function2(10, 20)

def function3(num1, num2):
    num3=num1+num2
    return num3
print(function3(10, 20))

def function4(num1, num2):
    num3 = float(num1)+num2
    return num3
print(function4("10", 20.2))

print("positional args")
def function5(num1, num2, num3, num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function5(10, 20, 30, 10)

print("keyword args")
def function5(num1, num2, num3, num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function5(num1=10, num2=20, num3=30, num4=1.0) #data/args sent from right to left

print("default args")
def function6(name, roll, branch, clgname="giet"):
    print(name, roll, branch, clgname)
function6("pm",1,"cse","giet")
function6("pm",2,"cse")

def function4(*var):
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
#adding variable types of arguments
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
        print(sum1)
add(10,20)
print()
add(10,20,30,40)
print()
add(10,20,30,40,50,60)