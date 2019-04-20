import requests

artister = []  # tom lista för de artister som finns i databasen
id = ""

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
r = requests.get(url)
# hämtar dictionary från länken om alla artister och id:n
artister_dictionary = r.json()

print("Dessa artister finns i databasen:")

for artist in artister_dictionary['artists']:
    # lägger till varje artistnamn i listan
    artister.append(artist['name'].lower())
    print(artist['name'])

vald_artist = input(
    "Skriv namnet på den artist som du vill veta mera om:").lower()  # användaren väljer artist

if vald_artist in artister:  # kollar så att vald artist finns i databasen
    print("Hämtar information om artisten...")
    for artist in artister_dictionary['artists']:
        # matchar med varje artist i databasen så att dess id blir rätt
        if artist['name'] == vald_artist.title():
            id = artist['id']  # sparar artist id:t

    url_id = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + \
        id  # förra länken + id
    r = requests.get(url_id)
    artist_dictionary = r.json()
    print("--------------------")
    print(artist_dictionary['artist']['name'])  # skrivar ut artistnamnet
    print("********************")

    print("Genrer: ")
    for genre in artist_dictionary['artist']['genres']:
        print(genre)  # skriver ut för varje genre

    print("\n")
    print("År då " + artist_dictionary['artist']['name'] + " varit/är aktiv:")
    for period in artist_dictionary['artist']['years_active']:
        print(period)

    print("\n")
    print("Medlemmar:")
    for medlem in artist_dictionary['artist']['members']:
        print(medlem)
else:
    print("Information saknas om " + vald_artist.title() +
          " i databasen")  # om användaren skrivit fel
