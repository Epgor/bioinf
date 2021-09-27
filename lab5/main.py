import numpy as np
import ast

def create_matrix(s1, s2, dct, pen):
    matrix = np.zeros([len(s1)+1,len(s2)+1],dtype=int)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] = max(matrix[i-1][j-1] + dct[s1[i-1]][s2[j-1]], matrix[i-1][j]-pen, matrix[i][j-1]-pen, 0)
    return matrix

def highest_value(matrix):
    temp = 0
    posx = 0
    posy = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] > temp:
                temp = matrix[i][j]
                posx = i
                posy = j
    return posx, posy

def penalty(init_pen, nr_of_gaps, gap_pen):
    return init_pen + nr_of_gaps*gap_pen

def load_seq(file):
    sekwencja=[]
    plik1=open(file, "r").readlines()
    for linia in plik1[1:]:
        sekwencja += linia.rstrip()
    return sekwencja
    
def load_blosum64(file):
    text =open(file, "r").read()
    slownik = ast.literal_eval(text)
    return slownik

def create_string(matrix, seq1, seq2, x, y, d):
    pos_x = x
    pos_y = y
    string1=''
    string2=''
    while True:
        if matrix[pos_x-1][pos_y-1] == max(matrix[pos_x-1][pos_y],matrix[pos_x][pos_y-1],matrix[pos_x-1][pos_y-1]):             
            string1 += seq1[pos_x-1]
            string2 += seq2[pos_y-1]       
            pos_x -=1
            pos_y -=1

        elif matrix[pos_x][pos_y]-1 == max(matrix[pos_x-1][pos_y],matrix[pos_x][pos_y-1],matrix[pos_x-1][pos_y-1]):
            string1 += "-"
            string2 += seq2[pos_y-1]
            pos_y -=1

        elif matrix[pos_x-1][pos_y] == max(matrix[pos_x-1][pos_y],matrix[pos_x][pos_y-1],matrix[pos_x-1][pos_y-1]):       
            string1 += seq1[pos_x-1]
            string2 += "-"      
            pos_x -=1 

        if pos_x | pos_y  == 0:
            break
        
    return string1[::-1], string2[::-1]
        
def main():
    d = -4
    seq1 = load_seq('seqProtein1.fasta')
    seq2 = load_seq('seqProtein2.fasta')
    
    blosum62 = load_blosum64('blosum62.txt')
    
    matrix = create_matrix(seq1, seq2, blosum62, d)
    
    x, y = highest_value(matrix)
    print(matrix)
    print(x, y)
    string1, string2 = create_string(matrix, seq1, seq2, x, y, d)
    print(string1)
    print(string2)
    print("end")

      
if __name__ == '__main__':
    main()