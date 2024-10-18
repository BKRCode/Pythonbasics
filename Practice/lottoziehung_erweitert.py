"""
Ich möchte jetzt mit Gewinnklassen arbeiten. (Die Ziffer ist die Anzahl der Richtigen. SZ ist die Superzahl)

I -> 6SZ
II -> 6
III -> 5SZ
IV -> 5
V -> 4SZ
VI -> 4
VII -> 3SZ
VIII -> 3
IX -> 2SZ

Bonus mission: Am ende des kompletten durchlaufes soll auch ausgegeben werden, wie oft welche gewinnkombinationen gezogen wurden 
"""
def gewinnklasse(richtige):
    if richtige < 2 or richtige > 6:
        return 
    pass