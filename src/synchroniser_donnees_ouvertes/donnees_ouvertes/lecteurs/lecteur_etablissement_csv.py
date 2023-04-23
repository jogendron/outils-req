"""Lecteur d'établissement au format csv"""

import csv

from . import Lecteur
from .. import Etablissement

class LecteurEtablissementCsv(Lecteur):
    """Lecteur d'établissement au format csv"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.fichier = "Etablissements.csv"

    def obtenir(self):
        """Obtient les établissements du fichier"""
        chemin = self.obtenir_chemin_fichier(self.fichier)

        with open(chemin, newline='', encoding="UTF-8-SIG") as fichier:
            lecteur_csv = csv.DictReader(fichier, delimiter=',', quotechar='"')
            for ligne in lecteur_csv:
                yield Etablissement(
                    ligne["NEQ"],
                    self._convertir_en_int(ligne["NO_SUF_ETAB"]),
                    self._convertir_en_bool(ligne["IND_ETAB_PRINC"]),
                    self._convertir_en_bool(ligne["IND_SALON_BRONZ"]),
                    self._convertir_en_bool(ligne["IND_VENTE_TABAC_DETL"]),
                    self._convertir_en_bool(ligne["IND_DISP"]),
                    ligne["LIGN1_ADR"],
                    ligne["LIGN2_ADR"],
                    ligne["LIGN3_ADR"],
                    ligne["LIGN4_ADR"],
                    ligne["COD_ACT_ECON"],
                    ligne["DESC_ACT_ECON_ETAB"],
                    self._convertir_en_int(ligne["NO_ACT_ECON_ETAB"]),
                    ligne["COD_ACT_ECON2"],
                    ligne["DESC_ACT_ECON_ETAB2"],
                    self._convertir_en_int(ligne["NO_ACT_ECON_ETAB2"])
                )
