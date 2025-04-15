class InvalidRollException(Exception):
    pass

def fc(base, roll):
    if get_length(roll) != 7:
        raise InvalidRollException()

    dept = roll[0] + roll[1]
    year = (ord(roll[2]) - 48) * 10 + (ord(roll[3]) - 48)
    prog = roll[4]

    if not (dept == 'CS' or dept == 'DS' or dept == 'ME' or dept == 'EE'):
        raise InvalidRollException()

    if prog == '1':
        duration = 4
    elif prog == '2':
        duration = 2
    else:
        raise InvalidRollException()

    total_fee = 0
    current_year = 23
    for i in range(duration):
        if year + i > current_year:
            break
        if i == 0:
            yearly = base
        else:
            yearly = yearly + (yearly * 10) // 100
        total_fee += yearly
    return total_fee
