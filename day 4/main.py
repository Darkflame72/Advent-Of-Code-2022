file = open("input.txt", "r").read().splitlines()

# file = [
#     "2-4,6-8",
# "2-3,4-5",
# "5-7,7-9",
# "2-8,3-7",
# "6-6,4-6",
# "2-6,4-8",
# ]

score = 0
for line in file:
    # sections: tuple[list[int], list[int]] = ([], [])
    side1, side2 = line.split(",")
    left = [int(x) for x in side1.split("-")]
    left = [*range(left[0], left[1]+1)]
    right = [int(x) for x in side2.split("-")]
    right = [*range(right[0], right[1]+1)]

    # check if all of left is in right or vice versa
    if all([x in right for x in left]) or all([x in left for x in right]):
        score += 1
    
print(score)

# part 2
score = 0
for line in file:
    # sections: tuple[list[int], list[int]] = ([], [])
    side1, side2 = line.split(",")
    left = [int(x) for x in side1.split("-")]
    left = [*range(left[0], left[1]+1)]
    right = [int(x) for x in side2.split("-")]
    right = [*range(right[0], right[1]+1)]

    # check if all of left is in right or vice versa
    if any([x in right for x in left]):
        score += 1

print(score)