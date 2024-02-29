#A program that generates prime numbers between two set numbers
#Date :29/02/2024
#Name :Wayne Kareigi
first_no = 1
sec_no = 99
print ("Prime numbers between {0} and {1} are :".format(first_no , sec_no))

def print_primes():
   
    for num in range (first_no,sec_no + 1):
         if num >1 :
            for i in range (2,num):
             if num % i == 0 :
                break
            else:
               print(num)

print_primes()                

