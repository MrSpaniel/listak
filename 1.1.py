"""1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""

szinek = ['piros','piros','piros','narancs','sárga','zöld','zöld','kék','lila']
ember=input('Írj be egy színt:')

if ember in szinek:
    print(f'A/Az {ember} jelen van a listában.')
    print(szinek)
else:
    print(f'A/Az {ember} nincs benne.')
    print(szinek)