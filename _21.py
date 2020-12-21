with open("_21.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

queues = [[] for i in range(5)]


def pop_queue():
    for queue in queues:
        if(len(queue) > 0):
            name = queue.pop(0)
            if(name == "Claus"):
                return True
            return False


counter = 0
for line in lines:
    if(line == "---"):
        if(pop_queue()):
            break
        counter += 1
    else:
        x = line.split(",")
        priority = int(x[1]) - 1
        queues[priority].append(x[0])
    # print(queues)


print(counter)
