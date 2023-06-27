x=int(input("Enter x:   "))
n=int(input("Enter n:   "))

s=-1
t=1
m=1
i=2
d=1
while i<=2*n:
    t*=x**2
    m*=i*(i-1)
    s+=d*t/m
    i+=2
    d=-d

print("\nS(",x,",",n,") = ",round(s,4),".\n")
