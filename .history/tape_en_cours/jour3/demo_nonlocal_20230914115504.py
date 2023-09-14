cache = 1 

def outer():
    cache = 2
    def inner():
        nonlocal cache
        print(cache) 
        cache = 3
    print(cache)
    inner()
    print(cache)

outer()