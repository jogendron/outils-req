"""Programme de chargement des données ouvertes du REQ"""

import argparse

def telecharger():
    """Télécharge les données du REQ sur disque"""

def importer():
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

    match args.subparser_name:
        case None:
            print("fait tout")
            telecharger()
            importer()

        case "telecharger":
            print("télécharge")
            telecharger()

        case "importer":
            print("importe")
            importer()

main()
