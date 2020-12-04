the_file = open("passwords")

passwords = the_file.readlines()


def find_valid():
    valid = 0
    invalid = 0
    for a in passwords:
        policy, password = a.split(":")
        limit, letter = policy.split(" ")
        lower_limit, upper_limit = limit.split("-")

        if int(lower_limit) <= password.count(letter) <= int(upper_limit):
            valid += 1
        else:
            invalid += 1

    return valid, invalid


print(find_valid())
