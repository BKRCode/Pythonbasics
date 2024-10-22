import random

print("Welcome to the Guessing Game!")
print("Bitte versuch die Nummer zu erraten, zwischen 1 und 100.")


number = random.randint(1,100)
guess = -1

while guess != number:
    guess_str= input("Gib deinen Tipp ein: ")
    guess = int(guess_str)

    if guess < number:
        print("Etwas zu niedrig, versuchs nochmal!")
    elif guess > number:
        print("Etwas zu hoch, versuchs nochmal!")

print(f"Herzlichen Glückwunsch du hast die Nummer {number} erraten!")
