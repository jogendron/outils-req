"""Dépôt Postgres"""

from psycopg2.extensions import cursor

class DepotPostgres:
    """Dépôt Postgres"""

    def __init__(self, curseur: cursor):
        self._curseur = curseur

    def mettre_a_jour(self, item):
        """Met à jour les données de la collection dans la BD"""
