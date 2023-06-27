import math

x=int(input("Enter x:   "))
n=int(input("Enter n:   "))

s=0
t=1
i=1
while i<=n:
    t*=x
    s=math.sqrt(t+s)
    i+=1

print("\nS(",x,",",n,") = ",round(s,4),".\n")