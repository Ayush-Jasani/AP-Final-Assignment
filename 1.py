def checkPalindrome(s):
    i = 0
    j = 0
    for ch in s:
        j += 1
    j -= 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
