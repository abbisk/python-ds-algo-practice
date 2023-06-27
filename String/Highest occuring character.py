
# Highest Occurring Character
# Given a string, S, find and return the highest occurring character present in the given string.
# If there are 2 characters in the input string with same frequency, return the character which comes first.


# Note : Assume all the characters in the given string are lowercase.

# Input format :
# String S

# Output format :
# Highest occurring character

# Constraints :
# 0 <= |S| <= 10^7
# where |S| represents the length of string, S.

# Sample Input 1:
# abdefgbabfba
# Sample Output 1:
# b
# Sample Input 2:
# xy
# Sample Output 2:
x

def highestOccuring(string):
    new_list=[]
    maxalpha=""
    maxno=0

    for i in (string):
        if i not in new_list:
            new_list.append(i)

    for ele in new_list:
        count = 0
        for j in range(len(string)):
            if ele == string[j]:
                count+=1
            if count> maxno:
                maxno=count
                maxalpha= ele
    return print(maxalpha)
                
string = input("Enter string to check max occurrance: ")
highestOccuring(string)

            