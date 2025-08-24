## Program to find Greater or Equal of Three Numbers:
a = int( input("Enter 1st number :") )
b = int ( input("Enter 2nd number : ") )
c = int ( input("Enter 3rd number :") )
if  a==b:
    print("both are equal ")
elif a>b:
    print("greater number in a = ",a)
elif b>c:
    print("greater number in b = ",b)
else:
    print("greater number in c = ", c)
