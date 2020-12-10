with open("ten.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

scores = {}

for line in lines:
    names = line.split(",")
    participants = len(names)
    for index, name in enumerate(names):
        if(name in scores):
            scores[name] += participants - (index + 1)
        else:
            scores[name] = participants - (index + 1)
    
winner = ""
points = 0
for key, value in scores.items():
    if(value > points):
        points = value
        winner = key

print("{}-{}".format(winner, points))
