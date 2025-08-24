## Program for having four subjects,any three subjects pass,then student pass
m1 = int(input("Enter sub1 Marks :"))
m2 = int(input("Enter sub2 Marks :"))
m3 = int(input("Enter sub3 Marks :"))
m4 = int(input("Enter sub4 Marks :"))
count = 0

if m1>=40:
    count = count + 1
    print("sub1 pass")
else:
    print("sub1 fail")
if m2>=40:
    count = count + 1
    print("sub2 pass")
else:
    print("sub2 fail")
if m3>=40:
    count = count + 1
    print("sub3 pass")
else:
    print("sub3 fail")
if m4>=40:
    count = count + 1
    print("sub4 pass")
else:
    print("sub4 fail")

if count >= 3:
    print("Pass")
else:
    print("Fail")
print("Pass count :",count)

