#AUFGABE:
 
#Schreibe ein Programm, mit dem Du Lotto spielen kannst. 6 aus 49.
 
#Als Eingabe müssen 6 unterschiedliche Zahlen zwischen 1 und 49 aufgenommen werden. Als siebte Zahl erfolgt dann die Angabe der Superzahl (0 - 9)
 
#In einer danach folgenden Schleife sollen per Zufallsgenerator ebenso 6 unterschiedliche(!) Zahlen gezogen und eine Superzahl ermittelt werden. Eine count Variable soll die Anzahl der insgesamten Durchläufe anzeigen.
 
#Jede Gewinnkombination soll auf der Konsole ausgegeben werden.
 
#Die Schleife ist fertig, wenn 6 Richtige inkl. Superzahl gezogen wurden. Dann die Gewinnkombination ausgeben und die Anzahl der Ziehungen.

import random

def lotto_spiel():
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            number = int(input("Gib eine Zahl zwischen 1 und 49 ein."))
            if 1 <= number <= 49 and number not in user_numbers:
                user_numbers.add(number)
            else:
                print("Flasche Eingabe, bitte eine Zahl zwischen 1 und 49 eingeben, die noch nicht gewählt wurde.")
        except ValueError:
            print ("Bitte eine auswertbare Zahl eingeben.")


    while True:
        try:
            superzahl = int(input("Gib die Superzahl (0 bis 9) ein: "))
            if 0 <= superzahl <= 9:
                break
            else:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 0 und 9 eingeben.")
        except ValueError:
            print("Bitte eine auswertbare Zahl eingeben.")
    
    user_numbers = list(user_numbers)
    user_numbers.sort()
    print(f"Deine Zahlen: {user_numbers} und Superzahl: {superzahl}")

    count = 0
    while True:
        count += 1

        draw_numbers = random.sample(range(1,50), 6)
        draw_numbers.sort()
        draw_superzahl = random.randint(0, 9)
        print (f"Ziehung {count}: Zahlen: {draw_numbers} Superzahl: {draw_superzahl}")

        if set(draw_numbers) == set(user_numbers) and draw_superzahl == superzahl:
            print(f"Herzlichen Glückwunsch! Sie haben die Gewincombination aus {count} Ziehungen gewonnen! ")
            break
        
lotto_spiel()
