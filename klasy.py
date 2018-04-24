from random import *


class Osobnik:
    def __init__(self, długość):
        self.długość = długość
        self.tablica = []
        for i in range(0, długość):
            self.tablica += [randrange(2)]

    def __str__(self):
        return str(self.tablica)

    def funkcja_przystosowania(self, pojemnosc, tablica_wag):
        suma = 0
        for i in range(0, len(self.tablica)):
            suma += tablica_wag[i] * self.tablica[i]
            i += 1
        if ((suma > 0) and (suma <= pojemnosc)):
            wartoscf = suma
        elif ((suma > pojemnosc) and (suma <= 2 * pojemnosc)):
            wartoscf = 2 * pojemnosc - suma
        else:
            wartoscf = 0
        return wartoscf

    def mutuj(self):
        miejsce = randrange(0, self.długość)
        self.tablica[miejsce] = int(not (self.tablica[miejsce]))


class Populacja:
    def __init__(self, wielkość, rozmiar_osobnika):
        self.wielkość = wielkość
        self.osobniki = []
        self.najlepszy=None
        self.najlepsze_przystosowanie=-1
        for i in range(0, wielkość):
            self.osobniki += [Osobnik(rozmiar_osobnika)]

    def selekcja(self, pojemnosc, tab):
        if min(tab)<0:
                raise AttributeError
        nowa_tablica = []
        tablica_wartosci_przystosowan=[]
       # tablica_wartosci_przystosowan = [i.funkcja_przystosowania(pojemnosc, tab) for i in self.osobniki]
        for i in range(0,len(self.osobniki)):
            wartosc=self.osobniki[i].funkcja_przystosowania(pojemnosc,tab)
            if wartosc>self.najlepsze_przystosowanie:
                self.najlepsze_przystosowanie=wartosc
                self.najlepszy=self.osobniki[i]
            tablica_wartosci_przystosowan+=[wartosc]

        suma = sum(tablica_wartosci_przystosowan)
        for i in range(0, len(self.osobniki)):
            a = randrange(suma + 1)
            sumsum = 0
            j = 0
            while (sumsum < a):
                sumsum += tablica_wartosci_przystosowan[j]
                j += 1

            nowa_tablica += [self.osobniki[max(0, j - 1)]]
            # nowa_tablica.append(self.osobniki[max(0, j-1)])
        self.osobniki = nowa_tablica

    def __str__(self):
        return str(self.osobniki)

    def krzyzowanie(self, prawdopodobienstwo):
        a, b = 0, 1
        while (b < len(self.osobniki[0].tablica)):
            r = randrange(0, 100) / 100
            if r <= prawdopodobienstwo:
                miejsce = randrange(1, len(self.osobniki[0].tablica) - 1)
                no1 = self.osobniki[a].tablica[0:miejsce] + self.osobniki[b].tablica[miejsce::]
                no2 = self.osobniki[b].tablica[0:miejsce] + self.osobniki[a].tablica[miejsce::]
                self.osobniki[a].tablica = no1
                self.osobniki[b].tablica = no2
                a += 2
                b += 2

    def __str__(self):
        return str(list(map(str, self.osobniki)))

    def mutacja(self, prawdopodobienstwo):
        for i in range(0, self.wielkość):
            p = randrange(0, 100) / 100
            if p <= prawdopodobienstwo:
                self.osobniki[i].mutuj()
