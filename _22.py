with open("_22.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

# lines = ["llmnmgimnaaiechhchajghefgjkudri [Michael, Guri, Aksel]"]


def find_name(random_letters, name):
    index = 0
    for char in random_letters:
        if(char == name[index]):
            index += 1
            if(index >= len(name)):
                return True

    return False


def remove_name_from_letters(random_letters, name):
    i = 0
    temp_letters = ""
    for char in random_letters:
        if(i < len(name) and char == name[i]):
            i += 1
        else:
            temp_letters += char

    return temp_letters


counters = []
for line in lines:
    split_index = line.find(" ")
    random_letters = line[:split_index]
    names_string = line[split_index + 1:]
    names_string = names_string[1:-1]  # Removes "[" and "]"
    names = names_string.split(",")
    names = list(map(lambda x: x.lower().strip(), names))

    counter = 0
    for name in names:
        success = find_name(random_letters, name)
        if(success):
            counter += 1
            random_letters = remove_name_from_letters(random_letters, name)

    counters.append(counter)

print("Max at", counters.index(max(counters)), "with value of", max(counters))
