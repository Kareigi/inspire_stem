

friends = ["Bree","Renish","Michael","Faith","Joel"]
for friend in friends :
    print(friend)


enemies = friends[:]  #to copy one list into another
for enemy in enemies :
    print("\t")
    print(enemy)

fruits = ["melon","pineapples", "oranges", "grapes","apples","strawberries"]  

#slce th list to get part of the list
print(fruits[0:3])

del fruits[0]
print(fruits)

squares =[] #initializes an empty list
for x in range(0,11):
    squares.append(x**2)
    
print(squares)




