with open("_15_dict.txt", "r", encoding="utf-8") as f:
    dict_lines = f.read().splitlines()

with open("_15_word_pairs.txt", "r", encoding="utf-8") as f:
    word_pair_lines = f.read().splitlines()

limord = set()
dict_lines_set = set(dict_lines)

for word_pair in word_pair_lines:
    for dict_word in dict_lines:
        pairs = word_pair.split(",")
        x = pairs[0].strip() + dict_word
        y = dict_word + pairs[1].strip()
        if(x in dict_lines_set and y in dict_lines_set):
            limord.add(dict_word)

counter = 0
for word in limord:
    counter += len(word)

print(counter)
