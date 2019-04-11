name = input("Ange ditt namn:")
age = int(input("Ange din ålder:"))  # gör om till int för if-satsen
sleep = ""  # tom variabel som kommer fyllas med hur många timmar sömn som behövs

if age >= 17:  # går från högsta åldern och vidare
    sleep = "8"
elif age == 16:
    sleep = "8,5"
elif age >= 12:
    sleep = "9"
elif age == 11:
    sleep = "9,5"
elif age >= 8:
    sleep = "10"
elif age == 7:
    sleep = "10,5"
elif age >= 5:
    sleep = "11"
elif age == 4:
    sleep = "11,5"
elif age == 3:
    sleep = "12"
elif age == 2:
    sleep = "13"
elif age == 1:
    sleep = "14"
else:
    sleep = "error"  # ger variabeln sleep stringvärdet error vid fel

if sleep != "error":  # om sleep inte är = error så kan ett meddelande skrivas ut
    print("Hej " + name + "!" + " Vårdguiden rekommenderar att individer i din ålder, " +
          str(age) + " år, behöver sova minst " + sleep + " timmar per natt.")
else:
    print("Åldern måste vara minst 1")  # annars uppmaning till användaren
