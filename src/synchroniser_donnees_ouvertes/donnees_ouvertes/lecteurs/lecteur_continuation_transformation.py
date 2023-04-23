"""Lecteur de continuation et transformation au format csv"""

import csv

from . import Lecteur
from .. import ContinuationTransformation

class LecteurContinuationTransformationCsv(Lecteur):
    """Lecteur de continuation et transformation au format csv"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.fichier = "ContinuationsTransformations.csv"

    def obtenir(self):
        """Retourne les continuations et transformations du fichier"""
        chemin = self.obtenir_chemin_fichier(self.fichier)

        with open(chemin, newline='', encoding="UTF-8-SIG") as fichier:
            lecteur_csv = csv.DictReader(fichier, delimiter=',', quotechar='"')
            for ligne in lecteur_csv:
                yield ContinuationTransformation(
                    ligne["NEQ"],
                    ligne["COD_TYP_CHANG"],
                    ligne["COD_REGIM_JURI"],
                    ligne["AUTR_REGIM_JURI"],
                    ligne["NOM_LOCLT"],
                    self._convertir_en_datetime(ligne["DAT_EFCTVT"])
                )
