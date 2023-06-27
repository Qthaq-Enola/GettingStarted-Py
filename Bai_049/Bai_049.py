n = int(input("Enter n: "))

i = 1
divisors = []
while i <= n:
    if n % i == 0:
        divisors.append(i)
    i = i + 1

print("Divisors list of n:  ", end="")
for divisor in divisors:
    print(divisor, end="    ")
print(".\n")