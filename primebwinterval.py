val=raw_input()
nk=val.split()
val1=int(nk[0])
val2=int(nk[1])
for num in range(val1,val2+1):
	if num>1:
		for i in range(2,num):
			if(num%i==0):
				break
		else:
			print(num),
			
   
