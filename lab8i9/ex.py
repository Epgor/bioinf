## Zadanie 1
## Zapoznaj się przykładowymi programami w Pyton które pozwola Ci zapoznać
##  się z podstawowymi bibliotekami umożliwiającymi szybkie parsowanie stron internetowych w celu pozyskiwania
##  z nich określonych informacji

# zainstaluj biblioteki: beautifulsoup4, urllib3, pillow, requests
import requests ## obsługa: url, stron www
#import wget   ## obsługa: adresy url
import bs4   ### obsługa: parsowanie www,   więcej na : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import os    ## obsługa: dyski i katalogi PC
import urllib.parse  ## obsługa: parsowanie url, więcej na: https://docs.python.org/3/library/urllib.parse.html
from PIL import Image   # praca z plikami graficznymi, więcej: https://pillow.readthedocs.io/en/5.1.x/
from io import BytesIO  #  praca z plikami, więcej na: https://www.tutorialspoint.com/python/python_files_io.htm
import fnmatch
##### Odczyt kodu HTML #######
url = 'http://www.poranny.pl/'
codeHTML = requests.get(url, verify=True).text # odczyt zawartości strony (HTML)
# #print(codeHTML)
soup = bs4.BeautifulSoup(codeHTML, 'html.parser') # tworzenie obiektu BeautifulSoup z zachowaniem struktury kodu strony
#print(soup) # wyświetlenie kodu z zachowaniem struktury

####podstawowe wybrane metody wyodrębniania tekstu w oparciu o znaczniki#######
######### Sprawdźmy jakie mamy znaczniki możliwe do odczytu
#list(print(tag.name) for tag in soup.find_all(True))  # pętla: wykaz wszystkich znaczników znalezionych na stronie
################# Treść widziana jako elementy listy
######### Odczytanie treści znajdującej się między znacznikiem <a> na stronie www
#print(soup.find("a"))  # 1-szy znaleziony znacznik <a> na stronie www
#print(soup.find_all("a"))  # uwaga ważne: tu argumentem wyjściowym jest lista, której elementy zawierają kod z każdego znacznika <a>
#print(soup.find_all("a")[1]) # kod z drugiego znacznika <a> czyli o indexie 1-szym,
#### Szukanie linków w znacznikach np. <a>
#for link in soup.find_all('a'):
#    print(link.get('href'))

#### lub
# list_link = list(link.get('href') for link in soup.find_all('a'))
# print(list_link)
################# Treść widziana jako elementy słownika
#onetags = soup.find_all("a")[3]  # kod z czwartego znacznika <a> czyli o indexie 3-szym,
#### <a class="serwisPlus" data-gtm="naglowek/link-do-serwisu-plus" ...........
#### Zwróć uwagę że mamy tu tekst zbliżony do struktury słownika
#print(onetags)
#print(onetags.attrs)    # wynik typ:słownik,   wyświetlamy zawartość w formie:  klucz <-> zawartość klucza
#print(onetags.attrs['href']) # wyświetl zawartość kodu klucza:'href'

########## Jeśli interesuje nas zawsze tylko 1-szy znaleziony znacznik możemy nie korzystać z metody find_all
########## Odczytamy teraz zawartość znacznika <a>
#print(soup.a) # uwaga ważne: tu argumentem wyjściowym jest słownik,  kod zawiera treść z pierwszego znacznika <a>,
#print(soup.a['href']) # kod z pierwszego znacznika o nazwie <a>, zawartość klucza href

########## Odczytamy teraz zawartość znacznika <div>
#print(soup.div) # kod zawiera treść z pierwszego znacznika <div>,
#print(soup.div['class']) # kod z pierwszego znacznika o nazwie <div>, zawartość klucza class  tj. <div class="zafixowanaGora">

##################################################################################

# ####### Selekcja informacji szukanie plików w określonym formatem:
url = 'http://www.poranny.pl/'
poranny = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')  # zwróć uwagę na zagnieżdżanie metod
#print(poranny)

