from collections import defaultdict


class Elf:
    def __init__(self, name):
        self.name = name
        self.found = False
        self.children = set()

    def __str__(self):
        return "{}: {}, {}".format(self.name, self.found, self.children)


with open("_20.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

# lines = ["Athena", "Demeter", "Hades", "Hades🎄Hypnos",
#          "Athena🎄Icarus",
#          "Hades🎄Nyx🎄Zagreus🎄Medusa",
#          "Athena🎄Orpheus",
#          "Athena🎄Icarus🎄Poseidon🎄Cerberus",
#          "Hades🎄Nyx🎄Zagreus",
#          "Athena🎄Icarus🎄Poseidon"]

lines = list(map(lambda x: x.split("🎄"), lines))

elves = dict()

print("Finding elves")

for names in lines:
    for name in names:
        elves[name] = Elf(name)

for names in lines:
    elves[names[-1]].found = True

print("Deleting unfound elves")

to_delete = []
for elf in elves.values():
    if(not elf.found):
        to_delete.append(elf.name)

for name in to_delete:
    del elves[name]

for i, names in enumerate(lines):
    temp_names = []
    for name in names:
        if(name in elves.keys()):
            temp_names.append(name)
    lines[i] = temp_names

print("Counting children...")

for names in lines:
    if(len(names) == 1):
        continue
    for i in range(len(names) - 1):
        elves[names[i]].children.add(names[i + 1])

print("Pruning managers with 1 child manager...")
to_prune = set()
for key, elf in elves.items():
    if(len(elf.children) == 1):
        child_name = list(elf.children)[0]
        if(len(elves[child_name].children) > 0):
            # Prune where the only child is a manager
            to_prune.add(elf.name)

for name in to_prune:
    del elves[name]

print("Gathering results...")

managers = 0
workers = 0
for key, elf in elves.items():
    if(len(elf.children) == 0):
        workers += 1
    else:
        managers += 1

print("Workers: {}, managers: {}, difference: {}".format(
    workers, managers, workers - managers))
