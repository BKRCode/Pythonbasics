import random

haeufigkeit = {}

for i in range(5,31):
    haeufigkeit[i] = 0

count_rolls = 1000

for _ in range(count_rolls):
    sum = 0
    for _ in range(5):
        dice = random.randint(1, 6)
        sum += dice
    
    haeufigkeit[sum] += 1

for sum, haeufigkeiten in haeufigkeit.items():
    print(f"{sum:02} ->" + "x" * haeufigkeiten)