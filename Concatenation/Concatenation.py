# String Concatenation
a='10'
print(a+a)

#we can not concatenate values of different types
#print('10'+10)

#conactenation of differnt data types
emp_id = 1001
emp_name = "SCOTT"
emp_job = "Manager"
emp_salary = 9550.50
emp_dept_name = "admin"
emp_gender = "male"
emp_age = 35

emp_record = str(emp_id)+":"+emp_name+":"+emp_job+":"+str(emp_salary)+":"+emp_dept_name+":"+emp_gender+":"+str(emp_age)

print(emp_record)