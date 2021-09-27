import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
URL = 'https://emedicine.medscape.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)


lista = []
x = 0
while x <= 29:
    lista.append(soup.find_all("li")[x])
    x += 1

print('Medicine: ')
new_list = []
pom = 0
for item in lista:
 title = str(item.get_text()).split(" > ", 2)[0]
 print(str(pom) + " - " + title)
 new_list.append(title)
 pom +=1



# podpunkt B
#tworze liste znacznikow <a> ktore mnie intersuja
tag_a = []
y = 32
while y <=61:
    tag_a.append(soup.find_all("a")[y])
    y += 1

#print(tag_a)

#pobieram linki ze znacznikow, jednoczesnie parsując linki ktore są relatywne

link_list = []
for x in tag_a:
    absolute_link = urljoin(URL, x.get('href'))
    link_list.append(absolute_link)
    #print(absolute_link)

#print(link_list)
print()
kategoria = input("Wprowadż cyfre odpowiadającą nazwie kategorii aby przejść dalej: ")


url_2 = link_list[int(kategoria)]
page_2 = requests.get(url_2)
soup2 = BeautifulSoup(page_2.content, 'html.parser')
#print(soup2)
print()
print("Podkategorie dla wybranego działu: ")
print()
lista_2 = []
x = 0
while x < 20:  #na te chwile ustawilem wyszukiwanie podkategorii do pierwszych 20 do celow testowych, w dalszej czesci postaram sie zrobic by petla while byla ogranicza do ilosci podkategorii w danej kategorii
    lista_2.append(soup2.find_all("li")[x])
    x += 1



for item in lista_2:
 title = str(item.get_text()).split(" > ", 2)[0]
 print("* " + title)
 new_list.append(title)

