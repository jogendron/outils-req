"""Dépôt de nom dans postgres"""

from psycopg2.errors import ForeignKeyViolation

from . import DepotPostgres
from .. import Nom

UPSERT_NOM = """
    insert into donnees_ouvertes.nom(
        neq,
        nom_assuj,
        nom_assuj_lang_etrng,
        stat_nom,
        typ_nom_assuj,
        dat_init_nom_assuj,
        dat_fin_nom_assuj
    ) values (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    ) on conflict (
        neq, nom_assuj, stat_nom, typ_nom_assuj
    ) do update set
        nom_assuj = excluded.nom_assuj,
        nom_assuj_lang_etrng = excluded.nom_assuj_lang_etrng,
        stat_nom = excluded.stat_nom,
        typ_nom_assuj = excluded.typ_nom_assuj,
        dat_init_nom_assuj = excluded.dat_init_nom_assuj,
        dat_fin_nom_assuj = excluded.dat_fin_nom_assuj
"""

class DepotNomPostgres(DepotPostgres):
    """Dépôt de nom dans postgres"""

    def mettre_a_jour(self, item: Nom):
        """Insert ou met à jour les noms dans la bd"""
        self._curseur.execute("savepoint savepoint_nom")

        try:
            self._curseur.execute(
                UPSERT_NOM,
                (
                    item.neq,
                    item.nom_assuj,
                    item.nom_assuj_lang_etrng,
                    item.stat_nom,
                    item.typ_nom_assuj,
                    item.dat_init_nom_assuj,
                    item.dat_fin_nom_assuj
                )
            )
        except ForeignKeyViolation:
            print(f"Impossible d'insérer le nom {item.nom_assuj} de l'entreprise {item.neq}")
            self._curseur.execute("rollback to savepoint savepoint_nom")
        finally:
            self._curseur.execute("release savepoint savepoint_nom")
