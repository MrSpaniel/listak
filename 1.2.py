"""1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""

szinek = ['piros','piros','piros','narancs','sárga','zöld','zöld','kék','lila']
ember=input('Írj be egy színt:')

if ember in szinek:
    print(f'A/Az {ember} jelen van a listában.')
    print(f'A/Az {ember} {szinek.count(ember)}-szor van benne')
    print(szinek)
else:
    print(f'A/Az {ember} nincs benne.')
    print(szinek)