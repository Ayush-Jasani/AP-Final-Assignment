def firstLetters(s):
    result = ''
    i = 0
    length = 0
    for _ in s:
        length += 1
    in_word = False
    while i < length:
        ch = s[i]
        if ch != ' ' and not in_word:
            result += ch
            in_word = True
        elif ch == ' ':
            in_word = False
        i += 1
    return result
