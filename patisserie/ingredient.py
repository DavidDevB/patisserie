
from abc import ABC, abstractmethod


class Ingredient(ABC):

    def __init__(self, nom, quantite, unite):
        self.nom = nom
        self.quantite = quantite
        self.unite = unite

