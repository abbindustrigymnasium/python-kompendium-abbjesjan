Daniel_Radcliffe = ["man", "brun", "brun"]  # personer och deras egenskaper
Rupert_Grint = ["man", "röd", "blå"]
Emma_Watson = ["kvinna", "brun", "brun"]
Selena_Gomez = ["kvinna", "brun", "brun"]
Donald_Trump = ["man", "gul", "blå"]
Kungen = ["man", "grå", "blå"]
Annie_Lööf = ["kvinna", "röd", "blå"]
Zara_Larsson = ["kvinna", "blond", "brun"]
Jesper_Jansson = ["man", "brun", "blå"]

matchlista = []  # lista med personer som matchar

matchar = False

kön = input("Ange kön:")
hårfärg = input("Ange hårfärg:")
ögonfärg = input("Ange ögonfärg:")

if kön == Daniel_Radcliffe[0] and hårfärg == Daniel_Radcliffe[1] and ögonfärg == Daniel_Radcliffe[2]:
    # lägger till namnet i listan om egenskaperna matchar
    matchlista.append("Daniel Radcliffe")
    matchar = True  # ändras till true då den matchar

if kön == Rupert_Grint[0] and hårfärg == Rupert_Grint[1] and ögonfärg == Rupert_Grint[2]:
    matchlista.append("Rupert Grint")
    matchar = True

if kön == Emma_Watson[0] and hårfärg == Emma_Watson[1] and ögonfärg == Emma_Watson[2]:
    matchlista.append("Emma Watson")
    matchar = True

if kön == Selena_Gomez[0] and hårfärg == Selena_Gomez[1] and ögonfärg == Selena_Gomez[2]:
    matchlista.append("Selena Gomez")
    matchar = True

if kön == Donald_Trump[0] and hårfärg == Donald_Trump[1] and ögonfärg == Donald_Trump[2]:
    matchlista.append("Donald Trump")
    matchar = True

if kön == Kungen[0] and hårfärg == Kungen[1] and ögonfärg == Kungen[2]:
    matchlista.append("Kungen")
    matchar = True

if kön == Annie_Lööf[0] and hårfärg == Annie_Lööf[1] and ögonfärg == Annie_Lööf[2]:
    matchlista.append("Annie Lööf")
    matchar = True

if kön == Zara_Larsson[0] and hårfärg == Zara_Larsson[1] and ögonfärg == Zara_Larsson[2]:
    matchlista.append("Zara Larsson")
    matchar = True

if kön == Jesper_Jansson[0] and hårfärg == Jesper_Jansson[1] and ögonfärg == Jesper_Jansson[2]:
    matchlista.append("Jesper Jansson")
    matchar = True

antal_matchningar = len(matchlista) # antalet_matchningar

if matchar == True:
    print("Du matchar med:")
    for antal in range(0, antal_matchningar): #för varje matchning med början på [0] i listan med matchningar
        # skriver ut varje matchning om egenskaperna matchar med någon
        
        print(matchlista[antal])
    
else:
    print("Dina egenskaper matchar inte med någon person i programmet")
