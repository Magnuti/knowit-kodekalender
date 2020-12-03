with open("one.txt", "r") as f:
    content = f.read()
    numbers = content.split(",")

numbers = list(map(lambda x: int(x), numbers))
numbers.sort()

for i in range(1, 100001):
    if not numbers[i - 1] == i:
        print(i)
        break
