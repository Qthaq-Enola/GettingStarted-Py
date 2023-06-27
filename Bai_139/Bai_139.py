print("Equation ax+b = 0")
a=int(input("Enter a:   "))
b=int(input("Enter b:   "))

if a==0:
    if(b==0):
        print("\nEquation have infinitely many roots.")
    else:
        print("\nThe equation has no solution.")
else:
    x=-b/a
    print("\nThe equation's root is:  ",x,".")
print("\n")