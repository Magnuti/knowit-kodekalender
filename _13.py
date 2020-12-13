from collections import Counter

with open("_13.txt", "r", encoding="utf-8") as f:
    line = f.read().splitlines()[0]

out = []
counts = Counter()
offset = ord("a")
for char in line:
    counts[char] += 1
    if(counts[char] == ord(char) + 1 - offset):
        out.append(char)

print("".join(out))
