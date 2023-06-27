x=int(input("Enter x:   "))
n=int(input("Enter n:   "))

s=0
t=1
m=0
i=1
while i<=n:
    t*=x
    m+=i
    s+=(t/m)
    i+=1

print("\nS(",x,",",n,") = ",round(s,4),".\n")
