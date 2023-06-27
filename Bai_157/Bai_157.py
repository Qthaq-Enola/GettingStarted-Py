n = int(input("Enter n: "))

s = 0
i = 1
sequence = "\nThe sequence a.1 to a.n is: "
while i <= n:
    s += 1 / i
    sequence += str(round(s,4)) + " "
    i += 1

print(sequence)