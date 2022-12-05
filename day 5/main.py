file = open("input.txt", "r").read().splitlines()

towers: list[list[str]] = [] 

state = 0

from typing import NamedTuple

Command = NamedTuple("Command", [("amount", int), ("from_amount", int), ("to_amount", int)])

commands: list[Command] = []

# read in until empty newline
for line in file:
    if state == 0 and line[1] == "1":
        state+=1
    elif state == 0:
        pos = 1
        length = int(((len(line) + 1) / 4))
        if len(towers) < length:
            diff = length - len(towers)
            for i in range(diff):
                towers.append([])
        
        while pos < len(line):
            if line[pos] != "" and line[pos] != ' ':
                towers[int((pos - 1) / 4)].append(line[pos])
            pos += 4
    elif line.startswith("move"):
        amount, other = line.split(" from ")
        amount = amount[4:]
        from_amount, to_amount = other.split(" to ")
        commands.append(Command(int(amount), int(from_amount), int(to_amount)))

for i in range(len(towers)):
    towers[i] = towers[i][::-1]

# why does python have to be painful here with referencing
towers_backup = [tower.copy() for tower in towers]

# part 1
for command in commands:
    for i in range(command.amount):
        moving = towers[command.from_amount - 1].pop()
        towers[command.to_amount - 1].append(moving)

ends = "".join([tower[-1] for tower in towers])
for command in commands:
    buffer = []
    for i in range(command.amount):
        buffer.append(towers_backup[command.from_amount - 1].pop())
    buffer.reverse()
    for item in buffer:
        towers_backup[command.to_amount - 1].append(item)

ends = "".join([tower[-1] for tower in towers_backup])
print(ends)