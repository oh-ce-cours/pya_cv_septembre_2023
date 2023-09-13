def ecrit_avant_apres(f):
    def wrapper():
        print("avant l'appel")
        f() 
        print("apres l'appel")
    return wrapper 


def parle():
    print("salut")