# Strings in python
#Date :22/02/2024
#Name :Wayne Kareigi

city = "nairobi"
print(city[0]) #n
print(city[1])#a
print(city[2])#i
print(city[3])#r
print(city[4])#o
print(city[-1])#b
print(city[-2])#i
#convert to uppercase
print(city)
print("\n") #Creates a new line
print(city.upper())

name = "WAYNE KAREIGI"
print(name)
print("\n")
print(name.lower()) #Converts upper to lower case

town = "       Naivasha      "
print(town)
print("\t") #creates new tab
print(town.strip())

#add two strings

f_name= "Wayne"
s_name = "Kareigi"

full_name = f_name + s_name
print(full_name)


#write a program that reverses a string
#write a program that detects a palindrome

#Replacing a character
fruit= "orangeooooo"
print(fruit.replace('o','y'))

subject = "physical,sciences"
print(subject.split(","))

age = 30
height = 1.75
print("I am {0}years old and {1}metres tall ". format(age,height))