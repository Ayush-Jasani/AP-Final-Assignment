class DimensionMismatchException(Exception):
    pass

def printMat(matrix):
    rows = len(matrix)
    if rows == 0:
        return
    
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise DimensionMismatchException("Matrix dimensions are inconsistent")
    
    for row in matrix:
        print(" ".join(str(x) for x in row))