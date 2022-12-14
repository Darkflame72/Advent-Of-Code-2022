file = open("test.txt").read().splitlines()
file = open("input.txt").read().splitlines()

# get the smallest and largest number

smallest_x = 10000
largest_x = 0

smallest_y = 10000
largest_y = 0

for line in file:
    x = [int(i.split(",")[0]) for i in line.split(" -> ")]
    y = [int(i.split(",")[1]) for i in line.split(" -> ")]
    smallest_x_line = min(x)
    largest_x_line = max(x)
    smallest_y_line = min(y)
    largest_y_line = max(y)

    if smallest_x_line < smallest_x:
        smallest_x = smallest_x_line

    if largest_x_line > largest_x:
        largest_x = largest_x_line

    if smallest_y_line < smallest_y:
        smallest_y = smallest_y_line

    if largest_y_line > largest_y:
        largest_y = largest_y_line

length = largest_x - smallest_x + 1
height = largest_y

# for part 2 add 2 to height
height += 2

# set length to 1000 for part 2
# length = 1000

matrix = [['.' for _ in range(length)] for _ in range(height)]

# set the bottom row to all # for part 2
for i in range(length):
    matrix[height-1][i] = '#'


for line in file:
    coords = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in line.split(" -> ")]
    for i in range(len(coords) - 1):
        if coords[i][0] == coords[i + 1][0]:
            if coords[i][1] > coords[i + 1][1]:
                for j in range(coords[i + 1][1], coords[i][1]):
                    matrix[j-1][coords[i][0] - smallest_x] = '#'
            else:
                for j in range(coords[i][1], coords[i + 1][1]):
                    matrix[j-1][coords[i][0] - smallest_x] = '#'
        else:
            if coords[i][0] > coords[i + 1][0]:
                for j in range(coords[i + 1][0], coords[i][0]+1):
                    matrix[coords[i][1]-1][j - smallest_x] = '#'
            else:
                for j in range(coords[i][0], coords[i + 1][0]+1):
                    matrix[coords[i][1]-1][j - smallest_x] = '#'

snowball = 500 - smallest_x
matrix[0][snowball] = '+'

running = True
while running:
    y = 0
    snowball = 500 - smallest_x
    while y < height:
        if matrix[y][snowball] == '#' or matrix[y][snowball] == 'o':
            if snowball - 1 < 0:
                for line in matrix:
                    line.insert(0, '.')
                    line.insert(0, '.')
                matrix[height-1][0] = '#'
                matrix[height-1][1] = '#'
                snowball += 2
                smallest_x -= 2
            if snowball + 1 >= length:
                # add 1 to all the lengths
                for line in matrix:
                    line.append('.')
                    line.append('.')
                # set the bottom line to #
                matrix[height-1][len(matrix[height-1])-1] = '#'
                matrix[height-1][len(matrix[height-1])-2] = '#'
                length += 2

            if snowball - 1 >= 0 and (matrix[y][snowball-1] != '#' and matrix[y][snowball-1] != 'o'):
                snowball -= 1
                y += 1
            elif snowball + 1 < length and (matrix[y][snowball+1] != '#' and matrix[y][snowball+1] != 'o'):
                snowball += 1
                y += 1
            else:
                # if y - 1 == 0:
                #     running = False
                #     break
                matrix[y-1][snowball] = 'o'
                break
        elif y + 1 >= height:
                running = False
                break
        else:
            y += 1

    if y == 0:
        running = False
        break


print(sum([1 for line in matrix for i in line if i == 'o']))