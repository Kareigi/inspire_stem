# A program that creates a simple multiplication table
#Date :22/02/2024
#Name :Wayne Kareigi


#column headers
for x in range (1,10):
    print ("{:4})" .format(x),end= "") #{:4}shows that the minimum width is 4 characters
    print()

#table body
for y in range (1,10):

 #row header
    print ("{:2} |".format (y),end ="") #{:2}--> row has a width of 2 characters

#products for the table
for y in range (1,10): 
    product = (x * y)
    print("{:4}".format(product),end = "")
    print()

        

