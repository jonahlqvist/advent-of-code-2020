the_file = open("text_input")
input = the_file.read().split("\n\n")


def find_yes_nr(answers):
    total_length = 0
    for group_answers in answers:
        group_list = []
        group_answers = group_answers.split("\n")
        for person_answers in group_answers:
            for letter in person_answers:
                if letter not in group_list:
                    group_list.append(letter)
        total_length += len(group_list)
    print(total_length)


def find_all_yes_nr(answers):
    total_length = 0
    for group_answers in answers:
        group_yes_list = []
        group_answers = group_answers.split("\n")
        for person_answers in group_answers:
            person_yes_list = []
            for letter in person_answers:
                person_yes_list.append(letter)
            group_yes_list.append(set(person_yes_list))

        all_yes = set.intersection(*group_yes_list)
        total_length += len(all_yes)
    print(total_length)


find_yes_nr(input)
find_all_yes_nr(input)