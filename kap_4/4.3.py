registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar = ["Anna", "Erik", "Karl"]

for avanmälning in avanmälningar: 
    registrerade.remove(avanmälning) #för varje avanmälning tas namnet i avanmälningen bort från registerade

print(registrerade)
