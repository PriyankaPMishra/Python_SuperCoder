#1arraychunks
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


"""
#3playwitharray
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

#2multiple
num = int(input("Enter a number:"))
if (num % 3 == 0):
    if (num % 5 == 0):
        print("Multiple of both ")
    else:
        print("multiple of 3")
elif(num % 5 == 0): print("multiple of 5")
#elif(num % 3 == 0 and num % 5 ==0): print("multiple of both 3 and 5")
else: print("Invalid")

#q1
a,b,c = map(int, input().split())
if (a==7):
    print(b*c)
elif(b==7):
    print(c)
elif(c==7):
    print("-1")
else:
    print(a*b*c)

#q2
curr = input()
inr = float(input())
if curr=="euro": res = inr*0.01417
elif curr=="british pound": res = inr*0.0100
elif curr=="australian dollar": res = inr*0.02140
elif curr=="canadian dollar": res = inr*0.02027
else: print(-1)
print(res, "inr")

#q3
#adult 37550
#chilod 1/3 adult
#tax = 7% ticket
#disc = 10% ticket + tax
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

#Q4
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

s=input()
if s[-1]!= 'a':
    r=s.rstrip('a')
    print(r)
    l=r.lstrip('a')
    print(l)
    if l==l[::-1]:
        print("Yes")
else:
    print("No")