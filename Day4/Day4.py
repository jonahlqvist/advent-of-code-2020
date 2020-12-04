the_file = open("input_text")
passports = the_file.read().split("\n\n")

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
req_fields_nocid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
req_fields.sort()
req_fields_nocid.sort()


def check_id():
    valid = 0
    for passport in passports:
        check_list = []
        passport = passport.split()
        print(passport)

        for field in passport:
            field_name = field.split(':')[0]
            check_list.append(field_name)
        check_list.sort()

        if check_list == req_fields or check_list == req_fields_nocid:
            valid += 1

    return valid


print(check_id())



#--------------------------- Crappy Solution -----------------------------------------------#



def check_id_2():
    valid = 0
    for passport in passports:
        valid_fields = 0
        passport = passport.split()
        print(passport)

        for field in passport:
            has_country = False
            field_name = field.split(':')[0]
            if field_name == 'cid':
                has_country = True
            if field_name in req_fields:
                valid_fields += 1
        if valid_fields == 8:
            valid += 1
            print('valid normal')
        elif valid_fields == 7 and not has_country:
            print('valid no country')
            valid += 1

    return valid


print(check_id_2())