import numpy as np

with open("_17.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

line_len = len(lines[0])
for y, line in enumerate(lines):
    if(len(line) != line_len):
        print("The floor is not a square")
        exit(1)


def get_vacume_coordinates():
    vacume = """  sss
 sssss
sssssss
sssXsss
sssssss
 sssss
  sss  """

    vacume_coordinates = [(0, 0)]
    vacume_center = (3, 3)
    for y, line in enumerate(vacume.splitlines(), start=-vacume_center[0]):
        for x, char in enumerate(line, start=-vacume_center[1]):
            if(char == "s"):
                vacume_coordinates.append((y, x))

    return vacume_coordinates


def get_brush_coordinates():
    brush = """kkk   kkk
kkkkkkkkk
kkkkkkkkk
 kkkkkkk 
 kkkXkkk 
 kkkkkkk 
kkkkkkkkk
kkkkkkkkk
kkk   kkk"""

    # Init list with the "x" value in the center
    brush_center = (4, 4)
    brush_coordinates = [(0, 0)]
    for y, line in enumerate(brush.splitlines(), start=-brush_center[0]):
        for x, char in enumerate(line, start=-brush_center[1]):
            if(char == "k"):
                brush_coordinates.append((y, x))

    return brush_coordinates


"""
0 = "x"
1 = " "
2 = "." cleaned
"""
floor = np.empty((len(lines), len(lines[0])), dtype=int)
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if(char == "x"):
            floor[y, x] = 0
        elif(char == " "):
            floor[y, x] = 1
        else:
            print("Unknown char in floor")
            exit(1)


vacume_coordinates = get_vacume_coordinates()
brush_coordinates = get_brush_coordinates()

print("Cleaning...")
for y in range(floor.shape[0]):
    for x in range(floor.shape[1]):
        if(floor[y, x] == 0):
            continue

        # Check if vacume fits
        fits = True
        for (v_y, v_x) in vacume_coordinates:
            new_y = y + v_y
            new_x = x + v_x
            if(new_y < 0 or new_y >= floor.shape[0] or new_x < 0 or new_x >= floor.shape[1]):
                fits = False
                break
            if(floor[new_y, new_x] == 0):
                fits = False
                break

        if not fits:
            continue

        # Clean surrounding tiles
        for (b_y, b_x) in brush_coordinates:
            new_y = y + b_y
            new_x = x + b_x
            if(new_y < 0 or new_y >= floor.shape[0] or new_x < 0 or new_x >= floor.shape[1]):
                continue

            if(floor[new_y, new_x] == 1):
                floor[new_y, new_x] = 2

counter = 0
for y in range(floor.shape[0]):
    for x in range(floor.shape[1]):
        if(floor[y, x] == 1):
            counter += 1

print(counter)
