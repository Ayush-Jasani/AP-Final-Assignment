def matMul(mat1, mat2):
    if not mat1 or not mat2 or not mat1[0] or not mat2[0]:
        raise DimensionMismatchException("Empty matrix provided")
    
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    
    for row in mat1:
        if len(row) != cols1:
            raise DimensionMismatchException("First matrix has inconsistent row lengths")
    
    for row in mat2:
        if len(row) != cols2:
            raise DimensionMismatchException("Second matrix has inconsistent row lengths")
    
    if cols1 != rows2:
        raise DimensionMismatchException("Matrix dimensions don't match for multiplication")
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result