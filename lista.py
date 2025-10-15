honapok = ['januar','februar', 'marcius', 'aprilis','majus','junius','julius','augusztus','szeptember','oktober','november','december']

# honapok.append("szopoklész")
# print(honapok)

# honapok.pop()
print("Utolsó hónap törölve:","\n",
      honapok)
torolt_honap = honapok.pop()
print("Törölt hónap:",torolt_honap)
print(honapok)

torolt_honap = honapok.pop(0)
print(honapok)

print(honapok.remove("februar"))
honapok.clear()
print(honapok)
honapok.insert(0, "februar")