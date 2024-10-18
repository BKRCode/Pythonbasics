""" Fakultaet in der Mathematik wird mit ! gekennzeichnet

 5 Fakulaet -> 5!
 5 * 4 * 3 * 2 * 1

 Dazu bite eine Metode definieren. Die Fakultaet soll dabei Variabel sein
"""

def berechne_fakultaet(num):
    if num < 0:
        return "Abbruch"
    elif num == 0 or num == 1:
        return 1
    else:
        fakultaet = 1
        for i in range(2, num + 1):
            fakultaet *= i
        return fakultaet

Num = 5
print(f"{Num}! = {berechne_fakultaet(Num)}")


# 49! / (43! +6!)