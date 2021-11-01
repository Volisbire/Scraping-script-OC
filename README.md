Script python de scraping pour le site : https://books.toscrape.com/
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
1. Python3 doit etre installe sur votre systeme : https://www.python.org/

2. L'utilisation d'un environnement virtuel est fortement recommandé:

py -m venv c:\path\to\myenv


3. Pour installer les bibliotheques necessaires:

py -m pip install -r requirements.txt


Utilisation
-----------
Depuis la console:

py main.py