# first_link = poranny.find_all('link')  # odczytanie tekstu z 2-go znacznika <a>
# print(first_img)
links = []
for img in poranny.find_all('img'):
    links.append(img.get('src'))
#
# print(links)



# ######## Jeśli w liście pojawiły się elementy NoneType, należy je usunąć
tag_list = list(filter(None,links)) # odfiltruj elementy NoneType
# print(tag_list)

# ######## Jak zauważyłeś lista set_one_tags  zawiera dużo nieistotnych danych
# ######## Jak możemy je usunąć ?  Jak możemy poszukać określonego rozszerzenia?
#
# set_one_tags_split = list(tag.split('.') for tag in tag_list) # rozdziel znaki separator '.'
# print(set_one_tags_split)  # mogę użyć metod dla typu string i list, dzielac tekst na wyrazy które stanowią elementy list
#
# ### mogę szukać bezpośrenio
# urlJPG = [element for element in tag_list if element.endswith('jpg')]
# print(urlJPG)

# #### mogę użyć masek
set_one_tags_split_bool = list('jpg' in tag for tag in tag_list) # sprawdź czy zawiera fragment tekstu 'jpg'
#print(set_one_tags_split_bool)  # argument wyjsciowy ma typ Bool, to taka maska którą nałożymy na dane
# # # odczytamy numery indeksów listy w których wartość była 'True' i zapiszemy do listy
indexes = list(i for i in range(len(set_one_tags_split_bool)) if set_one_tags_split_bool[i]== True)
# print(indexes)
# # ##### Wykonajmy filtrację teraz naszych adresów względem wydzielonych indeksów
urlJPG = list(tag_list[indexes[i]] for i in range(len(indexes)))
# print(urlJPG)

######Zapis obrazu z linku nr 2#####
response = requests.get(urlJPG[1])
img = Image.open(BytesIO(response.content))  # otwórz plik graficzny
img.show()      # pokaż zawartość pliku
# img.save('obraz.jpg', "JPEG") # zapisz obraz do pliku  o nazwie obraz.jpg

###### Uwaga czasami zamiast metod filtrowania wygodniej jest wykorzystać np. obsługę błędu########
##### więcej o obsłudze błędów i wyjątków możesz znaleźć tu: https://docs.python.org/2/tutorial/errors.html
##### i oczywiście w materiałach do Wykładu 4
#
# url = 'https://iist.uwb.edu.pl/nii/?student=plany-studiow-i-sylabusy-i-stopien'
# ii = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
# tags_pdf = list(link.get('href') for link in ii.find_all('a'))   # zapiszemy poszczególne znaczniki <img> jako elementy listy
#print(tags_pdf)
#
# adres_list_pdf = list()
# for link in tags_pdf:
#     try:     # 'złap' błąd
#         if fnmatch.fnmatch(link,'http*pdf'):    #  można też użyć   link.endswith('pdf'):
#             adres_list_pdf.append(link)
#     except(RuntimeError, TypeError, NameError, AttributeError,ValueError): # można wpisać więcej :)  # pomiń określone błędy
#         pass
#
# print(adres_list_pdf)

# #######zapis do pliku #########
#print(os.getcwd()) # sprawdź nazwę ścieżki twojego folderu roboczego

# path = 'e:\\DYDAKTYKA\\Python2020\\'  # tu ustaw inną ścieżkę
# for link in adres_list_pdf:
#     url_file_split = os.path.split(link) # wynik to 2 elementowa krotka: (fragment adresu url, nazwa pliku)
#     fileName = url_file_split[1]  # nazwa pliku
#     path_file_join = os.path.join(os.path.dirname(path), fileName)# połącz ścieżkę folderu i nazwe pliku
#     urllib.request.urlretrieve(link, path_file_join)  # zapisz każdy dokument pdf na dysk