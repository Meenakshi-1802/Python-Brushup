#Reverse a string
string = input("Enter a string:")
reverse_string = string[::-1]
print(reverse_string,"is a reverse string")

#reverse a num
num = int(input("Enter a num:"))
original_num = num
reverse_num = 0
while num > 0:
    digit = num%10
    reverse_num = (reverse_num*10)+digit
    num = num//10

print(reverse_num,"is a reverse number")