from oeuf import Oeuf
from chocolat import Chocolat


class Appareil(Oeuf, Chocolat):
    def __init__(self, quantite_oeuf: float, quantite_chocolat: float, unite: str):
        Oeuf.__init__(self, quantite_oeuf, unite)
        Chocolat.__init__(self, quantite_chocolat, unite)
        self.total = quantite_oeuf + quantite_chocolat
        self.unite = unite
