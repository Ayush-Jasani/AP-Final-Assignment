class InvalidInputException(Exception):
    pass

def change(s):
    count_R = 0
    count_G = 0
    i = 0
    while True:
        try:
            ch = s[i]
        except IndexError:
            break
        if ch == 'R':
            count_R += 1
        elif ch == 'G':
            count_G += 1
        else:
            raise InvalidInputException("Only 'R' and 'G' allowed")
        i += 1
    return count_R if count_R < count_G else count_G
