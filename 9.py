def moveDups(s):
    seen = ''
    dups = ''
    i = 0
    while True:
        try:
            ch = s[i]
        except IndexError:
            break
        if not char_in(ch, seen):
            seen += ch
        else:
            dups += ch
        i += 1
    if get_length(dups) > 0:
        return seen + '_' + dups
    return seen

def char_in(ch, s):
    for c in s:
        if c == ch:
            return True
    return False

def get_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
