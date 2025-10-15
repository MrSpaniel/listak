honapok = ['januar','februar', 'marcius', 'aprilis','majus','junius','julius','augusztus','szeptember','oktober','november','december']
print(type(honapok))

#lista hossza
print(len(honapok))

print(honapok[0])
print(honapok[1])
print(honapok[2])
print(honapok[3])
"""
#utolso elem a listaban
print(f'Utolsó elem a listában: {honapok[-1]}')

#a masodik szamu index
print(honapok[1:3])

#a masodik szamu indextol
print(honapok[2:])

#a otodik szamu indexig
print(honapok[:5])

#lista bejárása
for i in range(len(honapok)):
    print(honapok[i])
"""
#lista bejárása for - item
print("\nHonapok\n")
for honap in honapok:
    print(honap)