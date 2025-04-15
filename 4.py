class UpperCaseException(Exception):
    pass

def evenIndexCapital(s):
    result = ''
    i = 0
    while True:
        try:
            ch = s[i]
        except IndexError:
            break
        ascii_val = ord(ch)
        if ascii_val >= 65 and ascii_val <= 90:
            raise UpperCaseException("Input string contains uppercase letters.")
        if i % 2 == 0:
            ch = chr(ascii_val - 32)  # to uppercase
        result += ch
        i += 1
    return result
