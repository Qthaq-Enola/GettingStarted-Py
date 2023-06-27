n=int(input("Enter n:   "))

count=0
t=n
while t != 0:
    dv=t % 10
    if dv%2 != 0:
        count=count+1
    t=t//10

print("\nThe number of odd digits in n is:    ",count,".\n")