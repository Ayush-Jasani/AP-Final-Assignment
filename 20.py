def oddCollatz(n):
    if n <= 0:
        return []
    
    sequence = []
    if n % 2 == 1:  # Only add if n is odd
        sequence.append(n)
    
    while n != 1:
        if n % 2 == 0:  # If even, divide by 2
            n = n // 2
        else:  # If odd, multiply by 3 and add 1
            n = 3 * n + 1
        
        if n % 2 == 1:  # Only add odd numbers to the result
            sequence.append(n)
    
    return sequence