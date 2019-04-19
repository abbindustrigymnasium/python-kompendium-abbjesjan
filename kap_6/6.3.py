import requests

artister = []
id = ""

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
r = requests.get(url)
artister_dictionary = r.json()

print("Dessa artister finns i databasen:")

for artist in artister_dictionary['artists']:
    artister.append(artist['name'].lower())
    print(artist['name'])

vald_artist = input(
    "Skriv namnet på den artist som du vill veta mera om:").lower()

if vald_artist in artister:
    print("Hämtar information om artisten...")
    for artist in artister_dictionary['artists']:
        if artist['name'] == vald_artist.title():
            id = artist['id']

    url_id = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'+id
    r = requests.get(url_id)
    artist_dictionary = r.json()
    print("--------------------")
    print(artist_dictionary['artist']['name'])
    print("********************")

    print("Genrer: ")
    for genre in artist_dictionary['artist']['genres']:
        print(genre)

    print("\n")
    print("År då " + artist_dictionary['artist']['name'] + " varit/är aktiv:")
    for period in artist_dictionary['artist']['years_active']:
        print(period)

    print("\n")
    print("Medlemmar:")
    for medlem in artist_dictionary['artist']['members']:
        print(medlem)
else:
    print("Information saknas om " + vald_artist.title() + " i databasen")
