def ecrit_avant_apres(f):
    print("avant la définition du wrapper")
    def wrapper():
        print("avant l'appel")
        f() 
        print("apres l'appel")
    print("apres la définition du wrapper")
    return wrapper 

print("avant décoration")
@ecrit_avant_apres
def parle():
    print("salut")

# parle = ecrit_avant_apres(parle)

print("apres définition")

parle()

print("apres parle")