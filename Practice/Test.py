class Koffer:

    # In diesem Bereich werden Klassenvariablen deklariert und initiiert. 
    # Diese ist dann für alle Objekte dieselbe.
    bratwurst = "Vegane Bratwurst"

    # Der Konstruktor in Python wird mit 
    # def __init__(self) für (init -> initialize) eingeleitet 
    def __init__(self, anzahl_slots):
        # 'self' referenziert auf das aufrufende Objekt selbst
        # Es muss bei jeder Methode angegeben werden, damit es
        # innerhalb der Methode verfügbar ist
        
        # self.container deklariert die Objektvariable container
        # initiiert wird diese Variable mit einer Liste der Länge 0
        self.container = []

        # Hier wird die maximale Anzahl an Slots festgelegt.
        # Änalog zum Inventory in manchen Spielen
        self.anzahl_slots = anzahl_slots
        

    # Jetzt kann die Klasse um Methoden erweitert werden

    # Da der Container nicht mehr als 'anzahl_slots' elemente aufnehmen
    # darf, muss das Befüllen über eine Methode erfolgen.
    def lege_item_in_koffer(self, item : object) -> bool:
        if (len(self.container) > self.anzahl_slots) or item is None or item == '':
            return False
        self.container.append(item)
        return True
        
    # Auch für das Entnehmen muss eine Methode definiert werden.
    def entnehme_item_aus_koffer(self, slot_nummer : int) -> object | None:
        if len(self.container) == 0 or slot_nummer < 0 or slot_nummer > len(self.container):
            return
        return self.container.pop(slot_nummer)
    def freier_platz(self) -> int:
        return self.anzahl_slots - len(self.container)
    
    # Ausgabe aller 
    def zeige_inhalt(self):
         for i in enumerate(self.container):
              print(i)
    
def run():
     # Objekt der Klasse 'Koffer' instanziieren
     # Ein Koffer mit 10 Slots
     obj_von_klasse : Koffer = Koffer(10)

     print(obj_von_klasse.freier_platz)
     obj_von_klasse.lege_item_in_koffer("Gitarre")
     obj_von_klasse.lege_item_in_koffer("Songbook")

     obj_von_klasse.zeige_inhalt()

     print(obj_von_klasse.bratwurst)



if __name__ == '__main__':
        run()
