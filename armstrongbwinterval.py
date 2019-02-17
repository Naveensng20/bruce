# your code goes here
a=raw_input()
nk=a.split()
num1=int(nk[0])
num2=int(nk[1]) 
for num in range(num1,num2):
	pow=len(str(num))
	sum=0
	temp=num
	while(temp>0):
		sum=sum+((temp%10)**pow)
		temp=temp//10
	if(sum==num):
		print(num),
		
	

