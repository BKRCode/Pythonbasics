import random

for i in range(10):
    print(int(random.random() *49+1 )) #Output: Double/Float Zahl zwischen 0 und nicht 1

def rnd_ganzzahl(start, end):
    return int(random.random()* (end - start + 1) + start)

def rnd_boolean():
    return random.random() >= 0.5


rnd_wert = -1
while (rnd_wert != 49):
    rnd_wert = rnd_ganzzahl

print("Durch") 

for i in range (100):
    print(rnd_ganzzahl(1, 49))