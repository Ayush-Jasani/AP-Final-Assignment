def extractDup(nums):
    """
    Takes a list of integers and returns the list of integers that have duplicates in the original list.
    
    Args:
        nums (list): List of integers
        
    Returns:
        list: List of integers that appear more than once in the input list
    
    Examples:
        >>> extractDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) -> [20, 30, 60, -20]
        >>> extractDup([-1, 1, -1, 8]) -> [-1]
        >>> extractDup([-3, 1, -1, 8]) -> []
    """
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return sorted(list(duplicates))