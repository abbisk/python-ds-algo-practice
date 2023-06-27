# Given a string, S, remove all the consecutive duplicates that are present in the given string. That means, if 'aaa' is present in the string then it should become 'a' in the output string.


# Input format :
# String S

# Output format :
# Modified string

# Constraints :
# 0 <= |S| <= 10^7
# where |S| represents the length of string, S.

# Sample Input 1:
# aabccbaa
# Sample Output 1:
# abcba
# Sample Input 2:
# xxyyzxx
# Sample Output 2:
# xyzx

s= input()

s=s+" "

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        print(s[i], end="")