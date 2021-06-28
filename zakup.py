import sys

from mainhelper import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.zakup(sys.argv[2], sys.argv[3], sys.argv[4])

magazyn.save_sellbuy("zakup", sys.argv[2], sys.argv[3], sys.argv[4])
