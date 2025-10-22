"""Az adott lista (→ 'Próbáld ki!') elemei közül a program kiírja a 3-mal osztható páros számokat!
"""
paros = []
for i in range(1, 101):
    if i % 3 == 0 and i % 2 == 0:
        paros.append(i)
print(paros)