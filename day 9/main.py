file = open("test.txt").read().splitlines()
file = open("input.txt").read().splitlines()

field = [['.' for _ in range(10)] for _ in range(10)]
visited = [['.' for _ in range(10)] for _ in range(10)]
visited[4][0] = "#"

snake_pos = [[4, 0] for _ in range(10)]

steps = []

def display_board(field_copy):
    for row in field_copy:
        print("".join(row))

for line in file:
    direction, amount = line.split(" ")
    for _ in range(int(amount)):
        steps.append(direction)

for step in steps:
    # move the head
    if step == "U":
        if snake_pos[0][0] == 0:
            field.insert(0, ['.' for _ in range(len(field[0]))])
            visited.insert(0, ['.' for _ in range(len(visited[0]))])
            for i in range(len(snake_pos)):
                snake_pos[i][0] += 1
        snake_pos[0][0] -= 1
    elif step == "D":
        if snake_pos[0][0] == len(field) - 1:
            field.append(['.' for _ in range(len(field[0]))])
            visited.append(['.' for _ in range(len(visited[0]))])
        snake_pos[0][0] += 1
    elif step == "L":
        if snake_pos[0][1] == 0:
            for row in field:
                row.insert(0, ".")
            for row in visited:
                row.insert(0, ".")
            for i in range(len(snake_pos)):
                snake_pos[i][1] += 1
        snake_pos[0][1] -= 1
    elif step == "R":
        if snake_pos[0][1] == len(field[0]) - 1:
            for row in field:
                row.append(".")
            for row in visited:
                row.append(".")
        snake_pos[0][1] += 1

    for i in range(1, len(snake_pos)):
        if abs(snake_pos[i-1][0] - snake_pos[i][0]) > 1 or abs(snake_pos[i-1][1] - snake_pos[i][1]) > 1:
            # check if T is on the same x or y
            move = 0
            if snake_pos[i-1][0] != snake_pos[i][0] and snake_pos[i-1][1] == snake_pos[i][1]:
                # print("up/down")
                # move the same direction as H
                if snake_pos[i-1][0] < snake_pos[i][0]:
                    snake_pos[i][0] -= 1
                    move = 1
                elif snake_pos[i-1][0] > snake_pos[i][0]:
                    snake_pos[i][0] += 1
                    move = 2
            elif snake_pos[i-1][1] != snake_pos[i][1] and snake_pos[i-1][0] == snake_pos[i][0]:
                # print("across")
                # move the same direction as H
                if snake_pos[i-1][1] < snake_pos[i][1]:
                    snake_pos[i][1] -= 1
                    move = 3
                elif snake_pos[i-1][1] > snake_pos[i][1]:
                    snake_pos[i][1] += 1
                    move = 4

            else:
                # print("Diagonal")
                # move T diagonal to H
                if snake_pos[i-1][0] > snake_pos[i][0]:
                    snake_pos[i][0] += 1
                    move = 5
                else:
                    snake_pos[i][0] -= 1
                    move = 6
                
                if snake_pos[i-1][1] > snake_pos[i][1]:
                    snake_pos[i][1] += 1
                    move = 7
                else:
                    snake_pos[i][1] -= 1
                    move = 8
        # if i == 6 and snake_pos[i][0] == 5 and snake_pos[i][1] == 3:
        #     print(snake_pos[i])
        #     print(snake_pos[i-1])
                

        # set visited to T
        if i == len(snake_pos) - 1:
            visited[snake_pos[i][0]][snake_pos[i][1]] = "#"
        
    # field_copy = [row[:] for row in field]
    # for i in range(len(snake_pos)):
    #     field_copy[snake_pos[i][0]][snake_pos[i][1]] = str(i) if i != 0 else "H"
    # display_board(field_copy)
    # print()


# print(visited)

# add snake pos in
# for i in range(len(snake_pos)):
#     field[snake_pos[i][0]][snake_pos[i][1]] = str(i) if i != 0 else "H"
# display_board(field)
print(sum([True for row in visited for item in row if item == "#"]))
# display_board(visited)