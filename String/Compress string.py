# Compress the String
# Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.


# Exmple:
# If a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

# The string is compressed only when the repeated character count is more than 1.

# Note :
# Consecutive count of every character in the input string is less than equal to 9.


# Input Format :
# The first and the only line of input contains a string(no spaces in between).

# Output Format :
# The only line of output print the compressed string.

# Note:
# Return the compressed string and hence, no need to print.

# Constraints :
# 0 <= |S| <= 10^7
# Where |S| represents the length of string, S.

# Time Limit: 1sec
# Sample Input 1 :
# aaabbccdsa
# Sample Output 1 :
# a3b2c2dsa
# Sample Input 2 :
# aaabbcddeeeee
# Sample Output 2 :
# a3b2cd2e5

def compressString(strng):
    i= 0
    value = ""
    while(i < len(strng)):
        j= i+1
        count = 1
        while j<len(strng) and (strng[i]==strng[j]):
            j+=1
            count+=1
        if count==1:
                value+=strng[i]
        else:
            value+=strng[i]+str(count)
        i=j
    return value

strng= input()
print(compressString(strng))

        
        
