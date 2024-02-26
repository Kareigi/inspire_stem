#Program that gets sum of the first 20numbers
#Date :26/02/2024
#Name :Wayne Kareigi

sum_nums = 0

maxValue= int(input("Enter the max value : "))
for x in range (0,(maxValue+1) ):
    sum_nums = sum_nums + x
    print(sum_nums)