def my_map(f, iterator, *autre_nombres):
    res = []
    for values in zip(iterator, *autre_nombres):
        # values = list(values)
        f_result = f(*values)
        res.append(f_result)
    return res 

def multiplication(a, b, c):
    return a * b * c

print(my_map(multiplication, 
       [1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9], 
))

# multiplication(1, 4, 7)
# multiplication(2, 5, 8)
# multiplication(3, 6, 9)



def my_filter(f, iterator):
    res = []
    for value in iterator:
        f_result = f(value)
        if f_result == True:
            res.append(value)
    return res 