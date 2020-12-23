import csv
from math import sqrt, floor
import time

# No efficient algorithm found until this day I believe. Bruteforce to sqrt(n) for each n.
# https://stackoverflow.com/questions/26753839/efficiently-getting-all-divisors-of-a-given-number
# https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/

n = 1000000
# n = 25

with open("first_million_primes.csv", newline="") as f:
    reader = csv.reader(f)
    primes = set(map(int, list(reader)[0]))

start = time.time()

factors = dict()
# counters = dict()
for n in range(2, n):
    # print("---", n, "-----")
    factors[n] = {1, n}
    if(n in primes):
        continue

    # counters[n] = 1 + n

    for i in range(2, floor(sqrt(n)) + 1):
        if(n % i == 0):
            # Since if 100/25 works, then 100/4 works -> (4, 25) are pairs
            factors[n].add(i)
            # counters[n] += i
            i_pair = int(n / i)
            if(i_pair != i):
                factors[n].add(i_pair)
                # counters[n] += i_pair


print("Calculating counter...")
counter = 0
for key, value in factors.items():
# for key, value in counters.items():
    s = sum(value)
    # s = value
    k = 2 * key
    if(s > k):
        diff = s - k
        if(sqrt(s - k).is_integer()):
            counter += 1

print(time.time() - start)


print(counter)
