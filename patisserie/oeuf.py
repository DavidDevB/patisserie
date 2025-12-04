
from ingredient import Ingredient

class Oeuf(Ingredient):
    def __init__(self, nom, quantite, unite):
        super().__init__(nom, quantite, unite)