"""Dépôt d'établissements dans postgres"""

from psycopg2.errors import ForeignKeyViolation

from . import DepotPostgres
from .. import ContinuationTransformation

UPSERT_CONTINUATION_TRANSFORMATION = """
    insert into donnees_ouvertes.continuation_transformation(
        neq,
        cod_typ_chang,
        cod_regim_juri,
        autr_regim_juri,
        nom_loclt,
        dat_efctvt
    ) values (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    ) on conflict (
        neq,
        cod_typ_chang,
        dat_efctvt
    ) do update set
        cod_regim_juri = excluded.cod_regim_juri,
        autr_regim_juri = excluded.autr_regim_juri,
        nom_loclt = excluded.nom_loclt
"""

class DepotContinuationTransformationPostgres(DepotPostgres):
    """Dépôt de continuation et transformation dans postgres"""

    def mettre_a_jour(self, item: ContinuationTransformation):
        self._curseur.execute("savepoint savepoint_continuation_transformation")

        try:
            self._curseur.execute(
                UPSERT_CONTINUATION_TRANSFORMATION,
                (
                    item.neq,
                    item.cod_typ_chang,
                    item.cod_regim_juri,
                    item.autr_regim_juri,
                    item.nom_loclt,
                    item.dat_efctvt
                )
            )
        except ForeignKeyViolation:
            print(f"Impossible d'insérer la continuation/transformation \
                {item.neq}–{item.cod_typ_chang}-{item.dat_efctvt}")
            self._curseur.execute("rollback to savepoint savepoint_continuation_transformation")
        finally:
            self._curseur.execute("release savepoint savepoint_continuation_transformation")
