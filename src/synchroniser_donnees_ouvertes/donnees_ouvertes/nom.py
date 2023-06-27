"""Nom d'une entreprise"""

import datetime

class Nom:
    """Nom d'une entreprise"""

    def __init__(
        self,
        neq: str,
        nom_assuj: str,
        nom_assuj_lang_etrng: str,
        stat_nom: str,
        typ_nom_assuj: str,
        dat_init_nom_assuj: datetime,
        dat_fin_nom_assuj: datetime
    ):
        self.neq = neq
        self.nom_assuj = nom_assuj
        self.nom_assuj_lang_etrng = nom_assuj_lang_etrng
        self.stat_nom = stat_nom
        self.typ_nom_assuj = typ_nom_assuj
        self.dat_init_nom_assuj = dat_init_nom_assuj
        self.dat_fin_nom_assuj = dat_fin_nom_assuj
