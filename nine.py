import numpy as np

with open("nine.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

cells = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    line = str(line).strip()
    for j, char in enumerate(line):
        if(char == "S"):
            cells[i, j] = 1

# print(cells.shape)

days = 0
while True:
    days += 1
    # print(days)
    new_cells = cells.copy()
    for y in range(cells.shape[0]):
        for x in range(cells.shape[1]):
            if(cells[y, x] == 1):
                continue

            neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            counter = 0
            for i, j in neighbours:
                temp_x = x + i
                temp_y = y + j
                if(temp_y < 0 or temp_y >= cells.shape[0]):
                    continue

                if(temp_x < 0 or temp_x >= cells.shape[1]):
                    continue

                if(i == 0 and j == 0):
                    continue

                if(cells[temp_y, temp_x] == 1):
                    counter += 1

            if(counter >= 2):
                new_cells[y, x] = 1

    if(np.array_equal(cells, new_cells)):
        break

    cells = new_cells.copy()

print("Days:", days)
