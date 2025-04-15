def delVowels(s):
    result = ''
    i = 0
    while True:
        try:
            ch = s[i]
        except IndexError:
            break
        if not (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
                ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            result += ch
        i += 1
    return result
