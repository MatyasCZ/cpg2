if __name__ == "__main__":

    inp = input("Zadej cislo: ")
    while inp:
        try:
            print(10 / int(inp))
        except ZeroDivisionError:
            print("Nelze delit nulou")
        inp = input("Zadej cislo: ")


