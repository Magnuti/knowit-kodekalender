import numpy as np

number_of_locations = 50

with open("eight.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

# number_of_locations = 2

# with open("eight_test.txt", "r", encoding="utf-8") as f:
#     lines = f.read().splitlines()

route = lines[number_of_locations:]

locations = {}
for city in lines[:number_of_locations]:
    x = city.split(":")
    coordinates = str(x[1]).replace("(", "").replace(")", "").split(",")
    locations[x[0]] = list(map(int, coordinates))

max_x = 0
max_y = 0
for coordinates in locations.values():
    if(coordinates[0] > max_x):
        max_x = coordinates[0]
    if(coordinates[1] > max_y):
        max_y = coordinates[1]

paths_taken = np.zeros((max_y + 1, max_x + 1), dtype=int)
steps = 0
x = 0
y = 0
for city in route:
    coordinates = locations[city]
    if(coordinates[0] < x):
        for i in range(x - coordinates[0]):
            x -= 1
            paths_taken[y, x] += 1
            steps += 1
    else:
        for i in range(coordinates[0] - x):
            x += 1
            paths_taken[y, x] += 1
            steps += 1

    if(coordinates[1] < y):
        for i in range(y - coordinates[1]):
            y -= 1
            paths_taken[y, x] += 1
            steps += 1
    else:
        for i in range(coordinates[1] - y):
            y += 1
            paths_taken[y, x] += 1
            steps += 1

# print(paths_taken)

times = {}
for city, coordinates in locations.items():
    x = coordinates[0]
    y = coordinates[1]
    at_pixel = 0
    pixel_5 = 0
    pixel_20 = 0
    pixel_50 = 0
    for yi in range(y - 50, y + 51):
        if(yi < 0 or yi >= paths_taken.shape[0]):
            continue
        for xi in range(x - 50, x + 51):
            if(xi < 0 or xi >= paths_taken.shape[1]):
                continue

            diff_x = abs(xi - x)
            diff_y = abs(yi - y)
            distance = diff_x + diff_y
            # print(distance)
            if(distance >= 50):
                continue
            elif(distance >= 20):
                pixel_50 += paths_taken[yi, xi]
            elif(distance >= 5):
                pixel_20 += paths_taken[yi, xi]
            elif(distance >= 1):
                pixel_5 += paths_taken[yi, xi]
            else:
                at_pixel += paths_taken[yi, xi]

    # print(at_pixel, pixel_5, pixel_20, pixel_50)

    time_to_subtract = at_pixel + pixel_5 * 0.75 + pixel_20 * 0.5 + pixel_50 * 0.25
    times[city] = steps - time_to_subtract

# print(times)

print(max(times.values()) - min(times.values()))
