def my_map(f, iterator, *autre_nombres):
    for values in zip(iterator, *autre_nombres):
        pass  


def multiplication(a, b, c):
    return a * b * c


my_map(multiplication, 
       [1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]
)

multiplication(1, 4, 7)
multiplication(2, 5, 8)
multiplication(3, 6, 9)