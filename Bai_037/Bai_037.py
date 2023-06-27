n=int(input("Enter n:   "))

s=0
i=1
while(i<=n):
    s=s+pow(i,3)
    i=i+1

print("\nS(",n,") = ",round(s,4),".\n")