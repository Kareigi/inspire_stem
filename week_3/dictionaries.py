#dictionaries are mutable
##Date :28/02/2024
#Name :Wayne Kareigi

my_laptop = {"Make":"lenovo","Colour":"black", "Year obtained ":"2023", 
             "Weight":"1.2kg"}


print (my_laptop["Make"])
print (my_laptop["Colour"])
print (my_laptop["Weight"])

#changing the values in a dictionary
my_laptop["Colour"] = "red"
my_laptop["size"] = "1200mm x 600mm"

print(my_laptop)

del my_laptop["Colour"] #deleting items in a dictionary
print(my_laptop)

siz_laptop = my_laptop.copy
print(siz_laptop)

for key,value in my_laptop.items():
    print("\t")
    print(key)
 
    print(value)

#data type summary
#integers
#FloatingPoint
#complex
#lists
#tuples
#dictionaries    



     