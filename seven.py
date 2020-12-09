# from urllib.request import urlopen

# url = "https://julekalender-backend.knowit.no/challenges/7/attachments/forest.txt"
# with urlopen(url) as response:
#     heights = response.read().splitlines()

with open("seven.txt", "r", encoding="utf-8") as f:
    heights = f.read().splitlines()

for i in range(len(heights)):
    heights[i] = "  " + str(heights[i]) + "  "

heights.reverse()  # Easier to work with a top-down tree

print("Max height:", len(heights))

starting_positions = []
current_tribe = []
for index, char in enumerate(heights[0]):
    if char == "#":
        current_tribe.append(index)
    else:
        if(len(current_tribe) > 0):
            starting_positions.append(current_tribe)
            current_tribe = []

tribe_indexes = []
for index, tribe in enumerate(starting_positions):
    if(len(tribe) % 2 == 0):
        print("Error: tribe width is an odd number at index", tribe)
        exit()

    tribe_indexes.append(tribe[len(tribe) // 2])


print("Number of trees:", len(tribe_indexes))


def check_tree(tribe_index):
    for h in range(1, len(heights)):
        # print(heights[i])
        branch = 0
        while True:
            branch += 1
            left = heights[h][tribe_index - branch]
            double_left = heights[h][tribe_index - branch - 1]
            right = heights[h][tribe_index + branch]
            double_right = heights[h][tribe_index + branch + 1]

            if(left != right):
                # print("Uneven on {} with branch: {}".format(heights[i][tribe_index - 2: tribe_index + 3], branch))
                return 0

            if(left == " " and double_left == " " and right == " " and double_right == " "):
                # Finished this height
                # print("finished height")
                break

        # This one needs to be at the bottom because the upmost tribe can be asymmetric
        if heights[h][tribe_index] == " ":
            # Reached the top
            return 1

    return 1


counter = 0
for tribe_index in tribe_indexes:
    result = check_tree(tribe_index)
    counter += result

print("Asymmetric trees:", counter)
