val=int(input())
sum=0
while(val>0):
	num=val%10
	tot=num**2
	sum=sum+tot
	val=val//10
print(sum)
