class DimensionMismatchException(Exception):
    pass

class InvalidOperationException(Exception):
    pass

class Vector:
    def __init__(self, *components):
        self.__components = list(components)
    
    def __str__(self):
        return f"{len(self.__components)}-dimensional vector: {self.__components}"
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise InvalidOperationException("Can only scale with a number")
        return Vector(*[component * scalar for component in self.__components])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise InvalidOperationException("Can only add with another Vector")
        if len(self.__components) != len(other.__components):
            raise DimensionMismatchException("Vectors must have the same dimension")
        return Vector(*[self.__components[i] + other.__components[i] for i in range(len(self.__components))])
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise InvalidOperationException("Can only subtract with another Vector")
        if len(self.__components) != len(other.__components):
            raise DimensionMismatchException("Vectors must have the same dimension")
        return Vector(*[self.__components[i] - other.__components[i] for i in range(len(self.__components))])
    
    def __matmul__(self, other):  # For dot product (using @ operator)
        if not isinstance(other, Vector):
            raise InvalidOperationException("Can only calculate dot product with another Vector")
        if len(self.__components) != len(other.__components):
            raise DimensionMismatchException("Vectors must have the same dimension")
        return sum(self.__components[i] * other.__components[i] for i in range(len(self.__components)))