n=int(input("Enter n:   "))

s=0
t=1
i=1
while i<=n:
    t*=i
    s+=i*t
    i+=1

print("\nS(",n,") = ",s,".\n")
