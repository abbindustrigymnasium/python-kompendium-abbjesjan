import web as w
import ui


artister = []  # tom lista för de artister som finns i databasen
id = ""
vald_funktion = ""
artister_dictionary = {}
on = True  # gör så att while-loopen körs oändligt tills användaren trycker x


def top_header():  # funktion för att skriva ut huvudrubriken som finns på varje startskärm
    ui.line()
    ui.header("ARTIST DATABASE")
    ui.line()


def menu():  # menyval som finns på alla skärmar
    ui.line()
    ui.echo("L | View list of artists")
    ui.echo("P | View artists profile")
    ui.echo("X | Exit program")
    ui.line(True)

    vald_funktion = ui.prompt("Select here").lower()
    # returnerar stringen som användaren matat in för att användas i while-loopen
    return vald_funktion


def get_artists():  # hämtar och returnerar dictionary med namn och id på alla artister
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

    artister_dictionary = w.get(url)
    return artister_dictionary


while on:  # körs så länge on = True

    if vald_funktion == "x":

        ui.clear()  # rensar skärmen

        break  # stänger programmet genom att "passera while-loopen"

    elif vald_funktion == "l":

        ui.clear()

        top_header()  # skriver ut headern och linjer före och efter
        ui.echo("List of all artists in the database:")
        ui.line()

        artister_dictionary = get_artists()  # hämtar dictionaryn

        for artist in artister_dictionary['artists']:

            # skriver ut alla artistnamn som finns i den hämtade dictionaryn
            ui.echo(artist['name'])

        vald_funktion = menu()  # skriver ut menyn och hämtar input

    elif vald_funktion == "p":

        ui.clear()

        top_header()

        # hämtar vilken artist som användaren vill veta om
        vald_artist = ui.prompt(
            "Write artist/group name here(or X to exit to start):")

        # hämtar alla artister varje gång som användaren navigerar till sidan
        artister_dictionary = get_artists()

        for artist in artister_dictionary['artists']:
            # lägger till varje artistnamn i listan
            artister.append(artist['name'].lower())

        if vald_artist in artister:  # kollar så att vald artist finns i databasen

            for artist in artister_dictionary['artists']:
                # matchar med varje artist i databasen så att dess id blir rätt
                if artist['name'] == vald_artist.title():

                    id = artist['id']  # sparar artist id:t

            url_id = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + \
                id  # förra länken + id
            artist_dictionary = w.get(url_id)

            ui.line()
            ui.header(artist_dictionary['artist']['name'])
            ui.line()

            ui.echo("Genres:")
            for genre in artist_dictionary['artist']['genres']:
                ui.echo(genre)

            ui.echo("\nYears active:")
            for period in artist_dictionary['artist']['years_active']:
                ui.echo(period)

            ui.echo("\nMembers:")
            for member in artist_dictionary['artist']['members']:
                ui.echo(member)

            vald_funktion = menu()

            artister = []  # tömmer listan med artister så att den återställs tills nästa gång någon vill läsa om en artist

        elif vald_artist == "x":
            # om användaren trycker x innan menyn visats kommer den till startsidan(vald_funktion matchar inte med någon annan)
            vald_funktion = ""

        else:

            print("Information saknas om " + vald_artist.title() +
                  " i databasen")  # om användaren skrivit fel
            # startar om profilsidan direkt ifall användaren skrivit fel utan att komma till start då vald_funktion redan är "p"

    else:  # eftersom vald_funktion är tom kommer programmet att starta här
        ui.clear()
        top_header()
        ui.echo("Find infomation about your favourite artists!")
        ui.line()

        vald_funktion = menu()
