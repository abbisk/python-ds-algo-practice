# Check Palindrome
# Given a String s, check it its palindrome. Return true if string is palindrome, else return false.
# Palindrome strings are those, where string s and its reverse is exactly same.


# Input Format :
# String S

# Output Format :
# "true" if S is palindrome, else "false"

# Constraints :
# 0 <= |S| <= 10^7
# where |S| represents the length of string, S.

# Sample Input 1 :
# abcdcba
# Sample Output 1 :
# true
# Sample Input 1 :
# abcd
# Sample Output 1 :
# false

# Method 1 

# str = input("Enter String: ")

# if str==str[::-1]:
#     print("Is palindrome")
# else:
#     print("Not a palindrome")


# Method 2
# Time complexity: O(n)
# Auxiliary Space: O(1)

# def palinndrome(str):
#     for i in range(0, int(len(str)//2)):
#         if str[i] != str[len(str)-i-1]:
#             return print("Not a palindrom")

#     return print("Entered string is a Palindrome")

# str = input("Enter string to check palindrome: ")
# ans = palinndrome(str)

# Method 3

def palindrom(str):
    w = ""
    for i in str:
        w= i+w

        if (str == w):
            return print("palindrom")
        
    return print("Not a palindrom")

str = input("Enter string to check palindrom: ")
palindrom(str)
