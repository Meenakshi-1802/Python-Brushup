## Program for grade of the students based on avg marks
m1 = int(input("Enter sub1 Marks :"))
m2 = int(input("Enter sub2 Marks :"))
m3 = int(input("Enter sub3 Marks :"))

if m1>=40 and m2>=40 and m3>=40:
    print("Student Pass")
    avg = (m1+m2+m3)/3
    print("Average Marks :",avg)
    if avg >= 90:
        print("Grade A")
    elif avg >= 80:
        print("Grade B")
    elif avg >= 70:
        print("Grade C")
    elif avg >= 60:
        print("Grade D")
    else:
        print("Grade E")
    
else:
    print("Student Fail and No Grade")