"""Module de configuration"""

import os.path
import json

class Configuration:
    """Classe de gestion de la configuration"""

    def __init__(self):
        self._chemin = ""

    def _creer_config(self, chemin: str):
        """Crée le fichier de configuration"""

    def __obtenir_chemin_configuration(self) -> str:
        """Vérifie si le fichier de configuration existe"""
        chemin = self._chemin

        if not os.path.isfile(chemin):
            self._creer_config(chemin)

        return chemin

    def charger_config(self) -> dict:
        """Charge le fichier de configuration de l'outil"""
        dictionnaire = {}
        chemin = self.__obtenir_chemin_configuration()

        with open(chemin, "r", encoding="UTF-8") as fichier:
            dictionnaire = json.loads(fichier.read())

        return dictionnaire
