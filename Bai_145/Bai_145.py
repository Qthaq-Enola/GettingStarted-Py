n=int(input("Enter n:   "))

flag=False
i=0
while i<=n:
    if i*i==n:
        flag=True
    i=i+1
if flag==True:
    print("\nThe inputted number is a perfect number.")
else:
    print("\nThe inputted number isn't a perfect number.")
print("\n")
