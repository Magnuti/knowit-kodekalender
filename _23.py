from collections import defaultdict
from math import floor

vocals = set("aeiouyæøå")

with open("_23_words.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

grunnord = {}
for line in lines:
    x = line.split(" ")
    grunnord[x[0]] = int(x[1])

with open("_23_rap_battle.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()


def stripped_word(word):
    sw = word.replace("jule", "")
    if(sw not in grunnord.keys()):
        print(word, "is not valid")
        exit(1)

    return sw


def calculate_word_value(i, word, words):
    word_without_jule = stripped_word(word)
    g = grunnord[word_without_jule]

    def vocal_bonus():
        if(i == 0):
            return 0

        def count_vocals(word):
            counter = 0
            for char in word:
                if(char in vocals):
                    counter += 1
            return counter

        first = count_vocals(words[i - 1])
        second = count_vocals(word)
        if(first >= second):
            return 0

        diff = second - first
        if("jule" in word):
            diff *= 2

        return diff

    def repetisjonsdivisor():
        score = 1
        reversed_words_sublist = words[:i]
        reversed_words_sublist = reversed_words_sublist[::-1]
        for k in range(0, i):
            if(stripped_word(reversed_words_sublist[k]) == word_without_jule):
                score += 1
            else:
                break

        return score

    v = vocal_bonus()
    r = repetisjonsdivisor()

    word_score = floor((g + v) / r)
    return word_score


champs = defaultdict(lambda: 0, {})
for line in lines:
    x = line.split(": ")
    name = x[0]
    words = x[1].split(" ")

    score = 0
    for i, word in enumerate(words):
        score += calculate_word_value(i, word, words)

    # print("Total", score)
    champs[name] += score

print("Result:")
for key, value in champs.items():
    print(key, ":", value)
