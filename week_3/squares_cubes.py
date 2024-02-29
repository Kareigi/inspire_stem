#A program that prints all squares ,cubes of no. btw 1 and 10
#Date :29/02/2024
#Name :Wayne Kareigi

#squares of numbers btw 1 to 10
def square_nums(first_no,last_no):
    for i in range (first_no,last_no+1):
        z= (i **2)
        print(z)
square_nums(1,10)       


#cubes of numbers btw 1 to 10
def cube_nums(first_no,last_no):
    for i in range (first_no,last_no+1):
        z= (i **3)
        print(z)
print("\t")        
cube_nums(1,10)       


