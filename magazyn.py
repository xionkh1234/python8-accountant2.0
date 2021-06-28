import sys

from mainhelper import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.magazyn(sys.argv[2:])
