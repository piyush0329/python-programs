num=int(input("enter how many rows you want to print:"))
print("enter 1 or 0")
bool_val=input("1 for true 0 for false:")
if bool_val=="1":
	for i in range(0,num+1):
		print("@"*i)
if bool_val=="0":
	for i in range(num,0,-1):
		print("@"*i)		