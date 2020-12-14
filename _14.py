import csv

sequence = [0, 1]
found_set = {0, 1}

# for i in range(2, 16):
for i in range(2, 1800813):
    x = sequence[i - 2] - i
    if(x < 0 or x in found_set):
        x = sequence[i - 2] + i
    sequence.append(x)
    found_set.add(x)

with open("first_million_primes.csv", newline="") as f:
    reader = csv.reader(f)
    primes = list(reader)

primes = primes[0]
primes = list(map(int, primes))

if(max(sequence) > max(primes)):
    print("Not enough primes!")
    exit(1)

prime_counter = 0
primes_set = set(primes)  # Make it into a set to get the O(1) search time
for number in sequence:
    if(number in primes_set):
        prime_counter += 1

print(prime_counter)
