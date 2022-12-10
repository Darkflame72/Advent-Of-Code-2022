file = open("test.txt").read().splitlines()
file = open("input.txt").read().splitlines()

cycles = (20, 60, 100, 140, 180, 220)
cycle_scores = []

screen = [' ' for _ in range(240)]

cycle = 0
x = 1

for line in file:
    action = line.strip()
    amount = 0
    if action == "noop":
        pass
    else:
        amount = int(action.split(" ")[1])

    cycle += 1
    c = int((cycle) % 40)
    if c >= x and c <= x + 2:
        screen[cycle-1] = '#'

    if cycle in cycles:
        cycle_scores.append(cycle * x)
    

    if amount != 0:
        cycle += 1
        c = int((cycle) % 40)
        if c >= x and c <= x + 2:
            screen[cycle-1] = '#'
        if cycle in cycles:
            cycle_scores.append(cycle * x)
        x += amount

print(cycle_scores)
print(sum(cycle_scores))

print()
for i in range(6):
    print("".join(screen[i*40:(i+1)*40]))
