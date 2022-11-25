from monedas import Coin


def main():
    i = 0
    while i == 0:
        print("Seleccione una opcion:\n")
        print("1.-Agregar moneda")
        print("2.-Mostrar lista")
        print("3.-Salir")
        option = int(input())

        if option == 1:
            registration()
        elif option == 2:
            show()
        elif option == 3:
            print("Saliendo.")
            exit()
        else:
            print("Opción invalida.")


main()
