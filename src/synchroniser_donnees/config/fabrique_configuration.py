"""Module de fabriques pour les configurations"""

import os.path

from synchroniser_donnees.config import configuration_unix
from synchroniser_donnees.config import configuration_windows

class FabriqueConfiguration:
    """Fabrique de fournisseur de configuration"""

    @staticmethod
    def creer_configuration():
        """
        Crée le bon fournissesur de configuration selon le système 
        d'exploitation qui roule le programme
        """
        config = None

        if os.name == "posix":
            config = configuration_unix.ConfigurationUnix()
        else:
            config = configuration_windows.ConfigurationWindows()

        return config
