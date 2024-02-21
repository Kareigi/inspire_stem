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
print("Employee name :",f_name + s_name)
print("Employee age :", age)
print("Employee salary :", salary)
print("Employee bonus :", bonus)
print("Employee total earning : ",total_earning)

#salary increment
salary_increase_percentage = 0.3
newSalary = (salary * salary_increase_percentage) + salary

#deceasing bonus
decrease_bonus_amount = 5000
newBonus = (bonus - decrease_bonus_amount)

totalEarning = (newSalary + newBonus)

#Updated employee details
print("UPDATED EMPLOYEE DETAILS;")
print("Employee name:", f_name , s_name)
print("Employee age :",age)
print("Employee new salary :",newSalary)
print("Employee new bonus :", newBonus)
print("Employee new total earning :",totalEarning)
