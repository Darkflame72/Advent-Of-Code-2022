file = open("input.txt")
scores = []
buffer = 0
for line in file:
    if line == "\n":
        scores.append(buffer)
        buffer = 0
    else:
        buffer += int(line.strip())

scores.append(buffer)

# get top 3 scores
top3 = sum(sorted(scores, reverse=True)[:3])
print(top3)