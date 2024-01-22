#Chris Lab
#Paystub Printing

print('Hello, welcome to PayStub Calculator')
print('Please put in personal information such as name and hours')
name=input('What is your name?\n')
hourly_wage=float(input('What is your hourly wage?\n'))
hours_worked=float(input('How many hours did you work this week?\n'))
Salary=hourly_wage * hours_worked
taxed_salary=Salary*0.10
net_pay=(Salary-taxed_salary)
print('Calculating.....')
print('Thank you for using Paystub Printing')
print("Name",name)
print("Salary",Salary)
print("Taxed Salary",taxed_salary)
print("Net Salary",net_pay)