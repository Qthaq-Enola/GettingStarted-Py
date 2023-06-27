n=int(input("Enter n:   "))

flag=False
t=n
while t!=0:
    dv=t%10
    if dv%2!=0:
        flag=True
    t=t//10

if flag==True:
    print("\nNumber",n,"have odd digit(s).","\n")
elif flag==False:
    print("\nNumber",n,"doesn't have odd digit(s).","\n")    
