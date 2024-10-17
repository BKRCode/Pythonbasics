# Eingabe fuer Anwendende ermoeglichen


alter = 49

if (alter>=18):
    "Du bist voll und jährig!"


# Durch Usereingaben wird es dynamisch
# 'eingabe' muss überprüft werden, ob ein Zahlenwert enthalten ist
# erst wenn die Eingabe ein numeraler Wert ist, wird die 
# Fallunterscheidung vorgenommen

eingabe = input("Wie alt bist Du?: ")

if (int(eingabe) >= 18):
    print("Du bist voll und jährig!")
else:
    print("Du bist zu jung")

print(eingabe)
