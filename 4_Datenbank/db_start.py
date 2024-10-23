import sqlite3


connection = sqlite3.connect('erste_db.db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS \
             person(id int, name text, age int)")

# Datein einfügen INSERT INTO person VALUES (1, 'David', 37)

cursor.execute("INSERT INTO person VALUES (4, 'Legolas', 48)")

connection.commit()

cursor.execute("SELECT * FROM person")
datensaetze = cursor.fetchall()

for datensatz in datensaetze:
    print(datensatz)

connection.close()
# DQL, DML, TCL

# DQL > Data Query Language
# DML > Data Manipulation Language
# TCL > Transaction Control Language

# Transaktion
# Konto1 = 10€; Konto2 = 10€ -> 5€ Überweisen
# Konto1 = 5€ abziehen; Konto2: 5€ hinzufügen


# DDL >  Data Definition Language (CREATE, ALTER, DROP)
# DCL > (Nicht in SQLite) Data Control Language (GRANT, REVOKE)
