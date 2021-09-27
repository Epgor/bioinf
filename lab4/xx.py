def Przekatna(n1,n2):
    if(n1 == n2):
        return 1 # match
    else:
        return -1 # mismatch

def nowa(s1,s2, gap = -1):
    n = len(s1) + 1
    m = len(s2) + 1

    al_mat = [[0 for i in range(n)] for j in range(m )]
    for i in range(m):
            al_mat[i][0] = gap * i

    for j in range (n):
        al_mat[0][j] = gap * j

    for i in range(1,m):
        for j in range(1,n):
            litery = al_mat[i-1][j-1] + Przekatna(s1[j-1],s2[i-1])
            w_dol = al_mat[i][j-1] + gap
            w_prawo = al_mat[i-1][j] + gap
            al_mat[i][j] = max(litery,w_dol,w_prawo)

    for line in al_mat:
        print(line)


x = 'GATACTA'
y = 'GATTACCA'
nowa(x,y)