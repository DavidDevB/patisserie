
class Recipient:
    def __init__(self, contenu):
        self.contenu = contenu

    def get_quantite(self):
        return self.contenu.quantite

    def get_unite(self):
        return self.contenu.unite

    def __str__(self):
        return f"Récipient contenant {self.contenu.quantite}{self.contenu.unite} d'ingrédients."
