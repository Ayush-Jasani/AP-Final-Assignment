def shift(s, ccount=0, acount=0):
    if ccount < 0 or acount < 0:
        raise Exception("Counts must be non-negative integers.")

    def get_length(st):
        l = 0
        for _ in st:
            l += 1
        return l

    def rotate_left(st, count):
        l = get_length(st)
        count %= l
        return st[count:] + st[:count]

    def rotate_right(st, count):
        l = get_length(st)
        count %= l
        return st[-count:] + st[:-count]

    s = rotate_left(s, acount)
    s = rotate_right(s, ccount)
    return s
