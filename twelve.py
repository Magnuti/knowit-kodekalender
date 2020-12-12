with open("twelve.txt", "r", encoding="utf-8") as f:
    line = f.read().splitlines()[0]

# line = "Alvor (Alv Alf Alvaro (Halfrid Halvar Halvard (Alvilde Alva (Alfie Alvor Joralv) Alfonse)) Calvin (Tjalve Alvbert Alvard))"

elements = []
current = []
for char in line:
    if(char == "(" or char == ")"):
        siblings = "".join(current).strip()
        siblings = siblings.split(" ")
        elements.append(siblings)
        elements.append(char)
        current = []
    else:
        current.append(char)

elements_fixed = []
for inner_list in elements:
    if(inner_list[0] != ""):
        elements_fixed.append(inner_list)

depth_values = {}
current_depth = 0
temp = []
for i, value in enumerate(elements_fixed):
    if(value == "("):
        current_depth += 1
    elif(value == ")"):
        current_depth -= 1
    else:
        if(current_depth in depth_values):
            depth_values[current_depth] += len(value)
        else:
            depth_values[current_depth] = len(value)

max_key = 0
max_value = 0
for key, value in depth_values.items():
    if(value > max_value):
        max_value = value
        max_key = key

print("Found max value of {} at generation {}".format(max_value, max_key))
