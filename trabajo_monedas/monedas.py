class Coin:
    list = []

    def __init__(self, country, name, code):
        self.country = country
        self.name = name
        self.code = code

    def registration(self):
        print("Registro de moneda:")
        c = input("Ingrese el nombre del país:")
        n = input("Ingrese el nombre de la moneda:")
        co = input("Ingrese el codigo de la moneda:")
        C = Coin(c, n, co)
        list.append(C)

    def show(self):
        k = 0
        while k < len(list):
            print(list[k].country, "", list[k].name, "", list[k].code)
            k += 1
