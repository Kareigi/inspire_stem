#A program that determines the arithmetic progression of sequences
#Date : 20/02/2024
#Name: Wayne Kareigi

def func(a,n,d):
    return a+(n-1)*d

a = 1
d = int(input())
for i in range (1,11):
    n = i
    print(func(a,n,d),end = " ")