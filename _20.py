from collections import defaultdict


def print_elves(d):
    print()
    for elf in d.values():
        print(elf)


def print_lines(l):
    print()
    for line in l:
        print(line)


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


def prune_elf(elf_to_prune):
    for elf in elves.values():
        if(elf_to_prune.name in elf.children):
            elf.children.remove(elf_to_prune.name)
            elf.children = elf.children.union(elf_to_prune.children)

    del elves[elf_to_prune.name]


print("Pruning managers with 1 child manager...")
changed = True
while changed:
    changed = False
    for key, elf in elves.items():
        if(len(elf.children) == 1):
            c_name = list(elf.children)[0]
            if(len(elves[c_name].children) > 0):
                prune_elf(elf)
                changed = True
                break


# print_lines(lines)

# print_elves(elves)

print("Gathering results...")

managers = []
workers = []
for key, elf in elves.items():
    if(len(elf.children) == 0):
        # workers += 1
        workers.append(key)
    else:
        # managers += 1
        managers.append(key)

# print("Workers", workers)
# print("Managers", managers)
workers = len(workers)
managers = len(managers)
print("Workers: {}, managers: {}, difference: {}".format(
    workers, managers, workers - managers))
