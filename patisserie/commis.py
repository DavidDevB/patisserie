
from abc import ABC, abstractmethod

class Commis(ABC):
    """Classe abstraite Commis parente"""

    def __init__(self, name):
        self.name = name