# lista med länderna i de två kategorierna
norden = ["Danmark", "Finland", "Island", "Norge", "Sverige"]
storbritannien = ["England", "Nordirland", "Skottland", "Wales"]
land = input(
    "Skriv ett land som tillhör antingen Norden eller Storbritannien:").title()  # gör om inputen så att landet börjar med stor bokstav


if land in norden:
    print(land + " tillhör Norden.")
elif land in storbritannien:
    print(land + " tillhör Storbritannien.")
else:
    # om landet varken finns i någon av listorna
    print(land + " tillhör varken Norden eller Storbritannien.")
