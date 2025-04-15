def separate(s):
    groups = []
    if get_length(s) == 0:
        return groups

    i = 0
    current = ''
    while True:
        try:
            ch = s[i]
        except IndexError:
            break
        if current == '' or ch == current[0]:
            current += ch
        else:
            groups.append(current)
            current = ch
        i += 1
    groups.append(current)
    return groups
