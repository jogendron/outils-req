"""Fusion ou scission d'entreprise"""

import datetime

class FusionScission:
    """Fusion ou scission d'entreprise"""

    def __init__(
        self,
        neq: str,
        neq_assuj_rel: str,
        denomn_soc: str,
        cod_rela_assuj: str,
        dat_efctvt: datetime,
        ind_disp: bool,
        lign1_adr: str,
        lign2_adr: str,
        lign3_adr: str,
        lign4_adr: str
    ):
        self.neq = neq
        self.neq_assuj_rel = neq_assuj_rel
        self.denomn_soc = denomn_soc
        self.cod_rela_assuj = cod_rela_assuj
        self.dat_efctvt = dat_efctvt
        self.ind_disp = ind_disp
        self.lign1_adr = lign1_adr
        self.lign2_adr = lign2_adr
        self.lign3_adr = lign3_adr
        self.lign4_adr = lign4_adr
