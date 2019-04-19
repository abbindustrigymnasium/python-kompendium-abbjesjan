import requests

städer = ["stockholm", "göteborg", "malmö", "uppsala",
          "västerås"]  # lista med städer där tjänsten fungerar

print("Väderprognoser finns för:")

for stad in städer:  # skriver varje stad som finns i listan
    print(stad.title())

# den stad som användaren skriver in
vald_stad = input("Skriv den stad som du vill ha väderprognos för:").lower()

if vald_stad in städer:  # om staden som användaren skriver in har en prognos krös resten
    print("Hämtar väderprognoser för " + vald_stad.title() + "...")
    # url-en blir densamma förutom vilken stad som står sist
    url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + \
        vald_stad  # fungerar enbart för stockholm och uppsala(namn utan åäö)
    r = requests.get(url)
    response_dictionary = r.json()

    print("----------------------------")
    print("Senaste väderprognoserna:")
    print("****************************")

    for prognos in response_dictionary['forecasts']:  # för varje prognos
        # skrivs datum och väder ut
        print(prognos['date'] + "    " + prognos['forecast'])

    print("----------------------------")
else:
    # meddelande om staden inte finns
    print("Det finns ingen väderprognos för " + vald_stad.title() + "...")
