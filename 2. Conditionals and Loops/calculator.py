while True:
    n= int(input("Enter operation: "))

    if n==1:
        n1= int(input("Enter first no: "))
        n2 = int(input("Enter second no: "))
        result = n1+n2
        print("Sum is: ",result)
    elif n==2:
        n1= int(input("Enter first no: "))
        n2 = int(input("Enter second no: "))
        result = n1-n2
        print("Sbbtract is: ",result)
    elif n==1:
        n1= int(input("Enter first no: "))
        n2 = int(input("Enter second no: "))
        result = n1*n2
        print("Multiplicatoion is: ",result)
    elif n==1:
        n1= int(input("Enter first no: "))
        n2 = int(input("Enter second no: "))
        result = n1/n2
        print("Devide is: ",result)
    elif n==1:
        n1= int(input("Enter first no: "))
        n2 = int(input("Enter second no: "))
        result = n1//n2
        print("Remainder is: ",result)
    elif n==6:
        exit()
    else:
        print("Invalid Operations")