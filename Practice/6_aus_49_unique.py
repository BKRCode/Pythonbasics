import random

def treffer(ziehung, tipp):
    return len([zahl for zahl in tipps if zahl in ziehung ])

def rnd_ganzzahl(start = 1, end = 49):
    return int(random.random()* (end - start + 1) + start)

# Wie kann ich nun 6 Unterschiedliche Zahlen zufällig generieren?


lottoziehung = []

while (len(lottoziehung )< 6):
    zufallszahl = rnd_ganzzahl()
    if zufallszahl not in lottoziehung : 
        lottoziehung .append(zufallszahl)
lottoziehung .sort()
print(lottoziehung )

tipps = [12, 43, 3, 17, 39, 49]

print (treffer([45, 48, 12, 18, 3, 39], tipps))