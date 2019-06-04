#Multiplication Tables
a = int(input("Input the number : "))
for i in range(1,11):
	print(("{0} * {1} = {2}").format(a,i,a*i))