# Entrez jest systemem wyszukiwania online wprowadzonym przez NCBI
# Entrez moduł parsuje XML, zwraca dane w formie list() lub dict()
#
from Bio import Entrez, SeqIO
Entrez.email = "Your.Name.Here@example.org" # wskaż osobę wykazującą zapytania
# podstawowe informacje np. bazy danych
#info = Entrez.einfo() # funkcje wyszukiwania danych: einfo or esearch, efetch, ...
#record = Entrez.read(info)
#print(record)  # key: DbList - wykaz dostępnych baz danych
#info.close()



### pełny wykaz funkcji i parametrów dostępu dla w/w funkcji
##  https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch

# wyszukiwanie danych
#info = Entrez.esearch(db = "pubmed",term = "genome")  # m.in przedstawia listę identyfikatorów UID pasujących do zapytania tekstowego
#record = Entrez.read(info)
#print(record)
# Wyszukiwanie bez podania bazy danych
#info = Entrez.egquery(term = "genome")
#record = Entrez.read(info)
#print(record)
#print(record['eGQueryResult'][0]['DbName'])

## efetch do wyszukiwania i pobierania pełnych szczegółów rekordu z Entrez.
### UID stanowi wartość parametru funkcji id
#handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
#print(handle.readline().strip())

#handle = Entrez.efetch(db = "nucleotide", id = "EU490707", rettype = "fasta")
#record = SeqIO.read( handle, "fasta")
#print(record)

###  podsumowanie wyszukanych dokumentów dla listy wejściowych identyfikatorów UID
#info = Entrez.esummary(db="pubmed", id="19304878,14630660", retmode="xml")
#records = Entrez.parse(info)
#### uwaga przy odczycie zwracaj uwagę na typy/klasy argumentów wyjściowych
### wykorzystaj pętlę lub funkcję next dla 'generator'
### możesz wykorzystać też metody https://biopython.readthedocs.io/en/latest/api/Bio.Entrez.Parser.html
### dla 'Bio.Entrez.Parser.DictionaryElement'

# for record in records:
#     # each record is a Python dictionary or list.
#     print(record)



# info.close()

##########Zadanie 1
## Połącz się z Entrez - systemem wyszukiwania informacji w NCBI.
## Sprawdż ile publikacji w bazie PubMed znajduje się na temat 'covid-19' (parametr term)

info = Entrez.esearch(db = "pubmed",term = "covid-19")
record = Entrez.read(info)
print(record['Count'])

########### Zadanie 2
#### W bazie danych nucleotide wyszukaj informacje dla kwerendy: 'covid'
info = Entrez.esearch(db = "nucleotide",term = "covid")
record = Entrez.read(info)

#### a) wypisz wszystkie UID  dla w/w kwerendy (key: IdList)
# print(record)
print(record['IdList'])

####  b) dla 3-go znalezionego UID odczytaj (użyj funkcji efetch z parametrem retmode="xml")
#### dodatkowe informacje z bazy "nucleotide"
info = Entrez.efetch(db="nucleotide", id="1937369466", retmode="xml")
record = Entrez.read(info)
print(record)

####  (i) nazwę tego biomarkera/cząstki
#'GBReference_title': 'Staphylococcus aureus infected embolic stroke upregulates Orm1 and Cxcl2 in a rat model of septic stroke pathology'

####  (ii) z jakiego organizmu były pobrane próbki do badań
#'GBSeq_organism': 'Rattus norvegicus'



