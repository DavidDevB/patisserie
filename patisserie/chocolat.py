from ingredient import Ingredient


class Chocolat(Ingredient):
    def __init__(self, nom, quantity, unite):
        super().__init__(nom, quantity, unite)