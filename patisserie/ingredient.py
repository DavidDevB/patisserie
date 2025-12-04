
from abc import ABC, abstractmethod


class Ingredient(ABC):

    def __init__(self, quantite, unite):
        self.quantite = quantite
        self.unite = unite

