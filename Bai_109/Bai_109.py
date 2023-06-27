euler=1
m=1
e=1
i=1
while e>=10**-6:
    m*=i
    euler=1/m
    s+=e
    i+=1

print("\nEuler constant e = ",round(euler,6),".\n")
