"""Module de configuration pour les systèmes windows"""

import os.path

from synchroniser_donnees.config import configuration

class ConfigurationWindows(configuration.Configuration):
    """Gère la configuration pour les systèmes unix"""

    def __init__(self):
        super().__init__()
        self._chemin = os.path.expanduser(
            "~/AppData/Roaming/outils-req/synchroniser-donnees/config.json"
        )

    def _creer_config(self, chemin: str):
        """Crée le fichier de configuration"""
        repertoire_config = chemin[0:len("config.json") * -1]

        if not os.path.isdir(repertoire_config):
            os.makedirs(repertoire_config)

        with open(chemin, "w", encoding="UTF-8") as fichier:
            fichier.write("""{
    "OutilsREQ": {
        "Synchro": {
            "Repertoires": {
                "DonneesOuvertes": "~/AppData/Local/outils-req/donnees-ouvertes"
            },
            "SiteWeb": {
                "DonneesOuvertes": {
                    "Url": "https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_22A_PIU_RecupDonnPub_PC/PageDonneesOuvertes.aspx",
                    "TimeoutPage":  30,
                    "TimeoutDonnees": 600
                }
            }
        }
    }
}
"""
            )
