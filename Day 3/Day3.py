the_file = open("input_text")
input_text = the_file.read().split("\n")


def tree_finder(tree_map, right, down):
    row = 0
    column = 0
    tree = 0
    for line in tree_map:
        try:
            if tree_map[row][column] == '#':
                tree += 1
        except IndexError:
            try:
                column = (column - len(line))
                if tree_map[row][column] == '#':
                    tree += 1
            except IndexError:
                return tree
        column += right
        row += down
    return tree


a = tree_finder(input_text, 1, 1)
b = tree_finder(input_text, 3, 1)
c = tree_finder(input_text, 5, 1)
d = tree_finder(input_text, 7, 1)
e = tree_finder(input_text, 1, 2)

print(b)
print(a*b*c*d*e)
