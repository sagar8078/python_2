def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))


a = float(input("Enter a number"))
result = factorial(a)
print("Factorial of ",a,  " is ",result)