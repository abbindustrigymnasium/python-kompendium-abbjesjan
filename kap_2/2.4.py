print("Hur många år gammal är du?")
antal_år = input()
if int(antal_år) >= 18:  # programmet tar reda på om man är över 18
    print("Du är redan myndig!")
else:
    # är man under arton räknas antal år kvar ut
    antal_år_tillmyndig = 18 - int(antal_år)
    print("Du är myndig om "+str(antal_år_tillmyndig)+" år")
