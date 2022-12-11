import math

file = open("test.txt").read().splitlines()
file = open("input.txt").read().splitlines()

class Monkey:
    true_throw: int
    false_throw: int
    items: list[int]
    test_condition: int
    _operation: str
    inspected = 0

    def __init__(self, true_throw: int, false_throw: int, items: list[int], operation: Callable[[int], int], test_condition: Callable[[int], bool]):
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.items = items
        self._operation = operation
        self.test_condition = test_condition

    def __str__(self) -> str:
        return f"Monkey with {self.items}"

    def operation(self, value):
        other = value if not self._operation[1].isnumeric() else int(self._operation[1])
        if self._operation[0] == "+":
            return value + other
        elif self._operation[0] == "-":
            return value - other
        elif self._operation[0] == "*":
            return value * other
        else:
            return value / other

    def test(self, value):
        return value % self.test_condition == 0


monkeys: list[Monkey] = []

for i in range(0, len(file), 7):
    starting_values = file[i+1].split(": ")[1].split(", ")
    starting_values = [int(x) for x in starting_values]
    
    operation_value= file[i + 2].split("new = old ")[1]
    operation = (operation_value.split(" ")[0], operation_value.split(" ")[1].strip())
    
    value = int(file[i + 3].split("by ")[1])
    test_condition = value

    true_throw = int(file[i + 4].split("monkey ")[1].strip())
    false_throw = int(file[i + 5].split("monkey ")[1].strip())

    monkeys.append(Monkey(true_throw, false_throw, starting_values, operation, test_condition))

# get lowest common denominator of all test conditions
lcm = math.lcm(*[monkey.test_condition for monkey in monkeys])

for i in range(10000):
    print("Round", i)
    for j in range(len(monkeys)):
        monkey = monkeys[j]
        for item in monkey.items:
            item = monkey.operation(item)
            # item = math.floor(item / 3) # part 1
            item = item % lcm
            if monkey.test(item):
                monkeys[monkey.true_throw].items.append(item)
            else:
                monkeys[monkey.false_throw].items.append(item)
            monkey.inspected += 1
        monkey.items = []



monkeys.sort(key=lambda x: x.inspected, reverse=True)
monkeys = monkeys[:2]
print(monkeys[0].inspected, monkeys[1].inspected)
print(monkeys[0].inspected * monkeys[1].inspected)