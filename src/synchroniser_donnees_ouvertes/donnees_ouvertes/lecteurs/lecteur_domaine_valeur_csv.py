"""Lecteur de domaines de valeurs en format csv"""

import csv

from . import Lecteur
from ..domaine_valeur import DomaineValeur

class LecteurDomaineValeurCsv(Lecteur):
    """Lecteur de domaines de valeurs en format csv"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.fichier = "DomaineValeur.csv"

    def obtenir(self):
        """Retourne les domaines de valeurs"""
        chemin = self.obtenir_chemin_fichier(self.fichier)

        with open(chemin, newline='', encoding="UTF-8-SIG") as fichier:
            lecteur_csv = csv.DictReader(fichier, delimiter=',', quotechar='"')
            for ligne in lecteur_csv:
                yield DomaineValeur(
                    ligne["TYP_DOM_VAL"],
                    ligne["COD_DOM_VAL"],
                    ligne["VAL_DOM_FRAN"]
                )
