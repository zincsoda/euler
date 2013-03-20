#!/usr/bin/python2.6

one_to_nineteen_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens_dict = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80: 'eighty', 90:'ninety'}


def parse_1_to_19(number):
    return len(one_to_nineteen_dict[number])

def parse_20_to_99(number):
    ten = int(str(number)[0]) * 10
    one = int(str(number)[1])
    if one == 0:
        return len(tens_dict[ten])
    else:
        return len(tens_dict[ten]) + len(one_to_nineteen_dict[one])

def parse_100_to_999(number):
    sum = 0
    hundred_digit = int(str(number)[0])
    sum += len(one_to_nineteen_dict[hundred_digit]) + len('hundred')
    two_digit_number = int(str(number)[1:])
    if two_digit_number == 0:
        return sum        
    sum += len('and')
    if two_digit_number < 20:
        sum += parse_1_to_19(two_digit_number)
    else:
        sum += parse_20_to_99(two_digit_number)
    return sum

if __name__=="__main__":
    total_sum = 0
    for i in range(1, 1000):
        if i < 20:
            total_sum += parse_1_to_19(i)
            continue
        if i < 100:
            total_sum += parse_20_to_99(i)
            continue
        total_sum += parse_100_to_999(i)
    total_sum += len('one') + len('thousand')
    print total_sum
