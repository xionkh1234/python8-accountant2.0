from mainhelper import save_saldo, save_zakup, save_sprzedaz, stop, wrapper

with open("in.txt") as data:

    konto = {"saldo": 0}
    magazyn = []

    while True:
        act = data.readline().rstrip()
        if not act:
            break

        elif act == "saldo":
            operation = int(data.readline().rstrip())
            comment = data.readline().rstrip()
            if konto["saldo"] + operation < 0:
                print("Niewystarczające środki na koncie.")
                break
            konto["saldo"] += operation
            save_saldo(act, operation, comment)

        elif act == "zakup":
            product = str(data.readline().rstrip())
            price = int(data.readline().rstrip())
            quantity = int(data.readline().rstrip())
            if konto["saldo"] < price * quantity:
                print("Niewystarczające środki na koncie.")
                break
            else:
                konto["saldo"] -= price * quantity
            towar = {}
            towar[produkt] =+ quantity
            magazyn.append(towar)
            save_zakup(act, product, price, quantity)

        elif act == "sprzedaz":
            product = str(data.readline().rstrip())
            price = int(data.readline().rstrip())
            quantity = int(data.readline().rstrip())
            if product not in towar:
                print("Brak towaru w magazynie.")
                break
            if towar[product] < ilosc:
                print("Niewystarczająca ilość sztuk.")
                break
            else:
                towar[product] -= quantity
            konto["saldo"] += price * quantity
            save_sprzedaz(act, product, price, quantity)

        elif act == "stop":
            stop(act)
            break


