#Program to calculate the volume of solids
#Date : 20/02/2024
#Name: Wayne Kareigi
import math

radius_1 = float(input("Enter the radius of the cylinder  : "))
height_1 = float(input("Enter the height of the cylinder  : "))

volume1 = math.pi * radius_1**2 * height_1

print("The volume of the cylinder is ", volume1)


radius_2 = float(input("Enter the radius of the sphere  :  "))
volume2 = 4/3 * math.pi * radius_2**3
print("The volume of the sphere is ", volume2)
