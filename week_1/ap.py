#Program that creates geometric progression series
#Date : 20/02/2024
#Name: Wayne Kareigi

a = int(input("Enter the first term : "))
n = int(input("Enter the number of terms : "))
d = int(input("Enter the common difference : "))

nth_term = a +(n-1)* d
print("The nth term of the ap is : ",nth_term)
