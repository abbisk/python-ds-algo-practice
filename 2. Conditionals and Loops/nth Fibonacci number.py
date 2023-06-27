def Fibonacci(n):
    if n ==1:
        return 1
    elif n==2:
        return 2
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
n= int(input())
print(Fibonacci(n))

    