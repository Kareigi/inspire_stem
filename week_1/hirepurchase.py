#program that calculates the hire purchase price 
#Date : 21/02/2024
#Name: Wayne Kareigi


dep = float(input("Enter the deposited amount : "))
n = float(input("Enter the number of months : "))
inst = float(input("Enter the monthly installment paid : "))

hpp = dep + (n * inst)

print("The hire purchase  price is : ",hpp)