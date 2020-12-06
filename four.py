with open("four.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

sukker = "sukker"
mel = "mel"
melk = "melk"
egg = "egg"

food = {sukker: 0, mel: 0, melk: 0, egg: 0}

for line in lines:
    elements = line.split(",")
    for e in elements:
        x = e.split(":")
        key = x[0].strip()
        value = int(x[1])
        food[key] += value

print(food)

count_sukker = food[sukker] // 2
count_mel = food[mel] // 3
count_melk = food[melk] // 3
count_egg = food[egg] // 1

print(min(count_sukker, count_mel, count_melk, count_egg))
