#find the largest of three numbers
a = int(input("Enter First num:"))
b = int(input("Enter Second num:"))
c = int(input("Enter Third Num:"))

if a >= b and a >= c:
    print(a,"is the largest number")
elif b >= a and b >= c:
    print(b,"is the largest number")
else:
    print(c,"is the largest num")

#using max() function
a = int(input("Enter First num:"))
b = int(input("Enter Second num:"))
c = int(input("Enter Third Num:"))

print("The largest number is:",max(a,b,c))