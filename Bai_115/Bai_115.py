n=int(input("Enter n:   "))

abb=-1
ab=3
i=2
while i<=n:
    an=5*ab+6*abb
    i+=1
    abb=ab
    ab=an

print("\na_",n,"in the given sequence is: ",an,".\n")
