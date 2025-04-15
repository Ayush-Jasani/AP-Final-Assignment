def problem13_minOps(s):
    checked = ''
    freq = []

    i = 0
    while True:
        try:
            ch = s[i]
        except IndexError:
            break
        if not contains(checked, ch):
            checked += ch
            count = 0
            j = 0
            while True:
                try:
                    if s[j] == ch:
                        count += 1
                except IndexError:
                    break
                j += 1
            freq.append(count)
        i += 1

    min_op = 1000000
    k = 0
    while k < length(freq):
        target = freq[k]
        op = 0
        l = 0
        while l < length(freq):
            op += abs(freq[l] - target)
            l += 1
        if op < min_op:
            min_op = op
        k += 1
    return min_op

def contains(s, ch):
    for c in s:
        if c == ch:
            return True
    return False

def length(arr):
    c = 0
    for _ in arr:
        c += 1
    return c
