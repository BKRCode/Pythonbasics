#Listen funktionieren wie die ArrayList in Java

liste = ['Äpfel', 'Birnen', 'Tomaten']

print (liste)

print (liste[1]) # Birnen


print('For-Each-Construct')
# for-each
for i in liste:
    print(i)


# Auch mit Zahlen

liste = [12, 38, 48, 2]
print('Liste mit Zahlenwerten')
for i in liste:
    print(i)


# Addition der ausgegebenen werte
zahlen = [12, 45, 89, 4]
summe = 0

for zahl in zahlen:
    summe += zahl
    print("Hier der Addierte Zahlenwert:", summe)