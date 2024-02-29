#Date :29/02/2024
#Name :Wayne Kareigi

#defining the function
def print_name():
    print("My name is Wayne Kareigi") 

#calling the function
print_name()    
print_name()
print_name()

def print_details(name,age,id,gender):
    print("I am {0} , {1}years old . My id no. is {2} and gender is {3}" .format(name,age,id,gender))


print_details("Wayne karigi", "17","22977331", "male")    
print_details("John Kamau", "50","509877331", "male")  


def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)
print(sum_nums(6,5))

def prod_nums(x,y):
    return x * y

print(prod_nums(6,5))


def print_odds(first_num,last_num):
    for i in range (first_num,last_num):
        print(i%2 + 1)
print_odds(0,17)        


