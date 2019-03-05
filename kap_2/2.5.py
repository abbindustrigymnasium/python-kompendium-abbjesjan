print("Fyll i de uppgifter som efterfrågas:")
print("Hur många elever vill ha...")
print("2 vanliga korvar?")
antal_två_vanliga = int(input())
print("3 vanliga korvar?")
antal_tre_vanliga = int(input())
print("2 veganska korvar?")
antal_två_veganska = int(input())
print("3 veganska korvar?")
antal_tre_veganska = int(input())

antal_vanligakorvar = 2 * antal_två_vanliga + 3 * antal_tre_vanliga  # räknar ut antalet korvar
antal_veganskakorvar = 2 * antal_två_veganska + 3 * antal_tre_veganska

antal_paket_vanliga = antal_vanligakorvar / 8  # räknar ut antal paket
antal_paket_veganska = antal_veganskakorvar / 8

antal_dryck = antal_tre_vanliga + antal_två_vanliga + antal_tre_veganska + antal_två_veganska  # räknar ut antal elever

pris = 20.95 * antal_paket_vanliga + 34.95 * antal_paket_veganska + 13.95 * antal_dryck  # räknar ut kostnaden

print("Det behövs:" + str(int(antal_paket_vanliga)) +
      " paket vanlig korv")  # gör om till hela paket korvar
print("Det behövs:" + str(int(antal_paket_veganska))+" paket vegansk korv")
print("Det behövs:" + str(antal_dryck) + " flaskor dryck")

print("Allt kostar totalt:" + str(int(pris)) +
      " kronor.")  # visar priset i hela kronor
