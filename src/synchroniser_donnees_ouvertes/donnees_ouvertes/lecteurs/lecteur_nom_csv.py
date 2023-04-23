"""Lecteur de nom au format csv"""

import csv

from . import Lecteur
from .. import Nom

class LecteurNomCsv(Lecteur):
    """Lecteur de nom au format csv"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.fichier = "Nom.csv"

    def obtenir(self):
        """Retourne les noms du fichier"""
        chemin = self.obtenir_chemin_fichier(self.fichier)

        with open(chemin, newline='', encoding="UTF-8-SIG") as fichier:
            lecteur_csv = csv.DictReader(fichier, delimiter=',', quotechar='"')
            for ligne in lecteur_csv:
                yield Nom(
                    ligne["NEQ"],
                    ligne["NOM_ASSUJ"],
                    ligne["NOM_ASSUJ_LANG_ETRNG"],
                    ligne["STAT_NOM"],
                    ligne["TYP_NOM_ASSUJ"],
                    self._convertir_en_datetime(ligne["DAT_INIT_NOM_ASSUJ"]),
                    self._convertir_en_datetime(ligne["DAT_FIN_NOM_ASSUJ"])
                )
