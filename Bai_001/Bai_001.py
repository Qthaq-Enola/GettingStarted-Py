import math

print("Enter the first point's coordinate:")
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
print("\nEnter the second point's coordinate:")
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

d=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

print("\nThe distance between the first point and the second one is:  ",round(d,2),".\n")