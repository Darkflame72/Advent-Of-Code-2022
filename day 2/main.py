file = open("input-2.txt")

scores = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}

bonus_score = {"X": 1, "Y": 2, "Z": 3}

score = 0

for line in file:
    # remove all whitespace
    line = line.strip()
    line = line.replace(" ", "")
    score += scores[line]
    score += bonus_score[line[1]]
print(score)

score = 0
for line in file:
    line = line.strip()
    line = line.replace(" ", "")
    condition = line[1]
    added_score = 0
    if condition == "X":
        added_score += 0
    elif condition == "Y":
        added_score += 3
    else:
        added_score += 6

    key = [k for k, v in scores.items() if k.startswith(line[0]) and v == added_score][0]
    score += scores[key]
    score += bonus_score[key[1]]


print(score)
    
    
