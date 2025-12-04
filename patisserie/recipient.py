
from appareil import Appareil


class Recipient(Appareil):
    def __init__(self,quantite, unite):
        Appareil.__init__(self, quantite, unite)