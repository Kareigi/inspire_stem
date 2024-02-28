#Using dictionaries describe your fav car, print values ,keys
#Copy into another dictionary
#Date :28/02/2024
#Name :Wayne Kareigi

fav_car = {"make":"Rolls-Royce Cullinan ", "colour":"Blue","engine":"V12","body style":
           "luxury SUV", "interior":"leather"}
print(fav_car)

friends_car = fav_car.copy
print(friends_car)

for key,values in fav_car.items():
    print("\t")
    print(key)
    print(values)


