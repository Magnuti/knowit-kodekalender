# hint = "juletre"
password = "eamqia"

with open("eleven.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

hints = []
for hint in lines:
    rows = [hint]

    x = hint
    for _ in range(len(hint) - 1):
        y = []
        for char in x[1:]:
            y.append(chr(ord(char) + 1))

        z = []
        for i, char in enumerate(y):
            c = (ord(y[i]) - 97 + ord(x[i]) - 97) % 26
            c += 97
            z.append(chr(c))

        new_string = "".join(z)
        x = new_string
        rows.append(new_string)

    columns = []
    for j in range(len(rows[0])):
        x = []
        for i in range(len(rows)):
            if(j >= len(rows[i])):
                continue
            x.append(rows[i][j])

        columns.append("".join(x))

    for x in columns:
        if(password in x):
            # print(x)
            hints.append(hint)

print(hints)
