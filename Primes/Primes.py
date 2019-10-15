
positions = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    positions.append(n)

limit = max(positions)
prime = 2
count = 0
primeArray = []

while count < limit:

    i = 0
    while i < len(primeArray):
        if not (prime % primeArray[i]):
            break
        i = i+1

    if i == len(primeArray):
        primeArray.append(prime)
        count = count + 1

    prime = prime + 1

for position in positions:
    print(primeArray[position - 1])
