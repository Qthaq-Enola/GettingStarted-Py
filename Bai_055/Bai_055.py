n=int(input("Enter n:   "))

t=1
i=1
while i<=n:
    if n%i==0:
        t=t*i
    i=i+2

print("Multiplication of odd divisors of n is:  ",t,"")
