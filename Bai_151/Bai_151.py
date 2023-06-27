n=int(input("Enter n:   "))

flag=True
t=n
while t>1:
    r=t%2
    if r!=0:
        flag=False
    t//=2
if flag==True:
    print("\nThe inputted number is 2^m's form.")
else:
    print("\nThe inputted number isn't 2^m's form.")
print("\n")
