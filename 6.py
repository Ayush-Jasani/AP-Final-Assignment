def distChar(s1, s2):
    unique = ''
    i = 0
    while True:
        try:
            ch = s1[i]
        except IndexError:
            break
        if not char_in(ch, s2) and not char_in(ch, unique):
            unique += ch
        i += 1
    i = 0
    while True:
        try:
            ch = s2[i]
        except IndexError:
            break
        if not char_in(ch, s1) and not char_in(ch, unique):
            unique += ch
        i += 1
    return sort_str(unique)

def char_in(ch, s):
    for c in s:
        if ch == c:
            return True
    return False

def sort_str(s):
    s_list = []
    for ch in s:
        s_list.append(ch)
    # simple bubble sort
    n = len(s_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if s_list[j] > s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
    result = ''
    for ch in s_list:
        result += ch
    return result
