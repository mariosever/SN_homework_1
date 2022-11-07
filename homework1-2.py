import random


tajniBroj = random.randrange(1, 30)

print(tajniBroj)

pokusaj = int(input("Pogodi broj od 1 do 30: "))

if pokusaj == tajniBroj:
    print("Bravo ti si genije!")
else:
    print("Nije tocan broj!")