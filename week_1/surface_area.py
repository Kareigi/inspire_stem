#Program that gets the surface area of shapes
#Date : 20/02/2024
#Name: Wayne Kareigi

import math
radius_1 = float(input("Enter the radius of the cylinder : "))
height_1 = float(input("Enter the height of the cylinder :  "))

surface_area1 = 2 * math.pi * radius_1 * (radius_1 + height_1)
print ("The surface area of the cyinder is ",surface_area1)



radius_2 = float(input("Enter the radius of the sphere : "))

surface_area2 = 4 * math.pi * radius_2**2

print("The surface area of the sphere is", surface_area2)
