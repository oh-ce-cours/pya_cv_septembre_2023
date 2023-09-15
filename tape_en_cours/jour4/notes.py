class Note:
    def __init__(self, note):
        # self.validate_note(note)
        # self.__nombre = note
        self.nombre = note
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.validate_note(value)
        self.__nombre = value

    @staticmethod
    def validate_note(self, value):
        print(value)
        if not 0 <= value <= 20:
            raise ValueError("une note c'est entre 0 et 20")
        if not isinstance(value, int):
            raise TypeError("une note c'est un nombre entier")
    
    def compute_couleur(self):
        if self.__nombre < 5:
            return "rouge"
        elif self.__nombre < 9:
            return "orange"
        elif self.__nombre < 12:
            return "jaune"
        elif self.__nombre < 16:
            return "vert"
        elif self.__nombre <= 20:
            return "vert fluo"
        else:
            raise ValueError(f"ne devrait pas arriver. La note est {self.__nombre}")

    
    @property
    def couleur(self):
        return self.compute_couleur()
    
    def __str__(self):
        return f"La note est de {self.nombre} (catégorie {self.couleur})"