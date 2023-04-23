"""Dépôt de domaine de valeurs dans postgresql"""

from psycopg2.errors import ForeignKeyViolation

from . import DepotPostgres
from .. import FusionScission

UPSERT_FUSION_SCISSION = """
    insert into donnees_ouvertes.fusion_scission (
        neq,
        neq_assuj_rel,
        denomn_soc,
        cod_rela_assuj,
        dat_efctvt,
        ind_disp,
        lign1_adr,
        lign2_adr,
        lign3_adr,
        lign4_adr
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
        %s
    ) on conflict (
        neq, 
        neq_assuj_rel,
        cod_rela_assuj,
        dat_efctvt
    ) do update set
        denomn_soc = excluded.denomn_soc,
        ind_disp = excluded.ind_disp,
        lign1_adr = excluded.lign1_adr,
        lign2_adr = excluded.lign2_adr,
        lign3_adr = excluded.lign3_adr
"""

class DepotFusionScissionPostgres(DepotPostgres):
    """Dépôt de fusion et scission dans Postgres"""

    def mettre_a_jour(self, item: FusionScission):
        """Insère ou met à jour une fusion ou scission dans la bd"""
        self._curseur.execute("savepoint savepoint_fusion_scission")

        try:

            self._curseur.execute(
                UPSERT_FUSION_SCISSION,
                (
                    item.neq,
                    item.neq_assuj_rel,
                    item.denomn_soc,
                    item.cod_rela_assuj,
                    item.dat_efctvt,
                    item.ind_disp,
                    item.lign1_adr,
                    item.lign2_adr,
                    item.lign3_adr,
                    item.lign4_adr
                )
            )

        except ForeignKeyViolation:
            print(f"Impossible d'insérer la fusion/scission \
                {item.neq}-\
                {item.neq_assuj_rel}-\
                {item.cod_rela_assuj}-\
                {item.dat_efctvt} \
                de l'entreprise {item.neq}")
            self._curseur.execute("rollback to savepoint savepoint_fusion_scission")
        finally:
            self._curseur.execute("release savepoint savepoint_fusion_scission")
