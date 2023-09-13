def my_map(f, iterator, *autre_nombres):
    res = []
    for values in zip(iterator, *autre_nombres):
        # values = list(values)
        f_result = f(*values)
        res.append(f_result)
    return res 

def multiplication(a, b, c):
    return a * b * c


def multiplication(valeurs):
    return product(valeurs)

print(my_map(multiplication, 
       [1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9], 
))

# multiplication(1, 4, 7)
# multiplication(2, 5, 8)
# multiplication(3, 6, 9)