def minIndexFirstString(str1, str2):
    max_index = -1
    i = 0
    while True:
        try:
            ch1 = str1[i]
        except IndexError:
            break
        j = 0
        while True:
            try:
                ch2 = str2[j]
            except IndexError:
                break
            if ch1 == ch2:
                max_index = i
            j += 1
        i += 1
    return max_index
