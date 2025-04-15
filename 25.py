class InvalidKException(Exception):
    pass

def kMax(lst, k):
    if not lst:
        raise InvalidKException("List cannot be empty")
    
    if k <= 0 or k > len(lst):
        raise InvalidKException(f"k must be between 1 and {len(lst)}")
    
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[k-1]