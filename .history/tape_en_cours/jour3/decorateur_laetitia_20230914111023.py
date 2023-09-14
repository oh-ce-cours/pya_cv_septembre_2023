def salade(*args, **kwargs):
    print("salade")
    return salade

def tomate(*args, **kwargs):
    print("tomate")
    return tomate

def fromage(*args, **kwargs):
    print("avant l'appel")
    print("fromage")
    print("apres l'appel")
    return fromage

@fromage
@salade
@tomate
def sandwich(viande):
    print(f"{viande=}")

# sandwich = fromage(salade(tomate(sandwich)))

#sandwich(viande="vege")

 