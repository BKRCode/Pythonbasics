# Eingabe fuer Anwendende ermoeglichen


alter = 49

if (alter>=18):
    "Du bist voll und jährig!"

"""
Durch Usereingaben wird es dynamisch
'eingabe' muss überprüft werden, ob ein Zahlenwert enthalten ist
erst wenn die Eingabe ein numeraler Wert ist, wird die 
Fallunterscheidung vorgenommen
"""
eingabe = input("Wie alt bist Du?: ")

if (int(eingabe) >= 18):
    print("Du bist voll und jährig!")
else:
    print("Du bist zu jung")

print(eingabe)

def check_eingabe():
    while True:
        eingabe = input("Wie alt Bist du?: ")
        try:
            zahl = int(eingabe)
            if zahl < 0:
                print ("Die Zahl ist negativ.")
            elif zahl == 0:
                print("Die Zahl ist null..")
            else:
                print("Die Zahl ist positiv.")
            break
        except ValueError:
            print("Unglültige Eingabe :(")
check_eingabe()
