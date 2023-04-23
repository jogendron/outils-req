"""Dépôt de domaine de valeurs dans postgresql"""

from psycopg2.errors import Error

from . import DepotPostgres
from .. import DomaineValeur

UPSERT_DOMAINE_VALEUR = """
    insert into donnees_ouvertes.domaine_valeur(
        typ_dom_val,
        cod_dom_Val,
        val_dom_fran
    ) values (
        %s,
        %s,
        %s
    ) on conflict (
        typ_dom_val,
        cod_dom_val
    ) do update set
        val_dom_fran = excluded.val_dom_fran
"""

class DepotDomaineValeurPostgres(DepotPostgres):
    """DepotDomaineValeurPostgres"""

    def mettre_a_jour(self, item: DomaineValeur):
        """Met à jour les domaines de valeur dans la bd"""

        try:
            self._curseur.execute(
                UPSERT_DOMAINE_VALEUR,
                (
                    item.typ_dom_val,
                    item.cod_dom_val,
                    item.val_dom_fran
                )
            )
        except Error as ex:
            cle = f"{item.typ_dom_val}-{item.cod_dom_val}"
            print(f"Impossible d'insérer le domaine de valeur {cle}")
            raise ex
        