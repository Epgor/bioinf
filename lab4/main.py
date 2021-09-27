import numpy as np

def main():
    x = list('TTACG ')
    y = list('TTTCT')

    D = 2

    matrix = np.zeros([len(x)+1,len(y)+1],dtype=int)

    sim_matrix = matrix.copy()

    for i in range(len(matrix)):
        matrix[i][0] = -i
        
    for i in range(len(matrix[0])):
        matrix[0][i] = -i

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if x[i-1] == y[j-1]:
                sim_matrix[i][j] = 1
            else:
                sim_matrix[i][j] = -1
                
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] = max(matrix[i-1][j-1]+sim_matrix[i][j], matrix[i-1][j]-D, matrix[i][j-1]-D)
    
    pos_x = (len(matrix))-2
    pos_y = (len(matrix[0]))-2  
    string1 = ""
    string2 = ""


            
    while True:
        if matrix[pos_x][pos_y] == max(matrix[pos_x][pos_y+1],matrix[pos_x+1][pos_y],matrix[pos_x][pos_y]):
            if matrix[pos_x][pos_y] >= 1:             
                string1 += x[pos_x-1]
                string2 += y[pos_y-1]
            else:
                string1 += "-"
                string2 += "-"        
            pos_x -=1
            pos_y -=1

        elif matrix[pos_x+1][pos_y] == max(matrix[pos_x][pos_y+1],matrix[pos_x+1][pos_y],matrix[pos_x][pos_y]):
            if matrix[pos_x+1][pos_y] >= 1:
                string1 += "-"
                string2 += y[pos_y-1]
            else:
                string1 += "-"
                string2 += "-"       
            pos_y -=1

        elif matrix[pos_x][pos_y+1] == max(matrix[pos_x][pos_y+1],matrix[pos_x+1][pos_y],matrix[pos_x][pos_y]):
            if matrix[pos_x][pos_y+1] >= 1:         
                string1 += x[pos_x-1]
                string2 += "-"  
            else:  
                string1 += "-"
                string2 += "-"       
            pos_x -=1 


        if pos_x | pos_y  == 0:
            break
        
    print(matrix)

    #print(sim_matrix)
    print(string1[::-1])  
    print(string2[::-1])              
            
            
if __name__ == '__main__':
    main()