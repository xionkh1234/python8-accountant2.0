import sys

from mainhelper import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.saldo(sys.argv[2], sys.argv[3])

magazyn.save_saldo("saldo", sys.argv[2], sys.argv[3])
