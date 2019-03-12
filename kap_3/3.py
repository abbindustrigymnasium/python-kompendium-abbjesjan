male = ["Erik", "Lars", "Karl", "Anders", "Johan"]

female = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva"]

print(male[0]) 
print(female[2])
print(female[-1]) # -1 = sist
print(male[1])

del male[1]
del male[1]
del female[0]

male.append("Jesper")

male.sort() 
female.sort()

print("Vilket namn ska tas bort?")
ta_bort_namn = input()

try:
    male.remove(ta_bort_namn) # tar bor det namn som angivits från listan män
except Exception: # finns den inte i listan så kommer ett feleddelande, men med den extra koden ignoreras dessa fel
    pass
try:
    female.remove(ta_bort_namn)
except Exception:
    pass

print("Män:", male)
print("Kvinnor:", female)
