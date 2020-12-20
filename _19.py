from collections import defaultdict, deque

with open("_19.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

# lines = ["1 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]",
#          "2 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]",
#          "3 3 [Jenny, Alvin, Greger, Petra, Olaug]",
#          "4 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]"]

elf_victories = defaultdict(lambda: 0, {})

for line in lines:
    x = line.split(" ")
    rule = int(x[0])
    steps = int(x[1])

    # Remove "[" and "]"
    x[2] = x[2][1:]
    x[-1] = x[-1][:-1]

    elves = x[2:]
    elves = list(map(lambda x: x.replace(",", ""), elves))

    index_counter = 0
    while(len(elves) > 1):
        elves = deque(elves)
        elves.rotate(steps)
        elves = list(elves)

        if(rule == 1):
            del elves[0]
        elif(rule == 2):
            del elves[index_counter]
            index_counter += 1
            if(index_counter >= len(elves)):
                index_counter = 0
        elif(rule == 3):
            if(len(elves) == 2):
                del elves[0]
            else:
                middle = len(elves) // 2
                if(len(elves) % 2 == 0):
                    del elves[middle - 1: middle + 1]
                else:
                    del elves[middle]
        else:
            del elves[-1]

    elf_victories[elves[0]] += 1


max_value = 0
max_key = ""
for key, value in elf_victories.items():
    if(value > max_value):
        max_value = value
        max_key = key

print(max_key, max_value)
