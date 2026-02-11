employee_file = open("employee.txt","r")

# print(employee_file.read())
# print(employee_file.readline())
print(employee_file.readlines()[1])

employee_file.close()