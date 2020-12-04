the_file = open("input_text", "r")

file_contents = the_file.readlines()


def find2020_two(numbers):
    for a in numbers:
        for b in numbers:
            if int(a) + int(b) == 2020:
                return int(a)*int(b)


def find2020_three(numbers):
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if int(a) + int(b) + int(c) == 2020:
                    return int(a)*int(b)*int(c)


print(find2020_two(file_contents))
print(find2020_three(file_contents))
