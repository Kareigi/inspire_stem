#Program that prints odd and even numbers
#Date :28/02/2024
#Name :Wayne Kareigi

#Printing odd numbers
def print_odds ():
    for x in range (1,101):
        if x % 2 != 0:
            print(x)

print_odds ()           

#printing even nummbers
def print_even():
    for y in range (1,102):
        if y % 2 == 0:
            print(y)
print("\t")
print_even()


       
