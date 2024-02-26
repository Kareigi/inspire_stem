#program should get the employee name, age ,salary, bonuses.
#program should be able to increase employee salary 
#Program should decrease bonus e.g by ksh5000
#Date : 26/02/2024
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

#if salary >100000 give 30% raise
#if salary between 100000 and 150000 give 15%raise
#if salary >150000 give 5% raise

#salary raise
if salary <= 100000 :
    new_salary = (salary * 0.3)+ salary
elif salary >100000 and salary <= 150000:
    new_salary = (salary *0.15) + salary
elif salary > 150000 :
    new_salary = (salary * 0.5) + salary       

#Bonus decrease
bonus_change= int(input("Enter the bonus change : " ))
new_bonus = bonus - bonus_change  

totalEarning= new_salary + new_bonus

#Updated employee details
print("UPDATED EMPLOYEE DETAILS;")
print("Employee name:", f_name , s_name)
print("Employee age :",age)
print("Employee new salary :",new_salary)
print("Employee new bonus :",new_bonus )
print("Employee new total earning :",totalEarning)


