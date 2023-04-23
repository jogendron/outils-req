"""Fabriques pour les configurations"""

import os.path

from . import ConfigurationUnix
from . import ConfigurationWindows

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
            config = ConfigurationUnix()
        else:
            config = ConfigurationWindows()

        return config
