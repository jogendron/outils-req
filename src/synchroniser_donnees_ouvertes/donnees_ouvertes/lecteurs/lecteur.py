"""Module commun pour les lecteurs"""

import datetime
import os
import os.path

class Lecteur:
    """Interface commune pour les lecteurs"""
    def __init__(self, config: dict):
        repertoire_donnees_ouvertes = os.path.expanduser(config["DonneesOuvertes"])
        sous_repertoires = [
            f.path
            for f in os.scandir(repertoire_donnees_ouvertes)
            if f.is_dir()
        ]

        if sous_repertoires:
            sous_repertoires.sort(reverse=True)
            self._repertoire = sous_repertoires[0]

    def _convertir_en_bool(self, valeur: str):
        """Converti une chaîne O/N en bool"""
        return True if valeur == "O" else False

    def _convertir_en_int(self, valeur: str):
        """Converti une chaîne en int"""
        return int(valeur) if (valeur and valeur != "") else None

    def _convertir_en_datetime(self, valeur: str):
        """Converti une chaîne yyyy-mm-dd en datetime"""
        retour = None

        if valeur != "":
            segments = valeur[0:10].split("-")
            if len(segments) == 3:
                retour = datetime.datetime(
                    int(segments[0]),
                    int(segments[1]),
                    int(segments[2])
                )

        return retour

    def obtenir(self):
        """Obtient les entités du lecteur"""

    def obtenir_chemin_fichier(self, fichier: str):
        """
        Construit le chemin du fichier, vérifie qu'il existe
        et retourne le chemin
        """
        chemin = os.path.join(self._repertoire, fichier)

        if not os.path.isfile(chemin):
            raise FileNotFoundError()

        return chemin
