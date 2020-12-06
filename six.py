number_of_elves = 127

with open("six.txt", "r", encoding="utf-8") as f:
    text = f.read()
    candy_list = list(map(int, text.split(",")))
# x = "10,14,14,13,13,13,15,14,11,15,11"
# candy_list = list(map(lambda x: int(x), x.split(",")))

for i in range(len(candy_list), 0, -1):
    candy_count = sum(candy_list[:i])
    if(candy_count % number_of_elves == 0):
        print(candy_count / number_of_elves)
        break
