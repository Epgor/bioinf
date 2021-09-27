#LAB8
from bs4 import BeautifulSoup
import requests

link = 'https://emedicine.medscape.com/'
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

lista = []
temp = 0

while temp <= 29:
    lista.append(soup.find_all("li")[temp])
    temp += 1

print(lista)

#LAB9
##########Zadanie 1
## Połącz się z Entrez - systemem wyszukiwania informacji w NCBI.
## Sprawdż ile publikacji w bazie PubMed znajduje się na temat 'covid-19' (parametr term)

from Bio import Entrez, SeqIO
Entrez.email = "Your.Name.Here@example.org"

info = Entrez.esearch(db = "pubmed",term = "covid-19")
record = Entrez.read(info)
print('Ilość publikacji: ' + record['Count'])

########### Zadanie 2
#### W bazie danych nucleotide wyszukaj informacje dla kwerendy: 'covid'

info = Entrez.esearch(db = "nucleotide",term = "covid")
record = Entrez.read(info)

#### a) wypisz wszystkie UID  dla w/w kwerendy (key: IdList)

print(record['IdList'])

####  b) dla 3-go znalezionego UID odczytaj (użyj funkcji efetch z parametrem retmode="xml")
#### dodatkowe informacje z bazy "nucleotide"

handle = Entrez.efetch(db="nucleotide", id="1937369466", retmode="xml")
record = Entrez.read(handle)

print(record)

####  (i) nazwę tego biomarkera/cząstki

#'GBSeq_definition': 'Rattus norvegicus C-X-C motif chemokine ligand 2 (Cxcl2), mRNA'

####  (ii) z jakiego organizmu były pobrane próbki do badań

#'GBSeq_source': 'Rattus norvegicus (Norway rat)'