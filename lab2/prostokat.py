print(' Przykład 6. Utwórz klasę Prostokat, ktora bedzie miała możliwość obliczenia pola powierzchni '
      'prostokąta o bokach dowolnie zdefiniowanych przez użytkownika, początkowe wartości boków ustaw na 2 i 5')

# Comment / Uncomment the code    Ctrl+/
      
##### Wariant 1
class Prostokat:
    def __init__(self):  # konstruktor
        self.bokA = 2
        self.bokB = 5
        #return(print('Poczatkowe wartosci bokow to a = ' + str(self.bokA) + ' oraz b = ',str(self.bokB)))
    def podajBokA(self,podanybokA):
        self.bokA = podanybokA
    def podajBokB(self, podanybokB):
        self.bokB = podanybokB
    def pole(self):
        S = self.bokA * self.bokB
        return(print('Pole wynosi: '+ str(S)))

mojProstokat = Prostokat()
mojProstokat.pole()  # bez ustawiania wartości boku A i B, program korzysta z wartości początkowych
mojProstokat.podajBokA(10)  # ustawianie wartości boku A, początkowa wartość 2 zamieniana jest na 10
mojProstokat.podajBokB(20)  # ustawianie wartości boku B, początkowa wartość 5 zamieniana jest na 20
mojProstokat.pole()

#### Wariant 2
class Prostokat():
    def __init__(self):
        self.bokA = 2
        self.bokB = 5
    def podajBoki(self,bokA,bokB):
        self.bokA = bokA
        self.bokB = bokB
    def pole(self):
        S = self.bokA * self.bokB
        return(print('Pole wynosi: '+ str(S)))

# mojProstokat = Prostokat()
# mojProstokat.pole()
# mojProstokat.podajBoki(3,5)
# mojProstokat.pole()

# #### Wariant 3
class Prostokat():
    def __init__(self,bokA,bokB):
        self.bokA = bokA
        self.bokB = bokB
    def pole(self):
        S = self.bokA * self.bokB
        return(print('Pole wynosi: '+ str(S)))

# mojProstokat = Prostokat(2,5)
# mojProstokat.pole()