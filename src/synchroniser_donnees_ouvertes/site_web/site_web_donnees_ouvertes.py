"""Module d'accès aux données ouvertes du REQ"""

import os
import os.path
import zipfile

from seleniumrequests import Firefox
import bs4

class SiteWebDonneesOuvertes:
    """Accès à l'unité de traitement des données ouvertes du REQ"""
    def __init__(self, config_site_web: dict, config_repertoire: dict):
        self.__cache = {}

        self.__url = config_site_web["Url"]
        self.__timeout_page = config_site_web["TimeoutPage"]
        self.__timeout_donnees = config_site_web["TimeoutDonnees"]

        self.__repertoire_telechargement = os.path.expanduser(config_repertoire["DonneesOuvertes"])

        os.environ['MOZ_HEADLESS'] = '1'

    def __obtenir_date_mise_a_jour(self):
        """
        Obtient la date de dernière mise à jour des données ouvertes
        """
        cle_cache = "date_maj"

        if not cle_cache in self.__cache:
            navigateur = Firefox()
            navigateur.set_page_load_timeout(float(self.__timeout_page))
            navigateur.get(self.__url)
            soup = bs4.BeautifulSoup(navigateur.page_source, "html.parser")

            span = soup.find(name="span", attrs={"id": "CPHContenuGR_lblDate"})
            date = span.text
            self.__cache["date_maj"] = date[0:10]

        return self.__cache[cle_cache]

    def __obtenir_chemin_fichier(self) -> str:
        """
        Détermine le nom que le fichier devrait porter si on l'enregistre
        """
        repertoire = self.__repertoire_telechargement
        nom_fichier = f"{self.__obtenir_date_mise_a_jour()}.zip"

        if not os.path.isdir(self.__repertoire_telechargement):
            os.makedirs(self.__repertoire_telechargement)

        return os.path.join(repertoire, nom_fichier)

    def __creer_payload_telechargement(self, soup: bs4.BeautifulSoup):
        """Envoie une requête pour télécharger les données ouvertes"""
        viewstate = soup.find(
                name="input",
                attrs={
                    "type": "hidden",
                    "id": "__VIEWSTATE"
                }
            ).attrs["value"]

        viewstategenerator = soup.find(
                name="input",
                attrs={
                    "type": "hidden",
                    "id": "__VIEWSTATEGENERATOR"
                }
            ).attrs["value"]

        event_validation = soup.find(
                name="input",
                attrs={
                    "type": "hidden",
                    "id": "__EVENTVALIDATION"
                }
            ).attrs["value"]

        return {
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE":  viewstate,
                "__VIEWSTATEGENERATOR": viewstategenerator,
                "__EVENTVALIDATION": event_validation,
                "ctl00$CPHContenuGR$btnDonnees": "Télécharger+le+jeu+de+données"
            }

    def effacer_cache(self):
        """Efface la cache de la classe"""
        self.__cache = {}

    def mise_a_jour_est_disponible(self) -> bool:
        """
        Vérifie si une mise à jour des données ouvertes est disponible
        """
        return not os.path.isfile(self.__obtenir_chemin_fichier())

    def telecharger_donnees_ouvertes(self) -> str:
        """
        Télécharge les données ouvertes si nécessaire
        Retourne le répertoire où les données sont extraites
        """
        chemin_zip = self.__obtenir_chemin_fichier()
        chemin_decompresse = chemin_zip[0:len(".zip") * -1]

        if self.mise_a_jour_est_disponible():
            navigateur = Firefox()
            navigateur.set_page_load_timeout(float(self.__timeout_page))
            navigateur.get(self.__url)
            soup = bs4.BeautifulSoup(navigateur.page_source, "html.parser")

            post = navigateur.request(
                'POST', 
                self.__url,
                stream=True,
                timeout=self.__timeout_donnees,
                data=self.__creer_payload_telechargement(soup)
            )

            if post.ok:
                print("Téléchargement en cours...")
                with open(chemin_zip, 'wb') as fichier:
                    for segment in post.iter_content(chunk_size=1024 * 8):
                        if segment:
                            fichier.write(segment)
                            fichier.flush()

                print("Décompression de l'archive...")
                with zipfile.ZipFile(chemin_zip, 'r') as reference_zip:
                    reference_zip.extractall(chemin_decompresse)

        return chemin_decompresse
