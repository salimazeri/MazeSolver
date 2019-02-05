import os
clear = lambda : os.system('clear') # or clear for Linux
from collections import namedtuple

Dir = namedtuple("Dir", ["dy", "dx"])
RIGHT = Dir(0,  1)
DOWN  = Dir(1,  0)
LEFT  = Dir(0, -1)
UP    = Dir(-1,  0)
DIRS  = [RIGHT, DOWN, LEFT, UP]
OPEN  = {" ", "@"}

def wlasciwosci(plik):
    '''
    Funkcja zwracająca wysokość, szerokość labiryntu oraz listę dwuwymiarową
    gdzie elementy tablicy nadrzędnej to rzędy a elementy tablic podrzędnych to odpowiednie kolumny
    Wejście: nazwa plkiu wraz z typem pliku (String)
    Wyjście: lista
    '''
    try:
        plik = open(plik, "r")
    except IOError:
        print ('Problem z plikiem ', plik)
        
    labirynt = []
    #ignoruje pierwszą linię
    for line in plik.readlines()[1:]:
        labirynt.append(list(line))
    #print (labirynt)
    plik.seek(0)
    wysokosc =  ''.join(list(plik.read()[0:2]))
    plik.seek(0)
    szerokosc =  ''.join(list(plik.read()[3:5]))
    
    return (wysokosc, szerokosc, labirynt)

def start_pos(plik):
    '''
    
    '''
    wysokosc = wlasciwosci(plik)[0]
    szerokosc = wlasciwosci(plik)[1]
    labirynt = wlasciwosci(plik)[2]
    #print (labirynt)
    y = -1
    x = -1
    for line in labirynt:
        y += 1
        x = -1
        for char in line:
            x += 1
            if char == '@':
                return [x,y]

def droga(labirynt,y,x):
    
    if labirynt[y][x] == '$':
        print ('znalazlem wyjscie')
        return True
    elif labirynt[y][x] == '#':
        print ('sciana')
        return False
    elif labirynt[y][x] == '.':
        print ('Juz tu bylem')
        return False
    
    labirynt[y][x] = '.'
    print ('wykonalem krok')
    
    print (pokaz_labirynt(labirynt))
    if ((x < len(labirynt[0])-1 and droga(labirynt, y, x+1))
        or (y > 0 and droga(labirynt, y-1, x))
        or (x > 0 and droga(labirynt, y, x-1))
        or (y < len(labirynt)-1 and droga(labirynt, y+1, x))):
            return True
    return False
        
        
def pokaz_labirynt(labirynt):
    labirynt_ = []
    for line in labirynt:
        temp = ''
        for char in line:
            temp += str(char)
        labirynt_.append(temp)
    return ''.join(labirynt_)

def test_(nazwa_pliku):
    labirynt = wlasciwosci(nazwa_pliku)[2]
    print (pokaz_labirynt(labirynt))
    sy = start_pos(nazwa_pliku)[1]
    sx = start_pos(nazwa_pliku)[0]
    droga(labirynt,sy,sx)

def test():
    test_('labirynt0.txt')
    test_('labirynt1.txt')
    test_('labirynt2.txt')
    test_('labirynt3.txt')
    test_('labirynt4.txt')
    test_('labirynt5.txt')
    test_('labirynt6.txt')


test()





