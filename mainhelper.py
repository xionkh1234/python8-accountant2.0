import sys

class Magazyn:
    def __init__(self):
        self.konto = 0
        self.products = {}
        self.info = []

    def przeglad(self, start, end):
        for lista in self.info[int(start): int(end)]:
            for item in lista:
                print(item)

    def magazyn(self, product):
        for item in product:
            if item not in self.products:
                self.products[item] = 0
        for product, quantity in self.products.items():
            print("{}: {}".format(product, quantity))

    def saldo(self, wartosc, comment):
        if self.konto + int(wartosc) < 0:
            print("You're run out of money :(.")
            return False
        self.konto += int(wartosc)
        self.info.append(["saldo", wartosc, comment])
        return True

    def zakup(self, product, wartosc, quantity):
        if self.konto < int(wartosc) * int(quantity):
            print("You're run out of money :(.")
            return False
        self.konto -= int(wartosc) * int(quantity)
        self.products[product] = + int(quantity)
        self.info.append(["zakup", product, wartosc, quantity])
        return True

    def sprzedaz(self, product, wartosc, quantity):
        if product not in self.products:
            print("Not enough products.")
            return False
        if self.products[product] < quantity:
            print("Not enough quantity.")
            return False
        else:
            self.products[product] -= quantity
        self.konto += int(wartosc) * int(quantity)
        self.info.append(["sprzedaz", product, wartosc, quantity])
        return True

    def wczytaj(self, typ):
        with open(typ) as data:
            while True:
                act = data.readline().rstrip()
                if not act:
                    break

                elif act == "saldo":
                    operation = int(data.readline().rstrip())
                    comment = data.readline().rstrip()
                    self.saldo(operation, comment)

                elif act == "zakup":
                    product = str(data.readline().rstrip())
                    price = int(data.readline().rstrip())
                    quantity = int(data.readline().rstrip())
                    self.zakup(product, price, quantity)

                elif act == "sprzedaz":
                    product = str(data.readline().rstrip())
                    price = int(data.readline().rstrip())
                    quantity = int(data.readline().rstrip())
                    self.sprzedaz(product, price, quantity)

                elif act == "stop":
                    break

    def save_saldo(self, act, operation, comment):
        with open("in.txt", "r") as dane:
            id = dane.readlines()
            id.insert(-1, (str(act) + "\n"))
            id.insert(-1, (str(operation) + "\n"))
            id.insert(-1, (str(comment) + "\n"))

        with open("in.txt", "w") as dane:
            id = "".join(id)
            dane.write(id)

    def save_sellbuy(self, act, product, price, quantity):
        with open("in.txt", "r") as data:
            id = data.readlines()
            id.insert(-1, (str(act) + "\n"))
            id.insert(-1, (str(product) + "\n"))
            id.insert(-1, (str(price) + "\n"))
            id.insert(-1, (str(quantity) + "\n"))

        with open("in.txt", "w") as data:
            data = "".join(id)
            data.write(id)
