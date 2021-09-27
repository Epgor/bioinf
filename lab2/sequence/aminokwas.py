import ast

TabOfAminos=[]

def dna_to_rna(kdna):
    mdna = []
    rna = []
    for xi in kdna:
        if xi == "A":
            temp = "T"
        elif xi == "T":
            temp = "A"
        elif xi == "C":
            temp = "G"
        elif xi == "G":
            temp = "C"

        mdna.append(temp)
            
    for xi in mdna:    
        if xi == "A":
            temp = "U"
        elif xi == "T":
            temp = "A"
        elif xi == "C":
            temp = "G"
        elif xi == "G":
            temp = "C"

        rna.append(temp)
    return rna

def read_amino():
    try:
        WantedAmino = (str(input()))
    except KeyError:
        print("Oups! Wrong Charter")
        
def tranform_to_kodons(rna):
    opt = []
    for i in range((int(len(rna)/3))):
        opt.append(rna[3*i]+rna[3*i+1]+rna[3*i+2])
    return opt    

def translate_kodons(crna, amino_dict2):
    for i in crna: 
        TabOfAminos.append(amino_dict2.get(i))    
        
def count_occurations(WantedAmino):
    occured=0
    for x in range(len(TabOfAminos)):
        if WantedAmino == TabOfAminos[x]:
            occured+=1
    return occured

def how_many_times_occured():

    
    aminoacids = list(open('seqDNA.txt', 'r').read())
    rna = dna_to_rna(aminoacids)

    amino_dict=open('AminokwasySlownik.txt', 'r').read()
    amino_dict2 = ast.literal_eval(str(amino_dict))

    print("Insert Amino: \n")
    
    try:
        WantedAmino = (str(input()))
    except KeyError:
        print("Oups! Wrong Charter")
        
    coded_rna = tranform_to_kodons(rna)
    translate_kodons(coded_rna, amino_dict2)

    print(count_occurations(WantedAmino))

    

how_many_times_occured()

