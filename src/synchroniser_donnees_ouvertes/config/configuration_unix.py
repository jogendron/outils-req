"""Configuration pour les systèmes Unix"""

import os.path

from . import Configuration

CONFIG_DEFAUT_UNIX = """{
    "OutilsREQ": {
        "SynchroDonneesOuvertes": {
            "Repertoires": {
                "DonneesOuvertes": "~/.local/share/outils-req/donnees-ouvertes"
            },
            "SiteWeb": {
                "DonneesOuvertes": {
                    "Url": "https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_22A_PIU_RecupDonnPub_PC/PageDonneesOuvertes.aspx",
                    "TimeoutPage":  30,
                    "TimeoutDonnees": 600
                }
            },
            "Postgres": {
                "NomBaseDonnees": "req",
                "Hote": "localhost",
                "Utilisateur": "req_usr",
                "MotPasse": "req_usr",
                "Port": 5432
            }
        }
    }
}
"""

class ConfigurationUnix(Configuration):
    """Gère la configuration pour les systèmes unix"""

    def __init__(self):
        super().__init__()
        self._chemin = os.path.expanduser("~/.config/outils-req/synchroniser-donnees-ouvertes/config.json")

    def _creer_config(self, chemin: str):
        """Crée le fichier de configuration"""
        repertoire_config = chemin[0:len("config.json") * -1]

        if not os.path.isdir(repertoire_config):
            os.makedirs(repertoire_config)

        with open(chemin, "w", encoding="UTF-8") as fichier:
            fichier.write(CONFIG_DEFAUT_UNIX)
