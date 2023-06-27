x=int(input("Enter x:   "))
n=int(input("Enter n:   "))

s=0
t=1
i=1
d=1
while i<=n:
    t*=x
    s+=d*t
    i+=1
    d=-d

print("\nS(",x,",",n,") = ",s,".\n")