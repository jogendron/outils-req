"""Lecteur d'entreprise au format csv"""

import csv

from . import Lecteur
from .. import Entreprise

class LecteurEntrepriseCsv(Lecteur):
    """Lecteur d'entreprise au format csv"""

    def __init__(self, config: dict):
        super().__init__(config)
        self.fichier = "Entreprise.csv"

    def obtenir(self):
        """Retourne les domaines de valeurs"""
        chemin = self.obtenir_chemin_fichier(self.fichier)

        with open(chemin, newline='', encoding="UTF-8-SIG") as fichier:
            lecteur_csv = csv.DictReader(fichier, delimiter=',', quotechar='"')
            for ligne in lecteur_csv:
                yield Entreprise(
                    ligne["NEQ"],
                    self._convertir_en_bool(ligne["IND_FAIL"]),
                    self._convertir_en_datetime(ligne["DAT_IMMAT"]),
                    ligne["COD_REGIM_JURI"],
                    ligne["COD_INTVAL_EMPLO_QUE"],
                    self._convertir_en_datetime(ligne["DAT_CESS_PREVU"]),
                    ligne["COD_STAT_IMMAT"],
                    ligne["COD_FORME_JURI"],
                    self._convertir_en_datetime(ligne["DAT_STAT_IMMAT"]),
                    ligne["COD_REGIM_JURI_CONSTI"],
                    self._convertir_en_datetime(ligne["DAT_DEPO_DECLR"]),
                    self._convertir_en_int(ligne["AN_DECL"]),
                    self._convertir_en_int(ligne["AN_PROD"]),
                    self._convertir_en_datetime(ligne["DAT_LIMIT_PROD"]),
                    self._convertir_en_int(ligne["AN_PROD_PRE"]),
                    self._convertir_en_datetime(ligne["DAT_LIMIT_PROD_PRE"]),
                    self._convertir_en_datetime(ligne["DAT_MAJ_INDEX_NOM"]),
                    ligne["COD_ACT_ECON_CAE"],
                    self._convertir_en_int(ligne["NO_ACT_ECON_ASSUJ"]),
                    ligne["DESC_ACT_ECON_ASSUJ"],
                    ligne["COD_ACT_ECON_CAE2"],
                    self._convertir_en_int(ligne["NO_ACT_ECON_ASSUJ2"]),
                    ligne["DESC_ACT_ECON_ASSUJ2"],
                    ligne["NOM_LOCLT_CONSTI"],
                    self._convertir_en_datetime(ligne["DAT_CONSTI"]),
                    self._convertir_en_bool(ligne["IND_CONVEN_UNMN_ACTNR"]),
                    self._convertir_en_bool(ligne["IND_RET_TOUT_POUVR"]),
                    self._convertir_en_bool(ligne["IND_LIMIT_RESP"]),
                    self._convertir_en_datetime(ligne["DAT_DEB_RESP"]),
                    self._convertir_en_datetime(ligne["DAT_FIN_RESP"]),
                    ligne["OBJET_SOC"],
                    ligne["NO_MTR_VOLONT"],
                    self._convertir_en_bool(ligne["ADR_DOMCL_ADR_DISP"]),
                    ligne["ADR_DOMCL_LIGN1_ADR"],
                    ligne["ADR_DOMCL_LIGN2_ADR"],
                    ligne["ADR_DOMCL_LIGN3_ADR"],
                    ligne["ADR_DOMCL_LIGN4_ADR"]
                )
