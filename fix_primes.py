import csv

with open("first_million_primes_raw.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

lines = lines[4:]

primes = []
for line in lines:
    for prime in line.split():
        primes.append(prime)

with open("first_million_primes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(primes)
