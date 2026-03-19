class Square:
    def __init__(self, size=0):
        # check type
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
                                                
        # check value
        if size < 0:
            raise ValueError("size must be >= 0")
                                                                            
        # private attribute
        self.__size = size
