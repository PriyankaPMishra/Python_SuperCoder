#list - mutable, default index = 0, ordered

#Basics
"""
list1=[]
print(list1, type(list))
list2=[1,2,3,4]
print(list2, type(list2))
"""

#List Functions
"""
list3=[101, 201, 301]
print("Before Append:", list3)
list3.append(401)
print("After Append:", list3)
list3.extend(list2)
print("After Extend:", list3)
list3.insert(0, 51)
print("After Inserting at 0:", list3)
list3.insert(4, 55)
print("After Inserting at 4:",list3)
list3.remove(55)
print("After removing 55:", list3)
list3.pop()
print("Pop without args:", list3)
list3.pop(4)
print("After popping 4th index:", list3)
del list3[0]
print("After deleting list[0]:", list3)
"""

#q1. calculating number of digits and alphabets in a string.
def func(s):
    alpha=0
    digs=0
    for i in s:
        if i.isalpha(): alpha+=1
        if i.isdigit(): digs+=1
    return [alpha,digs]
s=input()
print(func(s))


#q2. counting number of pairs in a list that add upto the target.
def func2(arr,n):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr) ):
            if arr[i]+arr[j]==n:
                count+=1
    return count
arr=eval(input("enter a list: "))
target=int(input())
print(func2(arr, target))

#q3.
def func3(str):
    if(len(str)<2): return -1
    elif(len(str)==2): return str*2
    else:
        return str[:2]+str[-2:]
s=input()
print(func3(s))

#q4
def func4(str):
    if len(str)<3: return str
    elif(str[-3:] == "ing"): return str+"ly"
    else: return str+"ing"
s=input()
print(func4(s))

#q5
def check_double(num):
    doub = num*2
    if (len(str(num)) == len(str(doub)) and set(str(num)) == set(str(doub))):
        return True
    return False
print(check_double(125874))

#q6
def find_more_than_avg(marks):
    totm = sum(marks)
    avgm = totm/10
    stu=0
    for i in marks:
        if i> avgm: stu+=1
    return (stu/10)*100
print(find_more_than_avg((12, 18, 25, 24, 2, 5, 18, 20, 20, 21)))

def generate_freq(marks):
    l=[]
    for i in range(26):
        l.append(marks.count(i))
    return l
print(generate_freq((12, 18, 25, 24, 2, 5, 18, 20, 20, 21)))

def sort_marks(marks):
    marks=list(marks)
    marks.sort()
    return marks
print(sort_marks((12, 18, 25, 24, 2, 5, 18, 20, 20, 21)))

#q7
def translate(dict, ewords):
    trans=[]
    for i in ewords.split():
        if i in dict:
            trans.append(dict[i])
    return " ".join(trans)
dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
ewords="happy new year"
print(translate(dict, ewords))
"""

"""
def subarray(n1, n2):
    l=[i for i in range(n1, n2+1)]
    lists=[]
    count=0

    for i in range(len(l)+1):
        for j in range(i):
            lists.append(l[j:i])
    print(lists)
    for i in lists:
        if sum(i)&1==1:
           count+=1
    return count

n1=int(input())
n2=int(input())
print(subarray(n1,n2))

# same as above
# a = int(input())
# b = int(input())
# arr= [i for i in range(a,b+1)]
# l1 = [arr[i:j+1] for i in range(len(arr)) for j in range(i,len(arr))]
# print(l1)
# c = 0
# for i in l1:
#     if sum(i) % 2 == 0:
#        c+=1
#print(c)
