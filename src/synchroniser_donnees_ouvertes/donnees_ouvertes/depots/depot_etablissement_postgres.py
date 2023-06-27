"""Dépôt d'établissements dans postgres"""

from psycopg2.errors import ForeignKeyViolation

from . import DepotPostgres
from .. import Etablissement

UPSERT_ETAB = """
    insert into donnees_ouvertes.etablissement(
        neq,
        no_suf_etab,
        ind_etab_princ,
        ind_salon_bronz,
        ind_vente_tabac_detl,
        ind_disp,
        lign1_adr,
        lign2_adr,
        lign3_adr,
        lign4_adr,
        cod_act_econ,
        desc_act_econ_etab,
        no_act_econ_etab,
        cod_act_econ2,
        desc_act_econ_etab2,
        no_act_econ_etab2
    ) values (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    ) on conflict ( 
        neq, no_suf_etab
    ) do update set
        ind_etab_princ = excluded.ind_etab_princ,
        ind_salon_bronz = excluded.ind_salon_bronz,
        ind_vente_tabac_detl = excluded.ind_vente_tabac_detl,
        ind_disp = excluded.ind_disp,
        lign1_adr = excluded.lign1_adr,
        lign2_adr = excluded.lign2_adr,
        lign3_adr = excluded.lign3_adr,
        lign4_adr = excluded.lign4_adr,
        cod_act_econ = excluded.cod_act_econ,
        desc_act_econ_etab = excluded.desc_act_econ_etab,
        no_act_econ_etab = excluded.no_act_econ_etab,
        cod_act_econ2 = excluded.cod_act_econ2,
        desc_act_econ_etab2 = excluded.desc_act_econ_etab2,
        no_act_econ_etab2 = excluded.no_act_econ_etab2
"""

class DepotEtablissementPostgres(DepotPostgres):
    """Dépôt d'établissements dans postgres"""

    def mettre_a_jour(self, item : Etablissement):
        """Met à jour les établissements"""
        self._curseur.execute("savepoint savepoint_etablissement")

        try:
            self._curseur.execute(
                UPSERT_ETAB,
                (
                    item.neq,
                    item.no_suf_etab,
                    item.ind_etab_princ,
                    item.ind_salon_bronz,
                    item.ind_vente_tabac_detl,
                    item.ind_disp,
                    item.lign1_adr,
                    item.lign2_adr,
                    item.lign3_adr,
                    item.lign4_adr,
                    item.cod_act_econ,
                    item.desc_act_econ_etab,
                    item.no_act_econ_etab,
                    item.cod_act_econ2,
                    item.desc_act_econ_etab2,
                    item.no_act_econ_etab2
                )
            )
        except ForeignKeyViolation:
            print(f"Impossible d'insérer l'établisssement {item.neq}–{item.no_suf_etab}")
            self._curseur.execute("rollback to savepoint savepoint_etablissement")
        finally:
            self._curseur.execute("release savepoint savepoint_etablissement")
