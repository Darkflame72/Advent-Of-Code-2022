file = open("test.txt").read().splitlines()
file = open("input.txt").read().splitlines()

# turn into array of array of ints
trees = [list(map(int, list(line))) for line in file]
visible = [[False for _ in line] for line in file]

# make top line 
for i in range(len(trees[0])):
    visible[0][i] = True

# make left column
for i in range(len(trees)):
    visible[i][0] = True

# make right column
for i in range(len(trees)):
    visible[i][-1] = True

# make bottom line
for i in range(len(trees[-1])):
    visible[-1][i] = True

# go through left to right and make visible if number is bigger then any beforehand
for i in range(len(trees)):
    for j in range(1, len(trees[i])):
        if trees[i][j] > max(trees[i][:j]):
            visible[i][j] = True

# go through right to left and make visible if number is bigger then any beforehand
for i in range(len(trees)):
    for j in range(len(trees[i])-2, -1, -1):
        if trees[i][j] > max(trees[i][j+1:]):
            visible[i][j] = True

# go through top to bottom and make visible if number is bigger then any beforehand
for i in range(len(trees[0])):
    for j in range(1, len(trees)):
        if trees[j][i] > max([line[i] for line in trees[:j]]):
            visible[j][i] = True

# go through bottom to top and make visible if number is bigger then any beforehand
for i in range(len(trees[0])):
    for j in range(len(trees)-2, -1, -1):
        if trees[j][i] > max([line[i] for line in trees[j+1:]]):
            visible[j][i] = True


print(sum([sum(line) for line in visible]))

scores = visible = [[0 for _ in line] for line in file]

def get_score(x, y):
    # get amount of visible trees
    total_score = 1
    score = 0
    # go from that tree to the top
    for i in range(y-1, -1, -1):
        if trees[i][x] < trees[y][x]:
            score += 1
        else:
            score += 1
            break
    # print(score)
    
    if score>0:
        total_score *= score


    score = 0
    # go from that tree to the left
    for i in range(x-1, -1, -1):
        if trees[y][i] < trees[y][x]:
            score += 1
        else:
            score += 1
            # print(trees[y][i])
            break
    # print(score)

    if score>0:
        total_score *= score
    
    
    score = 0
    # go from that tree to the right
    for i in range(x+1, len(trees[y])):
        if trees[y][i] < trees[y][x]:
            score += 1
        else:
            score += 1
            break
    # print(score)

    if score>0:
        total_score *= score
    
    
    score = 0
    # go from that tree to the bottom
    for i in range(y+1, len(trees)):
        if trees[i][x] < trees[y][x]:
            score += 1
        else:
            score += 1
            break
    # print(score)
    
    if score>0:
        total_score *= score

    return total_score

for i in range(len(trees)):
    for j in range(len(trees[i])):
        scores[i][j] = get_score(j, i)

print(scores)
print(max([max(line) for line in scores]))
# print(get_score(1, 1)) # 1
# print(get_score(2, 1)) # 4
# print(get_score(2, 3)) # 8