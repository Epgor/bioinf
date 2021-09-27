import bs4
import requests
import io
import re
import urllib.parse
import calendar
from PIL import Image

def zad2():
   url = "https://bmcsystbiol.biomedcentral.com/articles"
   base_url = 'https://bmcsystbiol.biomedcentral.com'
   soup = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')

   month = calendar.month_name[int(input('Podaj nr miesiąca 1-12: '))]

   path = "C:\\Users\\User\\Desktop\\szkola\\3r1sem\\lab\\bioinf\\lab8i9\\" + month + ".txt"
   pathpdf = "C:\\Users\\User\\Desktop\\szkola\\3r1sem\\lab\\bioinf\\lab8i9\\" + month + "_"

   lista = []
   for li in soup.find_all('li'):
      if month in str(li):
         lista.append(li)

   f = open(path, "w")
   for article in lista:
      Title = article.find('a', {'data-test': 'title-link'}).text
      soup = bs4.BeautifulSoup(requests.get("https://bmcsystbiol.biomedcentral.com/articles/"\
                                            + re.search('href="/articles/(.*?)" itemprop',\
                                               str(article)).group(1), verify=True).text, 'html.parser')
      try:
         abstract = soup.find('section', {'data-title': 'Abstract'}).text
         
         with io.open(path, "a", encoding="utf-8") as f:
            f.write(article.find('a', {'data-test': 'title-link'}).text + "\n")
            f.write(article.find('p', {'class': 'c-listing__authors u-mb-0'}).text + "\n")
            f.write(abstract + "\n\n")
            
      except AttributeError:
         pass

      if 'network' in Title or 'networks' in Title:
         link = article.find('a', attrs={'data-test': 'pdf-link'}).get('href')
         file_title = "".join(list(filter(lambda x: x.isalnum() or x == ' ', Title)))
         urllib.request.urlretrieve(base_url + link + '.pdf', pathpdf + file_title + '.pdf')
         
   f.close()
   
def zad3():
    url = "https://emedicine.medscape.com"
    soup = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
    for categories in soup.find_all('div', {'class': 'browse-medicine'}):
       print(categories.text)

    wybor = input("Podaj nazwe kategorii: ")
    categories = soup.find('div', {'class': 'browse-medicine'})
    try:
        link = re.search('href="(.*?)">' + wybor, str(categories)).group(1)
        if link.startswith('http://'):
            url = link
        else:
            url = url + link
        print(url)
        soup = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
        for categories in soup.find_all('div', {'class': 'topic-head'}):
            print(categories.text)
    except(TypeError):
       pass
   
if __name__ == "__main__":
    while True:
        if int(input("\nLaboratory nr 8 \n Press any number to continue... \n 0 ends program \n")) !=0:
            if int(input("\n\nChoose number of excercise: (2 lub 3)\n")) == 2:
                zad2()
            else:
                zad3()
        else:
            break