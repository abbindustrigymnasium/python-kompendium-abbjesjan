given_dist = ""
dist = 0
km_miles = 0.621371192  # förändringsfaktor från km till miles
miles_km = 1.609344
dist_unit_list = []
unit = []


def km_to_miles(dist):
    dist = dist * km_miles  # multiplicerar avståndet med förändringsfaktorn
    return dist


def miles_to_km(dist):
    dist = dist * miles_km
    return dist


print("Konvertera mellan km och miles/miles och km:")
given_dist = input("Ange distans och vald enhet:")

# delar upp stringen vid mellanrummet och omvandlar till lista
dist_unit_list = given_dist.split()

# första objektet i listan är avståndet som görs om till int
dist = int(dist_unit_list[0])

unit = dist_unit_list[1].lower()  # andra objektet är enheten

if unit == "km":
    dist = km_to_miles(dist)  # kör funktionen
    print(given_dist + " motsvarar " + str(dist) + " miles.")
elif unit == "miles":
    dist = miles_to_km(dist)
    print(given_dist + " motsvarar " + str(dist) + " km.")
else:
    # programmet är känsligt för om mellanrum saknas mellan avstånd och enhet
    print("Ej korrekt inmatning av sträcka och enhet, korrekt exempel: '5 km'")
