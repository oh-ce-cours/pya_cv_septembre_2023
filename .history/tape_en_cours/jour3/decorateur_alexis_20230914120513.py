from functools import wraps

# Décorateur pour les ingrédients
def ingredient_haut(param):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"{param}") 
            sortie = f(*args, **kwargs)
            return sortie
        return wrapper
    return decorator


def ingredient_bas(param):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            sortie = f(*args, **kwargs)
            print(f"{param}") 
            return sortie
        return wrapper
    return decorator

# Décorateur pour le pain
def pain(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Pain")
        result = f(*args, **kwargs)
        print("Pain")
        return result
    return wrapper

# Fonction pour créer un sandwich
@pain
@ingredient_haut("salade")
@ingredient_haut("tomate")
@ingredient_bas("salade")
@ingredient_bas("fromage")
def sandwich(viande):
    """MIAM"""
    print(viande)


# Créez un sandwich en utilisant le décorateur
sandwich("steak")
help(sandwich)