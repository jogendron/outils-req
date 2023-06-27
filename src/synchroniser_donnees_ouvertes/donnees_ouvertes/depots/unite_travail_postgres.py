"""Unité de travail postgres"""

import psycopg2

from . import DepotDomaineValeurPostgres
from . import DepotEntreprisePostgres
from . import DepotNomPostgres
from . import DepotEtablissementPostgres
from . import DepotFusionScissionPostgres
from . import DepotContinuationTransformationPostgres

class UniteTravailPostgres:
    """Unité de travail postgres"""
    def __init__(self, config: dict):
        nom_base_donnees = config["NomBaseDonnees"]
        hote = config["Hote"]
        utilisateur = config["Utilisateur"]
        mot_passe = config["MotPasse"]
        port = config["Port"]

        self.__connexion = psycopg2.connect(
            database=nom_base_donnees,
            host=hote,
            user=utilisateur,
            password=mot_passe,
            port=port
        )

        self.__curseur = self.__connexion.cursor()
        self.depot_domaine_valeur = DepotDomaineValeurPostgres(self.__curseur)
        self.depot_entreprise = DepotEntreprisePostgres(self.__curseur)
        self.depot_nom = DepotNomPostgres(self.__curseur)
        self.depot_etablissement = DepotEtablissementPostgres(self.__curseur)
        self.depot_fusion_scission = DepotFusionScissionPostgres(self.__curseur)
        self.depot_continuation_transformation = DepotContinuationTransformationPostgres(self.__curseur)

    def commit(self):
        """Commit les transactions à la base de données"""
        self.__connexion.commit()

    def fermer(self):
        """Ferme l'unité de travail"""
        self.__curseur.close()
        self.__connexion.close()
