import threading
import time
import math
from commis import Commis
from recipient import Recipient
from oeuf import Oeuf
from chocolat import Chocolat


class BatteurOeufs(Commis, threading.Thread):
    def __init__(self, nb_oeufs: int, nom: str):
        Commis.__init__(self, nom)
        threading.Thread.__init__(self)
        self.nb_oeufs = nb_oeufs

    def run(self):
        # on suppose qu'il faut 8 tours de batteur par œuf présent dans le bol
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\t{self.nom} bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)  # temps supposé d'un tour de batteur


class FondeurChocolat(Commis, threading.Thread):
    def __init__(self, quantite: int, nom: str):
        Commis.__init__(self, nom)
        threading.Thread.__init__(self)
        self.quantite = quantite  # en grammes

    def run(self):
        print(f"{self.nom} mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print(f"{self.nom} verse l'eau dans une casserole")
        time.sleep(2)
        print(f"{self.nom} y pose le bol rempli de chocolat")
        time.sleep(1)
        # On suppose qu'il faut 1 tour de spatule par 10 g. de chocolat
        # présent dans le bol pour faire fondre le chocolat.
        nb_tours = math.ceil(self.quantite / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"{self.nom} mélange {self.quantite} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)  # temps supposé d'un tour de spatule


class Verseur(Commis, threading.Thread):
    _lock = threading.Lock()

    def __init__(self, recipient1: Recipient, recipient2: Recipient, nom):
        Commis.__init__(self, nom)
        threading.Thread.__init__(self)

        self.recipient1 = recipient1.contenu
        self.recipient2 = recipient2.contenu

    def run(self):
        with Verseur._lock:
            quantite_oeufs = self.recipient2.quantite
            print(f"{self.nom} prends le premier récipient")
            time.sleep(2)
            print(f"{self.nom} verse dans le deuxième récipient")
            time.sleep(5)
            self.recipient2.quantite += self.recipient1.quantite
            total_recipients1 = self.recipient1.quantite
            total_recipients1 += self.recipient1.quantite
            print(f"Le deuxième récipient contient maintenant {self.recipient2.quantite}{self.recipient2.unite} "
                  f"d'ingrédients: {total_recipients1}g de chocolat et {quantite_oeufs}g d'oeufs")


if __name__ == "__main__":
    batteur = BatteurOeufs(6, "Paul")
    fondeur = FondeurChocolat(200, "Alain")
    fondeur2 = FondeurChocolat(300, "Georges")
    recipient_choco1 = Recipient(Chocolat(200, "g"))
    recipient_choco2 = Recipient(Chocolat(300, "g"))
    recipient_oeuf = Recipient(Oeuf(300, "g"))
    verseur1 = Verseur(recipient_choco1, recipient_oeuf, "Pierre")
    verseur2 = Verseur(recipient_choco2, recipient_oeuf, "Michael")
    batteur.start()
    fondeur.start()
    fondeur2.start()
    batteur.join()
    fondeur.join()
    fondeur2.join()
    print("\nLes verseurs peuvent à présent incorporer le chocolat aux oeufs")
    verseur1.start()
    verseur2.start()
    verseur1.join()
    verseur2.join()
