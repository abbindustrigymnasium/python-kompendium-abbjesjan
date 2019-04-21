valt_nummer = 0 
summa = 0
antal_gånger = 1

try:
    valt_nummer = int(input("Ange en multiplikationstabell>>>")) #kollar så att inputen är ett heltal
except ValueError:
    antal_gånger = 0 #sätter till 0 om inputen inte är av int-typ

if antal_gånger !=0: #kör enbart while-loopen om ett korekkt tal skrvits in
    while antal_gånger <= 3:
        summa += valt_nummer #adderar med den valda tabellen
        print(summa) #skriver summan
    

        if antal_gånger == 3:
            fortsätta = input("Vill du fortsätta? (ja/nej)").lower() #frågar efter 3 tal om användaren vill fortsätta
            if fortsätta == "ja":
                antal_gånger = 1 # "nollställer" antalet gånger om svaret är ja
                continue #hoppar över sista koden så att antal_gånger = 1 vid while-loopens början
            elif fortsätta == "nej":
                break
            else:
                print("Ej korrekt svar.")

        antal_gånger += 1
else:
    print("Ej korrekt inmatad maultiplikationstabell.") # felmeddelande