n=int(input("Enter n:   "))

s=0
i=1
while(i<=(2*n+1)):
    s=s+(1/i)
    i=i+2

print("S(",n,") = ",round(s,4),".\n")