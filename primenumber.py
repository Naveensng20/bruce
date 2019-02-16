NUM=int(raw_input())
if NUM > 1:
   for i in range(2,NUM):
       if (NUM % i) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
