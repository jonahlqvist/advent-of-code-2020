the_file = open("passwords")

passwords = the_file.readlines()


def find_valid():
    valid = 0
    invalid = 0
    for a in passwords:
        policy, password = a.split(":")
        limit, letter = policy.split(" ")
        pos1, pos2 = limit.split("-")
        pos1, pos2 = int(pos1), int(pos2)

        password = list(password)

        if password[pos1] == letter and password[pos2] != letter:
            valid += 1
        elif password[pos1] != letter and password[pos2] == letter:
            valid += 1
        else:
            invalid += 1

    return valid, invalid


print(find_valid())