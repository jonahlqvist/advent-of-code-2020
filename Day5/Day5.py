import math

the_file = open("text_input")
input = the_file.read().split("\n")


def find_seat_id(boarding_pass):
    row_low = 0
    row_high = 127
    col_low = 0
    col_high = 7

    for letter in boarding_pass:
        if letter == 'B':
            row_low = math.ceil((row_high - row_low)/2) + row_low
        elif letter == 'F':
            row_high = row_high - math.ceil((row_high - row_low)/2)
        elif letter == 'R':
            col_low = math.ceil((col_high - col_low)/2) + col_low
        elif letter == 'L':
            col_high = col_high - math.ceil((col_high - col_low) / 2)

    return row_low*8+col_low


def find_highest_id(boarding_passes):
    highest_id = 0
    for bp in boarding_passes:
        if find_seat_id(bp) > highest_id:
            highest_id = find_seat_id(bp)
    print(highest_id)


def find_our_seat(boarding_passes):
    all_ids = []
    real_ids = []

    for a in range(0, 127*8+7):
        all_ids.append(a)

    for bp in boarding_passes:
        real_ids.append(find_seat_id(bp))
    real_ids.sort()

    for id in all_ids:
        if id not in real_ids and id-1 in real_ids and id+1 in real_ids:
            print(id)


find_highest_id(input)
find_our_seat(input)
