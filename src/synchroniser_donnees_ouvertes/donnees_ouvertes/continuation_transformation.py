"""Continuation ou transformation"""

import datetime

class ContinuationTransformation:
    """Continuation ou transformation"""

    def __init__(
        self,
        neq: str,
        cod_typ_chang: str,
        cod_regim_juri: str,
        autr_regim_juri: str,
        nom_loclt: str,
        dat_efctvt: datetime
    ):
        self.neq = neq
        self.cod_typ_chang = cod_typ_chang
        self.cod_regim_juri = cod_regim_juri
        self.autr_regim_juri = autr_regim_juri
        self.nom_loclt = nom_loclt
        self.dat_efctvt = dat_efctvt