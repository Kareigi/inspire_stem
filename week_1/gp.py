#Program that creates geometric progression series
#Date : 20/02/2024
#Name: Wayne Kareigi

a = int(input("Enter the first term : "))
r = float(input("Enter the common ratio of the gp : "))
n = int(input("Enter the number of terms : "))

y = (n-1)
nth_term = a * (r**y)

print("The n_th term of the gp is ",nth_term)