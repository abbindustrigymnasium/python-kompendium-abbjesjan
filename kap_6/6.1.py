import requests

input_tal = input("Skriv ett positivt heltal:")

try:
    int(input_tal)  # testar om stringen är ett heltal(kan bli göras till en integer)
except ValueError:
    print("Du matade inte in ett korrekt tal.")  # om inte skrivs meddelandet

# url-en blir densamma förutom vilket tal som står sist
url = 'http://77.238.56.27/examples/numinfo/?integer='+str(input_tal)
r = requests.get(url)
response_dictionary = r.json()
print(response_dictionary)
