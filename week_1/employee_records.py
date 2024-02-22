#program should get the employee name, age ,salary, bonuses.
#program should be able to increase employee salary e.g by 30%
#Program should decrease bonus e.g by ksh5000
#Date : 21/02/2024
#Name: Wayne Kareigi

#Obtaining employee details
f_name = input("Enter employee first name : ")
s_name = input("Enter employee second name : ")
age = input("Enter employee age : ")
salary = float(input("Enter employee salary :"))
bonus = float(input("Enter employee bonus :"))
total_earning = (salary + bonus)

#Show employee details
print("INITIAL EMPLOYEE DETAILS;")
print("Employee name :",f_name , s_name)
print("Employee age :", age)
print("Employee salary :", salary)
print("Employee bonus :", bonus)
print("Employee total earning : ",total_earning)

#salary increment
salary_percentage_change = float(input("Enter the percentage change : "))
newSalary = (salary * salary_percentage_change) + salary

#deceasing bonus
bonus_change= float(input("Enter the bonus change : ") )
newBonus = (bonus - bonus_change)

totalEarning = (newSalary + newBonus)

#Updated employee details
print("UPDATED EMPLOYEE DETAILS;")
print("Employee name:", f_name , s_name)
print("Employee age :",age)
print("Employee new salary :",newSalary)
print("Employee new bonus :", newBonus)
print("Employee new total earning :",totalEarning)
