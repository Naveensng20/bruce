n=int(input())
import statistics
num= [int(x) for x in input().split()] 
print(int(statistics.median(num)))
