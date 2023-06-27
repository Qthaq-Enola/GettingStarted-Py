n=int(input("Enter n:   "))

abb=1
ab=1
i=2
while i<=n:
    an=ab+abb
    i+=1
    abb=ab
    ab=an

print("\na_",n,"in the Fibonacci sequence is: ",an,".\n")
