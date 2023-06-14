# Check Permutation
# Given two strings, S and T, check if they are permutations of each other. Return true or false.
# Permutation means - length of both the strings should same and should contain same set of characters. Order of characters doesn't matter.
# Note : Input strings contain only lowercase english alphabets.



# Input format :
# Line 1 : String 1
# Line 2 : String 2

# Output format :
# 'true' or 'false'

# Constraints :
# 0 <= |S| <= 10^7
# 0 <= |T| <= 10^7
# where |S| represents the length of string, S.

# Sample Input 1 :
# abcde
# baedc
# Sample Output 1 :
# true
# Sample Input 2 :
# abc
# cbd
# Sample Output 2 :
# false

# Method 1
# s = input()
# t= input()

# if sorted(s) == sorted(t):
#     print("True")
# else:
#     print("Falst")a


# Method 2
def permutation(s,t):
    flag = "False"
    for i in s:
        for j in t:
            if j == i:
                flag="True"
                break
        if flag=="False":
            return print("Not permutaiton")
            exit(1)
    return print("Permutation")
s = input()
t= input()
permutation(s,t)