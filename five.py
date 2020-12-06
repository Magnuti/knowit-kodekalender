# import matplotlib.pyplot as plt
# import numpy as np

with open("five.txt", "r", encoding="utf-8") as f:
    text = f.read()

# text = "HHHHHHOOOOVVNNNVVOVVNN"

# area_dim = 50
# area = np.zeros((area_dim, area_dim))

# x = area_dim // 2
# y = area_dim // 2


# for char in text:
#     new_x = 0
#     new_y = 0
#     if char == "H":
#         new_x = 3
#     elif char == "V":
#         new_x = -3
#     elif char == "O":
#         new_y = -3
#     elif char == "N":
#         new_y = 3
#     else:
#         print("Unknown direction char:", char)

#     print(new_x)
#     print(new_y)
#     for i in range(new_y):
#         area[y + new_y, x] = 0.2
#     for j in range(new_x):
#         area[y, x + new_x] = 0.2

#     x += new_x
#     y += new_y

#     area[y, x] = 1
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j == 0:
#                 continue
#             area[y + i, x + j] = 0.5

#     break # !

# plt.imshow(area)
# plt.show()

coordinates = [(0, 0)]
current_x = 0
current_y = 0
for char in text:
    if char == "H":
        current_x += 1
    elif char == "V":
        current_x -= 1
    elif char == "O":
        current_y -= 1
    elif char == "N":
        current_y += 1
    else:
        print("Unknown direction char:", char)

    coordinates.append((current_x, current_y))

# Area algorithm taken from https://web.archive.org/web/20100405070507/http://valis.cs.uiuc.edu/~sariel/research/CG/compgeom/msg00831.html
# found on https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
# or explained better here https://www.mathopenref.com/coordpolygonarea2.html
# it is a result of Green's theorem: https://en.wikipedia.org/wiki/Green's_theorem#Area_Calculation
area = 0
for i in range(len(coordinates)):
    j = (i + 1) % len(coordinates)
    area += coordinates[i][0] * coordinates[j][1]
    area -= coordinates[i][1] * coordinates[j][0]
area = abs(area) / 2

print(area)
