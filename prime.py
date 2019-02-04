num=int(input())
if((num>0) and (num!=2)):
	if((num%2==0) or (num%3==0) or(num%5==0)):
		print("no")
	else:
		print("yes")
else:
	print("yes")
