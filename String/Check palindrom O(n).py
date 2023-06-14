def palinndrome(str):

    for i in range(0, int(len(str)//2)):
        if str[i] != str[len(str)-i-1]:
            return print("Not a palindrom")

    return print("Entered string is a Palindrome")

str = input("Enter string to check palindrome: ")
ans = palinndrome(str)