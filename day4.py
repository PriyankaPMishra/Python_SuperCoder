"""q1. WaP for nearest_palindrome which accepts a number and returns the nearest palindrome greater than number. ex-99, returns 1001"""
"""def nearest_palindrome(num):
    start = num+1
    while not ispalindrome(start):
        start += 1
    return start

def ispalindrome(num):
    s=str(num)
    return num==int(s[::-1])
n=int(input())
print(nearest_palindrome(n))
"""
#same as above
"""import sys
def next_smallest_palindrome(num):
    for i in range(num+1, sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(next_smallest_palindrome(int(input())))
"""

#q2
"""
d={"P":"Pediatrics", "E":"ENT", "O":"Orthopedics"}
l=list(input().split())
p=o=e=0
for i in l:
    if i=='P': p+=1
    elif i=='E': e+=1
    elif i=='O': o+=1
if p>e and p>o: print(d['P'])
if e>p and e>o: print(d['E'])
if o>p and o>e: print(d['O'])
"""

s1=input()
s2=input()
s=""
for i in s1 :
    if i in s2  and i!=' ':
        s+=i
print(s)