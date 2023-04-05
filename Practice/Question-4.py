"""Write a function check_anagram to check if two input strings are anagrams or not"""

def anagram_check(str1, str2):
    list1 = [letter for letter in str1]
    list2= [letter for letter in str2]
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"

s1 = "ate"
s2 = "eat"
print(anagram_check(s1, s2))