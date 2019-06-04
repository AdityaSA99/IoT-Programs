#Multiplication Tables
a = int(input("Input number of tables : "))
b = int(input("Input the start : "))
for i in range(b,a+1):
	print("Table of %d is :"%b)
	for j in range(1,11):
		print(("{0} * {1} = {2}").format(b,j,b*j))
	b+=1