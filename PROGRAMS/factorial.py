#factorial using loop
num = int(input("Enter a num:"))
fact = 1

if num < 0:
    print("Factorial is not possible for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        fact = fact * i
    print("The factorial of ",num,"is",fact)

#factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter a number:"))
if num < 0:
    print("factorial not possible")
else:
    print("the factorial of",num,"is",factorial(num))