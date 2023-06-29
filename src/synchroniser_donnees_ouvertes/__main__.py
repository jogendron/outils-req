"""Programme de chargement des données ouvertes du REQ"""

import argparse

from .config import FabriqueConfiguration
from .site_web import SiteWebDonneesOuvertes
from .donnees_ouvertes.lecteurs import LecteurDomaineValeurCsv
from .donnees_ouvertes.lecteurs import LecteurEntrepriseCsv
from .donnees_ouvertes.lecteurs import LecteurNomCsv
from .donnees_ouvertes.lecteurs import LecteurEtablissementCsv
from .donnees_ouvertes.lecteurs import LecteurFusionScissionCsv
from .donnees_ouvertes.lecteurs import LecteurContinuationTransformationCsv
from .donnees_ouvertes.depots import UniteTravailPostgres

def charger_config() -> dict:
    """Charge le fichier de configuration de l'outil"""
    gestionnaire_configuration = FabriqueConfiguration.creer_configuration()
    return gestionnaire_configuration.charger_config()

def telecharger(config: dict):
    """Télécharge les données du REQ sur disque"""
    site = SiteWebDonneesOuvertes(
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["SiteWeb"]["DonneesOuvertes"],
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"]
    )

    if site.mise_a_jour_est_disponible():
        site.telecharger_donnees_ouvertes()

def importer_domaine_valeur(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les domaines de valeurs dans la base de données"""
    lecteur_domaine_valeur = LecteurDomaineValeurCsv(
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"]
    )

    for domaine in lecteur_domaine_valeur.obtenir():
        print(f"Mise à jour du domaine de valeur {domaine.typ_dom_val}-{domaine.cod_dom_val}")
        unite_travail.depot_domaine_valeur.mettre_a_jour(domaine)
        unite_travail.commit()

def importer_entreprise(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les entreprises dans la base de données"""
    lecteur_entreprise = LecteurEntrepriseCsv(
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"]
    )

    compteur = 0
    for entreprise in lecteur_entreprise.obtenir():
        print(f"Mise à jour de l'entreprise {entreprise.neq}")
        unite_travail.depot_entreprise.mettre_a_jour(entreprise)
        compteur += 1

        if compteur >= 1000:
            unite_travail.commit()
            compteur = 0

    unite_travail.commit()

def importer_nom(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les noms dans la base de données"""
    lecteur_nom = LecteurNomCsv(config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"])

    compteur = 0
    for nom in lecteur_nom.obtenir():
        print(f"Mise à jour du nom {nom.neq}-{nom.nom_assuj}-{nom.stat_nom}-{nom.typ_nom_assuj}")
        unite_travail.depot_nom.mettre_a_jour(nom)
        compteur += 1

        if compteur >= 1000:
            unite_travail.commit()
            compteur = 0

    unite_travail.commit()

def importer_etablissement(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les établissements dans la base de données"""
    lecteur_etablissement = LecteurEtablissementCsv(
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"]
    )

    compteur = 0
    for etablissement in lecteur_etablissement.obtenir():
        cle = f"{etablissement.neq}-{etablissement.no_suf_etab}"
        print(f"Mise à jour de l'établissement {cle}")
        unite_travail.depot_etablissement.mettre_a_jour(etablissement)
        compteur += 1

        if compteur >= 1000:
            unite_travail.commit()
            compteur = 0


    unite_travail.commit()

def importer_fusion_scission(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les fusions et scissions dans la base de données"""
    lecteur_fusion_scission = LecteurFusionScissionCsv(
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"]
    )

    compteur = 0

    for fusion_scission in lecteur_fusion_scission.obtenir():
        cle = f"{fusion_scission.neq}- \
            {fusion_scission.neq_assuj_rel}- \
            {fusion_scission.cod_rela_assuj}- \
            {fusion_scission.dat_efctvt}"

        print(f"Mise à jour de la fusion/scission {cle}")
        unite_travail.depot_fusion_scission.mettre_a_jour(fusion_scission)
        compteur += 1

        if compteur >= 1000:
            unite_travail.commit()
            compteur = 0

    unite_travail.commit()

def importer_continuation_transformation(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les continuations et transformations dans la base de données"""
    lecteur_continuation_transformation = LecteurContinuationTransformationCsv(
        config["OutilsREQ"]["SynchroDonneesOuvertes"]["Repertoires"]
    )

    compteur = 0

    for continuation_transformation in lecteur_continuation_transformation.obtenir():
        cle = f"{continuation_transformation.neq}-\
            {continuation_transformation.cod_typ_chang}-\
            {continuation_transformation.dat_efctvt}"

        print(f"Mise à jour de la continuation/transformation {cle}")
        unite_travail.depot_continuation_transformation.mettre_a_jour(continuation_transformation)
        compteur += 1

        if compteur >= 1000:
            unite_travail.commit()
            compteur = 0

    unite_travail.commit()

def importer(config: dict, unite_travail: UniteTravailPostgres):
    """Importe les données du REQ dans la base de données"""
    importer_domaine_valeur(config, unite_travail)
    importer_entreprise(config, unite_travail)
    importer_nom(config, unite_travail)
    importer_etablissement(config, unite_travail)
    importer_fusion_scission(config, unite_travail)
    importer_continuation_transformation(config, unite_travail)

    unite_travail.commit()
    unite_travail.fermer()

def main():
    """Lis les arguments de ligne de commande et déclenche la bonne action"""
    parser = argparse.ArgumentParser(
        prog="ImporterReq",
        description="Importe les données du REQ"
    )

    subparsers = parser.add_subparsers(help="sub-command help", dest="subparser_name")
    subparsers.add_parser("creer_configuration", help="creer_configuration help")
    subparsers.add_parser("telecharger", help="telecharger help")
    parser_importer = subparsers.add_parser("importer", help="importer help")
    parser_importer.add_argument(
        "type_donnee", 
        type=str,
        nargs="?",
        choices=(
            "continuation_transformation",
            "domaine_valeur", 
            "entreprise", 
            "nom", 
            "etablissement", 
            "fusion_scission"
        )
    )

    args = parser.parse_args()
    config = charger_config()
    unite_travail = UniteTravailPostgres(config["OutilsREQ"]["SynchroDonneesOuvertes"]["Postgres"])

    match args.subparser_name:
        case None:
            telecharger(config)
            importer(config, unite_travail)

        case "creer_configuration":
            pass

        case "telecharger":
            telecharger(config)

        case "importer":
            match args.type_donnee:
                case None:
                    importer(config, unite_travail)
                case "continuation_transformation":
                    importer_continuation_transformation(config, unite_travail)
                case "domaine_valeur":
                    importer_domaine_valeur(config, unite_travail)
                case "entreprise":
                    importer_entreprise(config, unite_travail)
                case "nom":
                    importer_nom(config, unite_travail)
                case "etablissement":
                    importer_etablissement(config, unite_travail)
                case "fusion_scission":
                    importer_fusion_scission(config, unite_travail)
main()
