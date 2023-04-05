#q1
"""
ans=[]
for i in range(11):
    ans.append(i)
print(ans)
#list comprehension
print([i for i in range(11)])
#for loop - odd nums
for i in range(11):
    if i%2 == 1:
        ans.append(i)
print(ans)
print([i for i in range(11) if i%2 != 0])

#even square
for i in range(11):
    if i%2 == 1:
        ans.append(i)
    else: ans.append(i**2)
print([i if i%2 != 0 else i**2 for i in range(11) ])
"""

#q2
"""
n=6
l=[]
for i in range(8):
    for j in range(8):
        if i==0 or j==0 or j==7 or i==7:
            print('------', end=" ")
        else: print((j,i), end=" ")
    print()

ans=[[(j,i) if i not in (0,7) and j not in (0,7) else ('----') for i in range(8)] for j in range(8)]
for i in ans: print(i)
"""

#q3
"""
mat=[[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16], [4,3,2,1]]
ans=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] & 1 == 0:
            ans.append(mat[i][j]**3)
        else:
            ans.append(mat[i][j]**2)
print("AS ELEMENTS:")
for k in ans:
    print(k, end= " ")
print("\nAS MATRIX:", ans)
print("LIST COMPREHENSION:",[[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])
#here row=4, row=mat[0]=4
"""

#q4. for each num in list_b, get the num and its index in mylist. return the res as a list of tuples.
"""
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
ans=[]
for num in list_b:
    idx= mylist.index(num)
    if (num, idx) not in ans:
        ans.append((num, idx))
print("using loop:", ans)
print("using list comprehension", [(ele, mylist.index(ele)) for ele in list_b])
dct= {ele: mylist.index(ele) for ele in list_b}
print("using dictionary comprehension:", dct)
"""

#q5
"""
sentences=["a new world record was set", "in the holy city of ayodhya", 
"in the eve of diwali on tuesday", "with over three lakh diya or earthen lamps", 
"lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
results = []
for sentence in sentences:
    sentence_tokens = []
    for word in sentence.split(' '):
        if word not in stopwords:
            sentence_tokens.append(word)
    results.append(sentence_tokens)
print(results)
ans = [[word for word in sentence.split(' ') if word not in stopwords] for sentence in sentences]
print(ans)
"""

#q6
"""
str="Lee Quan Yew"
ans=[]
for i in str.lower():
    if i==" ": ans.append(" ")
    else:
        val=ord(i)-96
        print(val)
        ans.append(val)
print(ans)
"""

#q7
"""
arr=list(map(int, input().split(',')))
print(arr)
num1=0
num2=""
idxOf5 = arr.index(5)
idxOf8 = arr.index(8)
num1=sum(arr[:idxOf5]) + sum(arr[idxOf8+1:])
listFrom5_8 = arr[idxOf5:idxOf8+1]
num2=""
for i in listFrom5_8:
    num2+=str(i)
print("NUM1:", num1)
print("NUM2:", num2)
print("OP:", int(num2)+num1)
"""

#q8
"""
num=int(input())
digs=[int(i) for i in str(num)]
sq=[i**2 for i in digs]
print(digs)
print(sq)
print(sum(sq))
s=str(num)
if sum(sq)%2==0:
    print(s[-1:]+s[:-1])
else:
    print(s[-2:] + s[:-2])
"""


"""
facts=[]
def factors(n):
    for i in range(1, n+1):
        if n%i==0:
            facts.append(i)
    return facts
def isprime(n):
    flag=0
    for i in range(2, n//2):
        if n%i==0:
            flag=1
    if(flag == 1):
        return False
    return True
l=[]
for i in factors(12):
    if isprime(i):
        l.append(i)
print(l)
print(max(l))
"""