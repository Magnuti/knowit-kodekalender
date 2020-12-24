with open("_24.txt", encoding="utf-8") as f:
    line = f.read().splitlines()[0]

print(len(line))

steps = 0
food = 10
for char in line:
    steps += 1
    food -= 1
    if(char == "1"):
        food += 2
    if(food == 0):
        break
print(steps)
