"""2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!"""

import random
# randomszam = [random.randint(1,3) for _ in range(10)]
randomszamok = []
for i in range(10):
    randomszam = random.randint(1,3)
    randomszamok.append(randomszam)
    # print(randomszam)
print(randomszamok)

felhasznalo = int(input('Írj be egy sámot 1 és 3 között:'))
if felhasznalo > 3 or felhasznalo < 1:
    print('Rosszul adtad meg a számot!')
    quit( print('A Task Véget Ért!'))
while felhasznalo in randomszamok:
    randomszamok.remove(felhasznalo)
print(randomszamok)
# felhasznalo = input('Írj be egy számot 1 és 3 között:')
# print(randomszam.remove(felhasznalo))