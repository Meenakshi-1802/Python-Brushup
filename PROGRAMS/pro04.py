##  Program to find Smallest of Three number:
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

small = a

if b<small:
    small=b
if c<small:
    small=c

print("small number is:",small)