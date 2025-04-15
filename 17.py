def list_processor(numbers):
    """
    Takes a list of integers and performs various operations.
    
    Args:
        numbers (list): List of integers
        
    Returns:
        None (prints results)
    """
    if len(numbers) >= 4:
        print(f"a. Fourth item: {numbers[3]}")
    else:
        print("a. List doesn't have a fourth item")
    
    print(f"b. All items except first two: {numbers[2:]}")
    
    print(f"c. Reversed list: {numbers[::-1]}")
    
    print(f"d. Sum of elements: {sum(numbers)}")
    
    print(f"e. Maximum: {max(numbers)}, Minimum: {min(numbers)}")
    
    try:
        zero_index = numbers.index(0)
        print(f"f. Index of first zero: {zero_index}")
    except ValueError:
        print("f. No zero found: -1")
    
    # g. Print list sorted in ascending and descending order
    print(f"g. Ascending: {sorted(numbers)}")
    print(f"g. Descending: {sorted(numbers, reverse=True)}")