import Bio
from Bio.Seq import Seq as sequence
import random
from Bio import SeqIO
import matplotlib.pyplot as plt


#zadanie 1
def create_random():
    #string = "" 
    #losuję z określonego zbioru w 2 wersjach lambda i klasyczna pętla
    s = lambda typy, ile: [ random.choice(typy) for _ in range(ile) ]   #dwie wersje
    string = s(("A", "T", "C", "G"), 20)
    #for _ in range(20):
        #string += random.choice(("A", "T", "C", "G"))
    return "".join(string)
        

def zad1():
    my_seq = sequence(create_random())
    print("Losowa sekwencja: \n", my_seq)
    
    print("Sekwencja komplementara: \n", my_seq.complement())
    
    print("Rewers transkryptu: \n", my_seq.reverse_complement())
    
#zadanie2
def reading(file, type):
    # czytanie w oddzielnej funkcji dla kontroli błędów
    try:
        fasta = SeqIO.parse(file, type)
    except OSError:
        print ("Nie moge otworzyć pliku:", file)

        
    return fasta

def zad2():
    #zmienne pomocnicze
    i = 0
    wanted_seq = ""
    
    #czytam plik i parsuję
    seq = reading("ribosomal_RNA.fasta", "fasta")   
    
    for seq_record in seq: #za pomocą Fastaiteratora, wywołuję kolejno obiekty z kontenera
        
        i+=1 #numerek dla nie wtajemniczonych
        
        print("Dlugość sekwencji nr %d :" %i, len(seq_record))#wypisanie długości wszystkich sewkwencji
        
        if i == 10:#brak adnotacji, więc wypisuję garść informacji
           wanted_seq = str(seq_record.annotations) + "\n"+ \
               str(seq_record.description) + "\n" +\
                    str(seq_record.id) + "\n" +\
                        str(len(seq_record))  + "\n" +\
                            str(repr(seq_record.seq))   #zrzucam wszystko do jednego stringa
        
    print(wanted_seq) #wypisuję
    
def zad3():
    seq = reading("ribosomal_RNA.fasta", "fasta")#ładuję plik
    
    i=0#zmienna pomocnicza
    
    for seq_record in seq:#iteracja przez cąłu kontener
        i+=1
        
        print("[Transkrypt komplementarny]")
        print(seq_record.seq.complement())#transkryt komplementarny
        print("[Transkrypcja]")
        print(seq_record.seq.transcribe())#transkrypcja
        print("[Translacja]")
        print(seq_record.seq.translate())#translacja
        
def file_read(input_file):    #funkcja do odczytu pliku z sekwencją dna
    
    input_dna = "" #deklaruję zmienną, która przechowa wejściowy string
    
    try:    #próbujemy otworzyć plik za pomocą with open, która po wykonaniu automatycznie zamyka plik
        with open(input_file, 'r') as file:    #wykonujemy odczyt pliku, jako "file"
            next(file)  #tutaj pomijam pierwszą linię, gdyż zawiera niepotrzebne informacje
            lines = file.readlines()    #do zmiennej "lines" wczytuję wsztstkie linie pliku
            for one_line in lines:  #pętlą for łapię linia po lini "one_line" <- lines
                input_dna += one_line.rstrip()  #do zmiennej przechowwującej cały string doklejam koleje linie obcinając białe znaki z prawej
    except OSError: #w razie błędu wejściowego pliku np. zła nazwa, zwracam błąd wejscia
        print("Błąd ładowania pliku wejściowego! [Plik Dna]") #wyrzucam stosowny błąd
            
    return input_dna    #funkcja zwraca ciąg znaków będących zasadami azotowymi     
   
def zad4():
       
       big_seq = sequence(file_read("prot.fasta"))#nie udało mi siępobrć całego pliku, mam jego znaczną część
       
       print(repr(big_seq.complement))  #reprezentacja kodu komplementarnego
       
       print(repr(big_seq.reverse_complement))#reprezentacja kodu odwórconego komplementarnego
       
       print(len(big_seq))    #długość sekwencji


def zad5():
    plik = "ribosomal_RNA.fasta"
    seq = reading(plik, "fasta") #ładuję plik
    all_nitro = []
    
    for seq_record in seq:
        all_nitro += list(seq_record.seq) #łączę wszystko w jedną listę
        
    for i in all_nitro:
        if i not in ("A", "T", "C", "G"):   #pozbywam się śmieci
            all_nitro.remove(i)
      
    #definuję histogram :dane, ilosc serii, kolor, przezroczystosc  
    plt.hist(all_nitro, 4, alpha=0.7, histtype = 'stepfilled')
    #plt.bar([0,1,2,3],20000,color = ['black', 'red', 'green', 'blue'])
    #kreski 
    plt.grid(axis='y', alpha=0.75)
    plt.grid(color='white', lw = 0.5, axis='x')
    #etykiety
    
    plt.title('Histogram wystąpień zasad azotowych w pliku %s' %plik)
    plt.xlabel('Zasady Azotowe')
    plt.ylabel('Ilość wystąpień')

    #pokaż wykres
    plt.show()
    

def main():
    print("Używam biblioteki BioPython w wersji:", Bio.__version__)
    #zad1()
    
    #zad2()
    
    #zad3()
    
    #zad4()
    
    zad5()

if __name__ == '__main__':
    main()
