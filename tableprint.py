num = int(input("Enter a number for which you want table of: "))
print("Table of", num, "is:")
i = 1
while i < 11:
	table = num*i
	print(f"{num} x {i} = {table}")
	i+=1