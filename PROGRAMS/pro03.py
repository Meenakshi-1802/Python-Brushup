## Program to find Greater of Three Numbers:
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

if a>b:
    if a>c:
        print("big number a :",a)
    else:
        print("big number c :",c)
elif b>c:
    print("big number b :",b)  
else:
    print("big number c :",c)  


     ### OR ###

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

if a>b and a>c:
    print("big number a :",a)

elif b>a and b>c:
    print("big number b :",b)

else:
    print("big number c :",c)

