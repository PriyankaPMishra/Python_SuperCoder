"""
The number, 197, is called a circular prime because all
 rotations of the digits: 197, 971, and 719, are themselves
 prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11,
13, 17, 31, 37, 71, 73, 79, and 97.
Write a python program to find and display the number of
circular primes less than the given limit.
"""
def isPrime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

# print(num%100)
# print(num//100)
# print(num)
# print(num%10)
# print(num//10)
def rotate(num):
    digits = len(str(num))
    for i in range(digits):
        rem = num%10
        rem = rem*(10**(digits-1))
        num = num//10
        num = num+rem
        return num

for i in range(2, 101):
     if isPrime(i) and isPrime(rotate(i)):
         print(i)

