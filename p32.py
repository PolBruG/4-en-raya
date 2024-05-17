import string
import random
def filtreNumFiles(f):
    """
    Filtra un nombre per tal de que sigui un nombre vàlid com a valor de fila
    >>> filtreNumFiles('24')
    24
    >>> filtreNumFiles('2')
    Enter a valid integer of lines of the gameboard (minimum 4): Enter an INTEGER of lines of the gameboard (minimum 4): 4
    """
    while 0==0:
        Num=False
        for n in f:
            if n in string.digits:
                Num=True
            else:
                Num=False
                break
        if Num==True:
            f=int(f)
            if f<4:
                f=input("Enter a valid integer of lines of the gameboard (minimum 4): ")
            else:
                return f
        else:
            f=input("Enter an INTEGER of lines of the gameboard (minimum 4): ")

def filtreNumColumnes(c):
    """
    Filtra un nombre per tal de que sigui un nombre vàlid com a valor de columna
    >>> filtreNumColumnes('24')
    24
    >>> filtreNumColumnes('2')
    Enter a valid integer of columns of the gameboard (minimum 4): Enter an INTEGER of columns of the gameboard (minimum 4): 4
    """
    while 0==0:
        Num=False
        for n in c:
            if n in string.digits:
                Num=True
            else:
                Num=False
                break
        if Num==True:
            c=int(c)
            if c<4:
                c=input("Enter a valid integer of columns of the gameboard (minimum 4): ")
            else:
                return c
        else:
            c=input("Enter an INTEGER of columns of the gameboard (minimum 4): ")

def crearTaulell(f,c):
    """inicialitza el Taulell fxc qualsevol
    >>> crearTaulell(6,7)
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    """
    m = []
    for i in range(f):
        ll = [0] * c  # Crea una nueva lista ll con c ceros
        m.append(ll)
    return m


def escriuTaulell(m,c,f):
    """
    Mostra el taulell en un format adequat
    >>> escriuTaulell ([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],5,5)
    El taulell del joc
          0   1   2   3   4   
    --------------------------------
    4 --> 0   0   0   0   0   0
    3 --> 0   0   0   0   0   0
    2 --> 0   0   0   0   0   0
    1 --> 0   0   0   0   0   0
    0 --> 0   0   0   0   0   0
    """
    s="El taulell del joc"
    p=""
    i=0
    while i<c:
        p+=str(i)+" "*(4-len(str(i)))
        i+=1
    l="-"*(6+(4*c)+6)
    print(s)
    print(" "*5,p)
    print(l)
    for i in range(len(m)):
        if len(m)-i<=10:
            print(len(m) - i - 1, "-->", end=" ")
        elif len(m)-i<=100:
            print(len(m) - i - 1, "->", end=" ")
        else:
            print(len(m) - i - 1, ">", end=" ")
        print("   ".join(str(x) for x in m[i]))

        

def checkNumber(x):
    """
    Retorna True si es un nombre enter vàlid
    >>> checkNumber("11")
    True
    >>> checkNumber("1")
    True
    >>> checkNumber("a")
    False
    >>> checkNumber("un")
    False
    """
    Num=False
    for i in x:
        if i in string.digits:
            Num=True
        else:
            return False
    return Num


