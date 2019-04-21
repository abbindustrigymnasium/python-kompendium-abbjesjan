import random

gissning = 100
antal_gissningar = 0
slumptal = 0

slumptal = random.randint(0, 99)  # randomiserar det slumpade talet
print("::The Higher Lower Game::")
print("*************************")
print("Ett tal har slumpats mellan 0 och 99, gissa vilket!")
print("-------------------------")

while gissning != slumptal:  # körs så länge användaren gissar fel tal
    # gör om till int så att det går att jämföra med slumptalet
    gissning = int(input("Gissning >> "))
    antal_gissningar += 1
    if gissning > slumptal:
        print("För hög gissning!")
    elif gissning < slumptal:
        print("För låg gissning!")


print(str(gissning) + " är rätt!")
print("Du listade ut talet på " + str(antal_gissningar) + " försök.")

if antal_gissningar < 5:  # ger olika feedback efter resultatet
    print("Fantastiskt!")
elif antal_gissningar < 10:
    print("Bra jobbat!")
elif antal_gissningar < 15:
    print("Bättre kan du!")
else:
    print("Försökte du ens?")
