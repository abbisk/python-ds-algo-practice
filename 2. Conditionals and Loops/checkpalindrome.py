# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# 1.Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

# Sample Input 1
# 121

# Sample Output 1 :
# true

# Sample Input 2
# 1032

# Sample Output 2
# false
# 

# def checkPalindrome(n):
#     reverse = 0
#     while n>0:
#         remainder=n%10
#         n= int(n/10)
#         reverse=reverse*10+remainder
#     return reverse


# n= int(input("Enter number to check palindrome: "))
# reverse = checkPalindrome(n)
# if n==reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Method 2
n= int(input("Enter value to check palindrome: "))
realnum = n
reverse = 0
while n>0:
    reminder = n%10
    reverse= reverse*10+reminder
    n = n//10

if reverse == realnum:
    print("Plaindrome")
else:
    print("Not a palindrome")