def colocarfitxa(m,jugador,f,c,bot):
    """
    Coloca una fitxa del jugador corresponent a una columna lliure i dins dels parametres de la llista
    """
    y=3
    import random
    fs=f-1
    cs=c-1
    j1=1
    j2=2
    if not bot:
        p=input("Escriu la posició de la fitxa: ")
        pl=checkNumber(p)
        while not pl:
            p=input("Escriu un valor numèric com a posició de la fitxa: ")
            pl=checkNumber(p)   
        p=int(p)
        while p>cs:
            p=input("Escriu una columna dins linterval [0,"+str(cs)+"] la posicio de la fitxa: ")
            pl=checkNumber(p)
            while not pl:
                p=input("Escriu un valor numèric com a posició de la fitxa: ")
                pl=checkNumber(p)
                print(pl)
            p=int(p)
        p=int(p)
        while m[fs][p]==j1 or m[fs][p]==j2:
            fs-=1
            if fs<0:
                print("Columna plena, inserta en una columna lliure")
                m=colocarfitxa(m,jugador,f,c,bot)
                break    
        if jugador:
            m[fs][p]=1
        else:
            m[fs][p]=2
        return m


    
    elif bot:
        if jugador==True:
            p=input("Escriu la posició de la fitxa: ")
            pl=checkNumber(p)
            while not pl:
                p=input("Escriu un valor numèric com a posició de la fitxa: ")
                pl=checkNumber(p)   
            p=int(p)
            while p>cs:
                p=input("Escriu una columna dins linterval [0,"+str(cs)+"] la posicio de la fitxa: ")
                pl=checkNumber(p)
                while not pl:
                    p=input("Escriu un valor numèric com a posició de la fitxa: ")
                    pl=checkNumber(p)
                    print(pl)
                p=int(p)
            p=int(p)
            while m[fs][p]==j1 or m[fs][p]==j2:
                fs-=1
                if fs<0:
                    print("Columna plena, inserta en una columna lliure")
                    m=colocarfitxa(m,jugador,f,c,bot)
                    break    
            if jugador:
                m[fs][p]=1
            else:
                m[fs][p]=2
            return m
        
        if not jugador:
            p=str(random.randint(0,int(c)))
            pl=checkNumber(p)
            while not pl:
                p=str(random.randint(0,int(c)))
                pl=checkNumber(p)   
            p=int(p)
            while p>cs:
                p=str(random.randint(0,int(c)))
                pl=checkNumber(p)
                while not pl:
                    p=str(random.randint(0,int(c)))
                    pl=checkNumber(p)
                    print(pl)
                p=int(p)
            p=int(p)
            while m[fs][p]==j1 or m[fs][p]==j2:
                fs-=1
                if fs<0:
                    print("Columna plena, inserta en una columna lliure")
                    m=colocarfitxa(m,jugador,f,c,bot)
                    break    
            if jugador:
                m[fs][p]=1
            else:
                m[fs][p]=2
            return m
def options():
    """
    Mostra el menu necessari per jugar al connecta4
    El joc del connecta4
    0. Sortir
    1. Jugar
    """
    x=input("0. Sortir\n1. Jugar\nEscull opció: ")
    while 0==0:
        if x=="1":
            return True
        elif x=="0":
            return False
        x=input("\nOpció incorrecte\n0. Sortir\n1. Jugar\nEscull opció: ")

def check4enliniafiles(m):
    """
    Checkeja si hi ha algun 4 en ratlla a les files d'algun jugador
    >>> check4enliniafiles([[0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    1
    >>> check4enliniafiles([[0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    0
    """
    for fila in m:
        count=False
        times=0
        for v,i in enumerate(fila):
            if i==0:
                count=False
                times=0
            else:
                if count==False:
                    count=True
                    times=1
                else:
                    if fila[v-1]==fila[v]:
                        times+=1
                        if times==4:
                            win=i
                            return win
                    else:
                        times=1
    return False

def check4enliniacolumnes(m,f):
    """
    Checkeja si hi ha algun 4 en ratlla a les columnes d'algun jugador
    >>> check4enliniacolumnes([[0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 0, 0]],5)
    2
    >>> check4enliniacolumnes([[0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0]],5)
    0
    """
    for e,fila in enumerate(m):
        times=0
        for v,i in enumerate(fila):
            times=0
            if i!=0:
                for r in range(4):
                    if (e+r)<f:
                        if m[e+r][v]==i:
                            times+=1
                            if times==4:
                                win=i
                                return win
                        elif m[e+r][v]!=i:
                            count=False
                            times=0
                            break
                    else:
                        break
            else:
                pass
    return False

