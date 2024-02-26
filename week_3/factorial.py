# Program that gets the factorial of numbers
#Date :26/02/2024
#Name :Wayne Kareigi

factorial_nums = 1

maxValue= int(input("Enter the max value : "))
for x in range (1,(maxValue+1) ):
    factorial_nums = factorial_nums * x
    print(factorial_nums)
    
#printing even numbers 
for i in range (0,20,2) :
    print("\n")
    print(i)   

#printing odd numbers
for i in range (1,20,2) :
    print("\n")
    print(i)       