import numpy as np

# ! This solution is not working I think, use eight.py instead

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


# max_x = 0
# max_y = 0
# for location in locations:

times = np.zeros((500, 500))  # may fix later

# 50+: 1
# [20-49]: 0.75
# [5-19]: 0.5
# [1-4]: 0.25
# 0: 0


def adjust_times(santa_x, santa_y):
    for y in range(santa_y - 50, santa_y + 51):
        if(y < 0 or y >= times.shape[0]):
            continue
        for x in range(santa_x - 50, santa_x + 51):
            if(x < 0 or x >= times.shape[1]):
                continue

            diff_x = abs(santa_x - x)
            diff_y = abs(santa_y - y)
            distance = diff_x + diff_y

            if(distance >= 50):
                continue
            elif(distance >= 20):
                times[y, x] -= 0.25
            elif(distance >= 5):
                times[y, x] -= 0.5
            elif(distance >= 1):
                times[y, x] -= 0.75
            else:
                times[y, x] -= 1
            # if(x == santa_x and y == santa_y):
            #     times[y, x] -= 1

            # diff_x = abs(santa_x - x)
            # diff_y = abs(santa_y - y)
            # distance = diff_x + diff_y
            # if(distance <= 5):
            #     times[y, x] -= 0.75
            # elif(distance <= 20):
            #     times[y, x] -= 0.5
            # elif(distance <= 50):
            #     times[y, x] -= 0.25
            # else:
            #     # times[y, x] += 1
            #     continue


x = 0
y = 0
counter = 0
for city in route:
    counter += 1
    print("\r{} of {}".format(counter, len(route)), end="")
    coordinates = locations[city]
    if(coordinates[0] < x):
        for i in range(x - coordinates[0]):
            x -= 1
            times += 1
            adjust_times(x, y)
    else:
        for i in range(coordinates[0] - x):
            x += 1
            times += 1
            adjust_times(x, y)

    if(coordinates[1] < y):
        for i in range(y - coordinates[1]):
            y -= 1
            times += 1
            adjust_times(x, y)
    else:
        for i in range(coordinates[1] - y):
            y += 1
            times += 1
            adjust_times(x, y)

print()

location_times = []
for coordinates in locations.values():
    location_times.append(times[coordinates[1], coordinates[0]])

print(max(location_times) - min(location_times))
