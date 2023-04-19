"""Programme de chargement des données ouvertes du REQ"""

import argparse

from synchroniser_donnees.config import fabrique_configuration
from synchroniser_donnees.site_web import site_web_donnees_ouvertes

def charger_config() -> dict:
    """Charge le fichier de configuration de l'outil"""
    gestionnaire_configuration = fabrique_configuration.FabriqueConfiguration.creer_configuration()
    return gestionnaire_configuration.charger_config()

def telecharger(config: dict):
    """Télécharge les données du REQ sur disque"""
    site = site_web_donnees_ouvertes.SiteWebDonneesOuvertes(
        config["OutilsREQ"]["Synchro"]["SiteWeb"]["DonneesOuvertes"],
        config["OutilsREQ"]["Synchro"]["Repertoires"]
    )

    if site.mise_a_jour_est_disponible():
        site.telecharger_donnees_ouvertes()

def importer(config: dict):
    """Importe les données du REQ dans la base de données"""

def main():
    """Lis les arguments de ligne de commande et déclenche la bonne action"""
    parser = argparse.ArgumentParser(
        prog="ImporterReq",
        description="Importe les données du REQ"
    )

    subparsers = parser.add_subparsers(help="sub-command help", dest="subparser_name")
    parser_telecharger = subparsers.add_parser("telecharger", help="telecharger help")
    parser_importer = subparsers.add_parser("importer", help="importer help")

    args = parser.parse_args()
    config = charger_config()

    match args.subparser_name:
        case None:
            telecharger(config)
            importer(config)

        case "telecharger":
            telecharger(config)

        case "importer":
            importer(config)

main()
