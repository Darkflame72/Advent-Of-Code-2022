file = open("test.txt", "r").read().splitlines()
file = open("input.txt", "r").read().splitlines()

dirs = {}

class Folder:
    children: list
    name: str
    parent: "Folder"

    def __init__(self, name, parent):
        self.children = []
        self.name = name
        self.parent = parent

    def size(self):
        _size = 0
        for child in self.children:
            if isinstance(child, Folder):
                _size += child.size()
            else:
                _size += child
        dirs[self.full_name()] = _size
        return _size

    def __str__(self):
        return self.name

    def full_name(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.full_name() + "/" + self.name

# remove first 2 lines from file
file = file[2:]

root = Folder("root", None)

current = root
children = []

for line in file:
    if line.startswith("$"):
        if "cd" in line:
            if line == "$ cd ..":
                if len(children) > 0:
                    current.children = children

                current = current.parent
            else:
                if len(children) > 0:
                    current.children = children
                changed = False
                for child in current.children:
                    if not isinstance(child, int) and child.name == line[5:]:
                        current = child
                        changed = True
                        break
                if not changed:
                    for child in current.children:
                        if not isinstance(child, int) and child.name == line[5:]:
                            print(child.name)
                    raise Exception("Folder not found")
            children = []
        elif "ls" in line:
            children = []
            continue
    else:
        if line.startswith("dir"):
            children.append(Folder(line[4:], current))
        else:
            children.append(int(line.split(" ")[0]))

if len(children) > 0:
    current.children = children

# part 1
total_size = root.size()
print(sum([size for size in dirs.values() if size <= 100000]))

# part 2
# find smallest folder to get total size less than 30000000
available = [size for size in dirs.values() if (70000000 - (total_size - size)) >= 30000000]
smallest = min(available)
dir_name = [name for name, size in dirs.items() if size == smallest][0]
print(dir_name, smallest)