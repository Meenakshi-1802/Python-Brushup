## Program to find Max Min of Three Numbers:
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

max = a
min = a

if b>max:
    max=b
if b<min:
    min=b
if c>max:
    max=c
if c<min:
    min=c

print("max :",max)
print("min :",min)