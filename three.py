matrix = []
with open("three/matrix.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(line))

with open("three/words.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()

matrix_height = 1000
matrix_width = 1000


def solve_word(word):
    def solve_word_direction(word, start_y, start_x, y_direction, x_direction):
        # print("{} at {}, {}".format(word, start_y, start_x))
        for i in range(2, len(word)):  # Skip first two characters since they are already confirmed
            new_y = start_y + y_direction * i
            new_x = start_x + x_direction * i
            if new_y < 0 or new_y >= matrix_height:
                return False
            if new_x < 0 or new_x >= matrix_width:
                return False
            if not word[i] == matrix[new_y][new_x]:
                return False
        # print("Found {} at {},{} with direction {}, {}".format(
        #     word, start_y, start_x, y_direction, x_direction))
        return True

    for y in range(matrix_height):
        for x in range(matrix_width):
            if word[0] == matrix[y][x]:
                # print("letter {} at {},{}".format(word[0], y, x))
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_y = y + i
                        new_x = x + j
                        if new_y < 0 or new_y >= matrix_height:
                            continue
                        if new_x < 0 or new_x >= matrix_width:
                            continue
                        if word[1] == matrix[new_y][new_x]:
                            solved = solve_word_direction(word, y, x, i, j)
                            if solved:
                                return True
    return False


found_words = []
for word in words:
    solved = solve_word(word)
    if solved:
        # print("Found word:", word)
        found_words.append(word)

print("Number of found words:", len(found_words))
# print("Found words:", found_words)

not_found = list(set(words) - set(found_words))
not_found.sort()
print("Words not found:", not_found)
