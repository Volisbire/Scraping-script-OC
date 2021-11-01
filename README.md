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


Le script recupere page(s), ouvrage(s) et categorie(s) vers un fichier CSV
--------------------------------------------------------------------------

Le script est case sensitive | Nom de l'image = UPC du livre associé


Installation
------------
Python3 doit etre installe sur votre systeme : https://www.python.org/
L'utilisation d'un environnement virtuel est fortement recommandé
Pour installer les bibliotheques necessaires:

python -m pip -r requirments.txt
