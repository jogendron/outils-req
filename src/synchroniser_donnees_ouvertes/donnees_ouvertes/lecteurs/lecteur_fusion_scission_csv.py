"""Lecteur de fusion et scission au format csv"""

import csv

from . import Lecteur
from .. import FusionScission

class LecteurFusionScissionCsv(Lecteur):
    """Lecteur de fusion et scission au format csv"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.fichier = "FusionScissions.csv"

    def obtenir(self):
        """Retourne les fusions et scissions du fichier"""
        chemin = self.obtenir_chemin_fichier(self.fichier)

        with open(chemin, newline='', encoding="UTF-8-SIG") as fichier:
            lecteur_csv = csv.DictReader(fichier, delimiter=',', quotechar='"')
            for ligne in lecteur_csv:
                yield FusionScission(
                    ligne["NEQ"],
                    ligne["NEQ_ASSUJ_REL"],
                    ligne["DENOMN_SOC"],
                    ligne["COD_RELA_ASSUJ"],
                    self._convertir_en_datetime(ligne["DAT_EFCTVT"]),
                    self._convertir_en_bool(ligne["IND_DISP"]),
                    ligne["LIGN1_ADR"],
                    ligne["LIGN2_ADR"],
                    ligne["LIGN3_ADR"],
                    ligne["LIGN4_ADR"]
                )
