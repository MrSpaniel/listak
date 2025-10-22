szamok = []
harommal = []
ottel = []
paros = []
for i in range(100):
    if i % 3 == 0 and i % 5 ==0:
        szamok.append(i)
    elif i % 3 ==0:
        harommal.append(i)
    elif i % 5 == 0:
        ottel.append(i)
for i in range(100):
    if i % 3 == 0 and i % 2 == 0:
        paros.append(i)
print(f'3-mal oszthatóak {harommal}, 5-tel oszthatóak {ottel}, 3-mal és 5-tel oszthatóak {szamok}, 3-mal és páros szám {paros}')