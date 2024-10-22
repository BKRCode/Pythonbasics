"""
Ausgangssituation: Ich bin Zuschauer eines vergangeng Spektakels, in einem Land, vor unserer Zeit. Ihr Rang ist Informatikus, doch lesen Sie zunächst die Geschichte...

König, 
100 prisoners
schrank mit 100 schubladen, 1-100 Nummeriert (1, 101)
100 kleine Holzplättchen, 1-100 Nummeriert
Jeder Prisoner, 50 Schubladen aufmachen, von 100, wenn zahl gefunden, nächster prisoner, wenn letzter gefunden dann- alle befreit.

Wenn nicht - 5 Random befreit.

keine print im ganzen code. 

Repeat 10000.
Count: Alle befreit.
"""

import random


print("Willkommen in der Jährlichen ziehung:  'WHO GETS TO WALK!' ")
print("Wird das Gefähngniss leer sein oder schaffen es nur wieder 5 Gewinner?")

erfolgreiche_runs = 0
only_five_will_Walk = 0

for _ in range(10000):
    schublade = list(range(1, 101))
    random.shuffle(schublade)

    alle_Gefangenen_frei = True

    for prisoner in range(1, 101):
        schublade_aufmachen = prisoner
        for _ in range(50):
            nummer_in_schublade = schublade[schublade_aufmachen - 1]
            if nummer_in_schublade == prisoner:
                break
            else:
                schublade_aufmachen = nummer_in_schublade
        else:
            alle_Gefangenen_frei = False
            break

    if alle_Gefangenen_frei:
        erfolgreiche_runs += 1
    else:
        only_five_will_Walk +=1


print(f"Nach 10000 jahren wurden {only_five_will_Walk} mal nur 5 befreit.. und {erfolgreiche_runs} mal alle befreit..")





