with open("_18.txt", encoding="utf-8") as f:
    words = f.read().splitlines()

# words = ["gnisning", "kake", "kauka",
#          "regninger", "baluba", "tarotkorta", "epoke", "aka"]


def check_word(word):
    # print(word)
    if(word == word[::-1]):
        return True

    if(word[0] == word[-1]):
        return check_word(word[1:-1])

    if(word[0] == word[-2] and word[1] == word[-1]):
        return check_word(word[2:-2])

    return False


found_words = []
counter = 0
for word in words:
    if(word == word[::-1] or len(word) <= 2):
        continue

    success = check_word(word)
    if(success):
        found_words.append(word)

# print(found_words)
print(len(found_words))
