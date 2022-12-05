# file = ["vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]

file = open("input.txt", "r").read().splitlines()


def get_value(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96

score = 0

# part 1
for line in file:
    part1, part2 = line[:len(line)//2], line[len(line)//2:]

    # get common letters in both parts
    common = [c for c in part1 if c in part2]
    # remove duplicates
    common = list(set(common))
    score += sum([get_value(c) for c in common])
print(score)



# part 2
lines = [file[i:i+3] for i in range(0, len(file), 3)]

for line in lines:
    # get common letters in all 3 lines
    common = [c for c in line[0] if c in line[1] and c in line[2]]
    # remove duplicates
    common = list(set(common))
    score += sum([get_value(c) for c in common])

print(score)