"""Entités en lien avec les entreprises"""

import datetime

class Entreprise:
    """Entreprise"""

    def __init__(
        self,
        neq: str,
        ind_fail: bool,
        dat_immat: datetime,
        cod_regim_juri: str,
        cod_intval_emplo_que: str,
        dat_cess_prevu: datetime,
        cod_stat_immat: str,
        cod_forme_juri: str,
        dat_stat_immat: datetime,
        cod_regim_juri_consti: str,
        dat_depo_declr: datetime,
        an_decl: int,
        an_prod: int,
        dat_limit_prod: datetime,
        an_prod_pre: int,
        dat_limit_prod_pre: datetime,
        dat_maj_index_nom: datetime,
        cod_act_econ_cae: str,
        no_act_econ_assuj: int,
        desc_act_econ_assuj: str,
        cod_act_econ_cae2: str,
        no_act_econ_assuj2: int,
        desc_act_econ_assuj2: str,
        nom_loclt_consti: str,
        dat_consti: datetime,
        ind_conven_unmn_actnr: bool,
        ind_ret_tout_pouvr: bool,
        ind_limit_resp: bool,
        dat_deb_resp: datetime,
        dat_fin_resp: datetime,
        objet_soc: str,
        no_mtr_volont: str,
        adr_domcl_adr_disp: bool,
        adr_domcl_lign1_adr: str,
        adr_domcl_lign2_adr: str,
        adr_domcl_lign3_adr: str,
        adr_domcl_lign4_adr: str
    ) -> None:
        self.neq = neq
        self.ind_fail = ind_fail
        self.dat_immat = dat_immat
        self.cod_regim_juri = cod_regim_juri
        self.cod_intval_emplo_que = cod_intval_emplo_que
        self.dat_cess_prevu = dat_cess_prevu
        self.cod_stat_immat = cod_stat_immat
        self.cod_forme_juri = cod_forme_juri
        self.dat_stat_immat = dat_stat_immat
        self.cod_regim_juri_consti = cod_regim_juri_consti
        self.dat_depo_declr = dat_depo_declr
        self.an_decl = an_decl
        self.an_prod = an_prod
        self.dat_limit_prod = dat_limit_prod
        self.an_prod_pre = an_prod_pre
        self.dat_limit_prod_pre = dat_limit_prod_pre
        self.dat_maj_index_nom = dat_maj_index_nom
        self.cod_act_econ_cae = cod_act_econ_cae
        self.no_act_econ_assuj = no_act_econ_assuj
        self.desc_act_econ_assuj = desc_act_econ_assuj
        self.cod_act_econ_cae2 = cod_act_econ_cae2
        self.no_act_econ_assuj2 = no_act_econ_assuj2
        self.desc_act_econ_assuj2 = desc_act_econ_assuj2
        self.nom_loclt_consti = nom_loclt_consti
        self.dat_consti = dat_consti
        self.ind_conven_unmn_actnr = ind_conven_unmn_actnr
        self.ind_ret_tout_pouvr = ind_ret_tout_pouvr
        self.ind_limit_resp = ind_limit_resp
        self.dat_deb_resp = dat_deb_resp
        self.dat_fin_resp = dat_fin_resp
        self.objet_soc = objet_soc
        self.no_mtr_volont = no_mtr_volont
        self.adr_domcl_adr_disp = adr_domcl_adr_disp
        self.adr_domcl_lign1_adr = adr_domcl_lign1_adr
        self.adr_domcl_lign2_adr = adr_domcl_lign2_adr
        self.adr_domcl_lign3_adr = adr_domcl_lign3_adr
        self.adr_domcl_lign4_adr = adr_domcl_lign4_adr
