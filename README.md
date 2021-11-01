Utilisation du script python de scraping pour le site : https://books.toscrape.com/
===================================================================================

Python 3 doit etre installé:
* https://www.python.org/downloads/

Le script extrait les donees suivantes:
* product_page_url
* universal_ product_code (upc)
* title
* price_including_tax
* price_excluding_tax
* number_available
* product_description
* category
* review_rating
* image_url
* image_associee_au_livre.jpeg

Le script recupere page(s), ouvrage(s) et categorie(s) vers un fichier CSV
--------------------------------------------------------------------------

Le script est case sensitive | Nom de l'image = UPC du livre associé


Installation
------------
Python3 doit etre installe sur votre systeme : https://www.python.org/
L'utilisation d'un environnement virtuel est fortement recommandé
Pour installer les bibliotheques necessaires, rendez vous depuis la console dans le dossier contenant le fichier requirements.txt:

py -m pip install -r requirements.txt


Utilisation
-----------
Rendez vous dans le dossier ou se trouve le main.py, puis:

py main.py
