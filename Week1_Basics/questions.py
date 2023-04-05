#1. Given an array of size K, split the array into N chunks
"""
k=int(input())
if k<=0 or k%2!=0: print("Invalid Input")
else:
    arr=list(map(int, input().split()))
    n=int(input())
    for i in range(0,len(arr), n):
        for j in arr[i:i+n]:
            print(j, end=" ")
        print()
"""


#2. sort the numbers in the array, 
#but on the condition that all the even numbers get sorted first and placed in the front
#followed by all the odd numbers sorted and placed following the even numbers.
"""
n = int(input())
l = list(map(int, input().split()))
if(len(l) <= 0): print("Invalid Input")
else:
    l.sort()
    e = []
    o = []
    for i in l:
        if i%2 == 0:
            e.append(i)
        else:
            o.append(i)
    #e.sort()
    #o.sort()
    for i in e+o:
        print(i, end=" ")
"""

#3. multiple of 3 or 5 or 3 and 5
"""
num = int(input("Enter a number:"))
if (num % 3 == 0):
    if (num % 5 == 0):
        print("Multiple of both ")
    else:
        print("multiple of 3")
elif(num % 5 == 0): print("multiple of 5")
#elif(num % 3 == 0 and num % 5 ==0): print("multiple of both 3 and 5")
else: print("Invalid")
"""

#q4. check for 7.
# It should display the product of the three values except when one of the integer value is 7.
# In that case, 7 should not be included in the product and the values to its left also should not be included.
# If there is only one value to be considered, display that value itself.
# If no values can be included in theproduct, display -1.
"""
a,b,c = map(int, input().split())
if (a==7):
    print(b*c)
elif(b==7):
    print(c)
elif(c==7):
    print("-1")
else:
    print(a*b*c)
"""

#q5. Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency.
# The program should identify and display the amount provided in the currency to get the specified amount in INR.
# Note: Use the forex information provided in the table below for the calculation.
# Consider that only the currency names mentioned in the table are valid.
# For any invalid currency name, display -1.
# Currency Equivalent of 1.00 INR
# Euro 0.01417 British Pound 0.0100 Australian Dollar 0.02140 Canadian Dollar 0.02027
"""
curr = input()
inr = float(input())
if curr=="euro": res = inr*0.01417
elif curr=="british pound": res = inr*0.0100
elif curr=="australian dollar": res = inr*0.02140
elif curr=="canadian dollar": res = inr*0.02027
else: print(-1)
print(res, "inr")
"""

#q3
#adult 37550
#child 1/3 adult
#tax = 7% ticket
#disc = 10% ticket + tax
"""
adult = int(input())
child = int(input())
tot = ((adult*37550.0)+(child*37550.0/3))
#after tax tot + 0.07tot = tot(1+0.07)
after_tax = tot*1.07
#after discount 0.9*after_tax
after_disc = after_tax*0.9
print(after_disc)

ans = ((adult*37550.0)+(child*37550.0*1/3))*1.07*0.9
print(ans)
"""

#Q4
"""
x_5 = int(input())
y_1 = int(input())
z_amt = int(input())
tot_5=0
tot_1=0
if z_amt > x_5*5 + y_1*1: print("Invalid")
else:
    if z_amt%5 == 0:
        tot_5 = z_amt%5
    elif z_amt%5 != 0:
        tot_1 = z_amt%5
        tot_5 = z_amt//5
    print(tot_5, tot_1)
"""