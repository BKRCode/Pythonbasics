"""
AUFGABE:
 
Schreibe ein Programm, mit dem Du Lotto spielen kannst. 6 aus 49.
 
Als Eingabe müssen 6 unterschiedliche Zahlen zwischen 1 und 49 aufgenommen werden. Als siebte Zahl erfolgt dann die Angabe der Superzahl (0 - 9)
 
In einer danach folgenden Schleife sollen per Zufallsgenerator ebenso 6 unterschiedliche(!) Zahlen gezogen und eine Superzahl ermittelt werden. Eine count Variable soll die Anzahl der insgesamten Durchläufe anzeigen.
 
Jede Gewinnkombination soll auf der Konsole ausgegeben werden.
 
Die Schleife ist fertig, wenn 6 Richtige inkl. Superzahl gezogen wurden. Dann die Gewinnkombination ausgeben und die Anzahl der Ziehungen.

Bonus aufgabe: Ende des Durchlaufes soll auch ausgegeben werden, wie oft welche Gewinncombo gezogen wurde
"""
import random

def lotto_spiel():
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            number = int(input("Gib eine Zahl zwischen 1 und 49 ein: "))
            if 1 <= number <= 49 and number not in user_numbers:
                user_numbers.add(number)
            else:
                print("Falsche Eingabe, bitte eine Zahl zwischen 1 und 49 eingeben, die noch nicht gewählt wurde.")
        except ValueError:
            print("Bitte eine auswertbare Zahl eingeben.")

    while True:
        try:
            superzahl = int(input("Gib die Superzahl (0 bis 9) ein: "))
            if 0 <= superzahl <= 9:
                break
            else:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 0 und 9 eingeben.")
        except ValueError:
            print("Bitte eine auswertbare Zahl eingeben.")

    user_numbers = sorted(user_numbers)
    print(f"Deine Zahlen: {user_numbers} und Superzahl: {superzahl}")

    count = 0
    gewinn_klassen = {
        "6 Richtige + SZ": 0,
        "6 Richtige": 0,
        "5 Richtige + SZ": 0,
        "5 Richtige": 0,
        "4 Richtige + SZ": 0,
        "4 Richtige": 0,
        "3 Richtige + SZ": 0,
        "3 Richtige": 0,
        "2 Richtige + SZ": 0,
    }

    try:
        while True:
            count += 1

            draw_numbers = set(random.sample(range(1, 50), 6))
            draw_superzahl = random.randint(0, 9)

            richtige = len(user_numbers & draw_numbers)
            superzahl_treffer = (draw_superzahl == superzahl)

            if richtige == 6 and superzahl_treffer:
                gewinn_klassen["6 Richtige + SZ"] += 1
                print(f"Herzlichen Glückwunsch! Sie haben die Gewinnkombination nach {count} Ziehungen erreicht!")
                break
            elif richtige == 6:
                gewinn_klassen["6 Richtige"] += 1
            elif richtige == 5 and superzahl_treffer:
                gewinn_klassen["5 Richtige + SZ"] += 1
            elif richtige == 5:
                gewinn_klassen["5 Richtige"] += 1
            elif richtige == 4 and superzahl_treffer:
                gewinn_klassen["4 Richtige + SZ"] += 1
            elif richtige == 4:
                gewinn_klassen["4 Richtige"] += 1
            elif richtige == 3 and superzahl_treffer:
                gewinn_klassen["3 Richtige + SZ"] += 1
            elif richtige == 3:
                gewinn_klassen["3 Richtige"] += 1
            elif richtige == 2 and superzahl_treffer:
                gewinn_klassen["2 Richtige + SZ"] += 1

            if count % 100000 == 0:
                print(f"Fortschritt: {count} Ziehungen durchgeführt...")

    except KeyboardInterrupt:
        print(f"Das Programm wurde nach {count} Ziehungen gestoppt.")
    
    print("\nErgebnisse der Gewinnklassen:")
    for klasse, anzahl in gewinn_klassen.items():
        print(f"{klasse}: {anzahl} mal gezogen")

lotto_spiel()
