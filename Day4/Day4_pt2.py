the_file = open("input_text")
passports = the_file.read().split("\n\n")

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
req_fields_nocid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
req_fields.sort()
req_fields_nocid.sort()


def valid_value(field):
    name, value = field.split(':')
    value = unicode(value, 'utf-8')

    if name == 'byr' and 1920 <= int(value) <= 2002:
        return True
    elif name == 'iyr' and 2010 <= int(value) <= 2020:
        return True
    elif name == 'eyr' and 2020 <= int(value) <= 2030:
        return True
    elif name == 'hgt':
        if value[-2:] == 'cm' and 150 <= int(value[0:-2]) <= 193:
            return True
        elif value[-2:] == 'in' and 59 <= int(value[0:-2]) <= 76:
            return True
    elif name == 'hcl':
        if value[0] == '#' and len(value) == 7:
            for a in value[1:]:
                if a not in 'abcdef1234567890':
                    return False
            return True
    elif name == 'ecl':
        color_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in color_list:
            return True
    elif name == 'pid':
        if len(value) == 9 and value.isnumeric():
            return True
    elif name == 'cid':
        return True
    return False


def check_id(passports):
    valid = 0
    for passport in passports:
        check_list = []
        passport = passport.split()
        print(passport)

        for field in passport:
            field_name = field.split(':')[0]
            check_list.append(field_name)
        check_list.sort()

        if check_list == req_fields:
            valid_field_count = 0
            for field in passport:
                if valid_value(field):
                    valid_field_count += 1
            if valid_field_count == 8:
                print('valid normal')
                valid += 1
        elif check_list == req_fields_nocid:
            valid_field_count = 0
            for field in passport:
                if valid_value(field):
                    valid_field_count += 1
            if valid_field_count == 7:
                print('valid nocid')
                valid += 1

    return valid


print(check_id(passports))
