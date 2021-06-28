import sys

from mainhelper import Magazyn

magazyn = Magazyn()
magazyn.wczytaj(sys.argv[1])

print(magazyn.konto)

