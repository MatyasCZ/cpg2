


if __name__ ==  "__main__":
    print(list(range(1, 10)))
    print(list(range(1, 10, 2)))
    



def my_range(start, stop, step=1):
    vysledek = []
    hodnota = start
    while hodnota < stop:
        vysledek.append(hodnota)
        hodnota += step
    return vysledek

print(my_range(1, 10))
print(my_range(1, 10, 2))

#print(list(enumerate(["a", "b", "c"])))
#print(list(enumerate(["a", "b", "c"], 1)))

def my_enumerate(seznam, start=0):
    vysledek = []
    i = 0
    while i < len(seznam):
        vysledek.append((start+i, seznam[i]))
        print(vysledek)
        i += 1
    return vysledek
