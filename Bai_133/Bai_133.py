x=float(input("Enter x:   "))
y=float(input("Enter y:   "))
z=float(input("Enter z:   "))

if ((x+y>z)and(y+z>x)and(z+x>y)):
    if ((x==y)and(y==z)):
        print("\nThe inputted sides create an equilateral triangle.")
    else:
        if((x*x==y*y+z*z)or(y*y==x*x+z*z)or(z*z==x*x+y*y)):
            if((x==y)or(y==z)or(x==z)):
                print("\nThe inputted sides create an isosceles right triangle.")
            else:
                print("\nThe inputted sides create a right triangle.")
        else:
            if((x==y)or(y==z)or(x==z)):
                print("\nThe inputted sides create an isosceles triangle.")
            else:
                print("\nThe inputted sides create a normal triangle.")
else:
    print("\nThe inputted sides can't create a triangle.")
print("\n")
