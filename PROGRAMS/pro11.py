## Program to display Message on cricekt bat's man score
score = int(input("Enter the score:"))
if score<0:
    print("Invalid Score")
elif score==0:
    print("Duck Out")
elif score<50:
    print("Normal score")
elif score<100:
    print("Half Century")
elif score<200:
    print("Century")
else:
    print("more than Century")