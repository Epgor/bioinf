
from Bio import Entrez, SeqIO
Entrez.email = "Your.Name.Here@example.org"
#1
def z1():
    try:
        info = Entrez.esearch(db = "pubmed",term = "covid-19")
        record = len(Entrez.read(info))
        print(record)          
    except Exception:
        print("There was an error :C")

#1.2
def z12():
    try:
        info = Entrez.esearch(db = "nucleotide",term = "covid")
        record = Entrez.read(info)
        #a
        print(record['IdList'])
        #b
        info = Entrez.efetch(db="nucleotide", id=record['IdList'][2], retmode="xml")
        record = Entrez.read(info)
        print(record)
    except Exception:
        print("There was an error :C")
     
   

#2
## Połącz się z Entrez - systemem wyszukiwania informacji w NCBI.
## Wyszukaj informacje o sekwencji  id = 'NC_045512'
## odpowiedz na pytania:
# (a) Jak długa jest sekwencja nukleotydowa?
# (b) Od jakiego organizmu pochodzi?
# (c) Kiedy opublikowano pierwsze wyniki?
# (d) Czy ta sekwencja była kiedykolwiek poprawiana/aktualizowana? (kolejne wersje?)
# (e) Kto jest pierwszym autorem badań sekwencji?
# (f) Gdzie (w jakich czasopismach) opublikowano wyniki badań tej sekwencji po zgłoszeniu w bazie (wszystkie publikacje)
# (g) Jaką część sekwencji opisano jako gen (ang. gene)? Jak długi jest ten fragment? I jaką nazwę genu
# przypisano temu fragmentowi?
# (h) Przełącz się na widok w formacie FASTA. Spróbuj rozszyfrować, co wpisano jako opis sekwencji.
def z2():
    #try:  #b   
    
        handle2 = Entrez.efetch(db = "nucleotide", id = "NC_045512", rettype="gb", retmode="text")   
        record2 = Entrez.read(handle2)
        print(handle2)
        print(record2['eGQueryResult'][0]['DbName'])
    
        handle = Entrez.efetch(db = "nucleotide", id = "NC_045512", rettype = "fasta")   

        record = SeqIO.read( handle, "fasta")
        
        print(len(record))
        
        print(record.description)
        
      
       # print("There was an error :C") 
    
if __name__ == "__main__":
    #z1()
    #z12()
    #z2()