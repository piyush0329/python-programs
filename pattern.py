n=int(input("enter a no:"))
a=int(input("enter your boolean no:"))
if(bool(a)):
	for i in range(1,n+1):
		for j in range(1,i+1):
			 print("*",end="")
		print()

else:
	for i in range(1,n+1):
			for j in range(1,n+2-i):
				print("*",end="")
			print()
			
			