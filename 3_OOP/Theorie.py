from abc import abc

class Fahrzeug(abc):
    anzahl_reifen = None
    marke = None
    modell = None
    bauart = None
    tueren = None
    max_v = None
    antriebsart = None
    leistung = None

class Auto(Fahrzeug):
    anzahl_achsen = None
   
class Lkw(Fahrzeug):
    anzahl_achsen = None
    zugleistung = None

class Motorrad(Fahrzeug):
    verkleidung = None
