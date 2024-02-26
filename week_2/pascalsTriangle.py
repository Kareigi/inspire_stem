#creating pascal's triangle using loops
#Date :22/02/2024
#Name :Wayne Kareigi

# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
	for j in range(n-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()
