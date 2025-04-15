def problem14_groupWords(words):
    groups = []
    used = []

    i = 0
    while i < list_len(words):
        if in_list(used, i):
            i += 1
            continue
        temp_group = [words[i]]
        used.append(i)

        j = i + 1
        while j < list_len(words):
            if share_char(words[i], words[j]):
                temp_group.append(words[j])
                used.append(j)
            j += 1

        groups.append(temp_group)
        i += 1
    return groups

def list_len(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt

def in_list(lst, val):
    for item in lst:
        if item == val:
            return True
    return False

def share_char(w1, w2):
    for ch1 in w1:
        for ch2 in w2:
            if ch1 == ch2:
                return True
    return False