def check4enlinaDiagonalDEBD(m,f,c):
    """
    Checkeja si hi ha algun 4 en ratlla a les diagonals d'esquerra superior a dreta inferior d'algun jugador
    >>> check4enlinaDiagonalDEBD([[0, 2, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]],5,6)
    2
    >>> check4enlinaDiagonalDEBD([[0, 0, 0, 0, 2, 0], [0, 0, 0, 2, 0, 0], [0, 0, 2, 0, 0, 0], [0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],5,6)
    False
    """
    for i in range(f-3):
        for j in range(c-3):
            if m[i][j]!=0 and m[i][j]==m[i+1][j+1]==m[i+2][j+2]==m[i+3][j+3]:
                return m[i][j]
    return False
            
def check4enlinaDiagonalDDBE(m,f,c):
    """
    Checkeja si hi ha algun 4 en ratlla a les diagonals de dreta superior a esquerra inferior d'algun jugador
    >>> check4enlinaDiagonalDDBE([[0, 2, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]],5,6)
    False
    >>> check4enlinaDiagonalDDBE([[0, 0, 0, 0, 2, 0], [0, 0, 0, 2, 0, 0], [0, 0, 2, 0, 0, 0], [0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],5,6)
    2
    """
    for i in range(f-3):
        for j in range(c-3):
            if m[i][j+3]!=0 and m[i][j+3]==m[i+1][j+2]==m[i+2][j+1]==m[i+3][j]:
                return m[i][j+3]
    return False

def jocacabat(m):
    """
    Detecta si no hi ha més espais per insertar una fitxa
    >>> jocacabat([[0, 2, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]])
    False
    >>> jocacabat([[1, 2, 1, 2, 1, 2], [2, 1, 2, 2, 2, 1], [1, 1, 2, 2, 1, 1], [1, 1, 1, 2, 1, 2], [1, 2, 2, 1, 2, 1]])
    True
    """
    for fila in m:
        for columna in fila:
            if columna==0:
                return False
    return True


def joc(bot):
    """
    Inicialitza el joc 4 en ratlla de dimensions infinites de 2 jugadors
    """
    jugador=True
    f=input("Enter number of lines of the gameboard: ")
    f=filtreNumFiles(f)
    c=input("Enter number of columns of the gameboard: ")
    c=filtreNumColumnes(c)
    m=crearTaulell(f,c)
    while not check4enliniafiles(m) and not check4enliniacolumnes(m,f) and not check4enlinaDiagonalDDBE(m,f,c) and not check4enlinaDiagonalDEBD(m,f,c):
        print('\n')
        k=escriuTaulell(m,c,f)
        print('\n')
        m=colocarfitxa(m,jugador,f,c,bot)
        if jocacabat(m):
            print('\n')
            escriuTaulell(m,c,f)
            print('\nGAME OVER')
            break
        if jugador:
            jugador=False
        elif not jugador:
            jugador=True
    if not jocacabat(m):
        if check4enliniafiles(m)!=False:
            print('\n')
            escriuTaulell(m,c,f)
            print('\n')
            print('Player',check4enliniafiles(m),'made 4 in line')
        elif check4enliniacolumnes(m,f)!=False:
            print('\n')
            escriuTaulell(m,c,f)
            print('\n')
            print('Player',check4enliniacolumnes(m,f),'made 4 in column')
        elif check4enlinaDiagonalDEBD(m,f,c)==1 or check4enlinaDiagonalDEBD(m,f,c)==2:
            print('\n')
            escriuTaulell(m,c,f)
            print('\n')
            print('Player',check4enlinaDiagonalDEBD(m,f,c),'made 4 in diagonal from left above to right')
        elif check4enlinaDiagonalDDBE(m,f,c)==1 or check4enlinaDiagonalDDBE(m,f,c)==2:
            print('\n')
            escriuTaulell(m,c,f)
            print('\n')
            print('Player',check4enlinaDiagonalDDBE(m,f,c),'made 4 in diagonal from right above to left')
        
        
if __name__=='__main__':
    x=options()
    y="3"
    bot=False
    while x:
        while y!="2" or y!="1":
                y=input("2. Jugar vs CPU\n1. Jugar vs altre jugador\nEscull opció: ")
                if y=="2":
                    bot=True
                    joc(bot)
                    break
                elif y=="1":
                    joc(bot)
                    break
        
        print('\n')
        x=options()
    print("\nGame Cancelled")
