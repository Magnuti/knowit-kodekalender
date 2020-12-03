primes = []  # index, prime number, interval to previous prime
with open("primes_to_6_million.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        x = line.split(",")
        primes.append(int(x[1]))
        # primes.append(list(map(lambda x: int(x), x)))

package_count = 0
primes_iter = iter(primes)
x = next(primes_iter)
to_skip = 0
for i in range(5433000):
    if to_skip > 0:
        to_skip -= 1
        continue
    if "7" in str(i):
        while x <= i:
            prev = x
            x = next(primes_iter)
        to_skip = prev
        continue
    package_count += 1

print(package_count)
