import csv
import re
import requests
import urllib.request
from bs4 import BeautifulSoup


def parsing(url):
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    return soup


def creation_csv(data, result):
    with open(data, 'a') as f:
        w = csv.DictWriter(f, result)
        w.writeheader()
        w.writerow(result)


def extraction_donnees_livre(url):
    result = {}
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    book_info = soup.find_all("td")
    result["title"] = soup.find('title').string.replace("\n", "").replace("| Books to Scrape - Sandbox", "").strip()
    result["product_page_url"] = url
    result["universal_product_code (upc)"] = book_info[0].string
    result["price_including_tax"] = book_info[3].string
    result["price_excluding_tax"] = book_info[2].string
    result["number_available"] = re.findall("\\d+", book_info[-2].string)
    result["product_description"] = soup.find_all("p")[-1].string
    result["category"] = soup.find("ul", class_="breadcrumb").find_all("a")[-1].string
    result["review_rating"] = soup.find(class_="star-rating").attrs['class'][1]
    result["image_url"] = soup.find('img').attrs['src'].replace("../", "")
    data = result.get("category")
    data = str(data)+(".csv")
    creation_csv(data, result)
    url_entiere_image = "http://books.toscrape.com/"+result.get("image_url")
    titre_de_limage = result.get("universal_product_code (upc)")
    titre_de_limage = str(titre_de_limage)+(".jpeg")
    f = open(titre_de_limage, 'wb')
    f.write(urllib.request.urlopen(url_entiere_image).read())
    f.close()


def lien_nb_page(url_de_base, url_cat):
    lien_suivant = parsing(url_de_base).find("li", class_="next").find("a").attrs['href']
    lien_suivant = url_cat+lien_suivant
    return lien_suivant


def trouver_le_nombre_de_page(url_cat):
    if parsing(url_cat).find('li', class_="current"):
        nb_de_page = parsing(url_cat).find('li', class_="current").string.strip().replace("Page 1 of ", "")
        nb_de_page = int(nb_de_page)
        return nb_de_page
    else:
        return 0


def nombre_de_page(nb_de_page):
    i = 1
    url_de_base = url_cat
    toute_les_url = []
    while i != nb_de_page:
        toute_les_url.append(lien_nb_page(url_de_base, url_cat))
        url_de_base = lien_nb_page(url_de_base, url_cat)
        i += 1
    return toute_les_url


def livre_de_la_page(url_cat):
    url = "http://books.toscrape.com/catalogue/"
    parsed_cat = parsing(url_cat).find_all("h3")
    links_books = []
    for link in parsed_cat:
        links_books.append(link.find("a").attrs['href'].replace("../", ""))
    each_book = []
    for link in links_books:
        each_book.append(url+link)
    return each_book


#parsing de la page d'acceuil et choix d'une catégorie
liste_cat = {}
categorie = None
url = "http://books.toscrape.com/"
all_cat = parsing(url).find(class_="nav").find_all("a")
for cat in all_cat:
    key = cat.string.strip()
    value = "http://books.toscrape.com/"+cat.attrs['href']
    liste_cat[key] = value
while categorie not in liste_cat.keys():
    categorie = input("Quelle catégorie voulez vous scraper (Books = toute les catégories) ? ")
url_cat = liste_cat[categorie].replace("index.html", "")
nb_de_page = trouver_le_nombre_de_page(url_cat)
liste_des_livres = livre_de_la_page(url_cat)
if nb_de_page:
    url_des_pages = nombre_de_page(nb_de_page)
    for i in url_des_pages:
        liste_des_livres.extend(livre_de_la_page(i))
for i in liste_des_livres:
    extraction_donnees_livre(i)