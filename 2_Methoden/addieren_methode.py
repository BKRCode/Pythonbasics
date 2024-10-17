# Methoden Funktionen Prozeduren

def addiere (zahl_1, zahl_2):
    return zahl_1 + zahl_2
print(addiere(5, 7))



# Addieren von Listenwerten


def sum_liste(liste):
    sum = 0
    for zahl in liste:
        sum += zahl
    return sum
    
zahlen =[23, 42, 187, 420, 17]

sum = sum_liste(zahlen)
print(sum)

