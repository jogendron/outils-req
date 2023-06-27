"""Établissement"""

class Etablissement:
    """Établissement"""

    def __init__(
        self,
        neq: str,
        no_suf_etab: int,
        ind_etab_princ: bool,
        ind_salon_bronz: bool,
        ind_vente_tabac_detl: bool,
        ind_disp: bool,
        lign1_adr: str,
        lign2_adr: str,
        lign3_adr: str,
        lign4_adr: str,
        cod_act_econ: str,
        desc_act_econ_etab: str,
        no_act_econ_etab: int,
        cod_act_econ2: str,
        desc_act_econ_etab2: str,
        no_act_econ_etab2: int
    ):
        self.neq = neq
        self.no_suf_etab = no_suf_etab
        self.ind_etab_princ = ind_etab_princ
        self.ind_salon_bronz = ind_salon_bronz
        self.ind_vente_tabac_detl = ind_vente_tabac_detl
        self.ind_disp = ind_disp
        self.lign1_adr = lign1_adr
        self.lign2_adr = lign2_adr
        self.lign3_adr = lign3_adr
        self.lign4_adr = lign4_adr
        self.cod_act_econ = cod_act_econ
        self.desc_act_econ_etab = desc_act_econ_etab
        self.no_act_econ_etab = no_act_econ_etab
        self.cod_act_econ2 = cod_act_econ2
        self.desc_act_econ_etab2 = desc_act_econ_etab2
        self.no_act_econ_etab2 = no_act_econ_etab2
