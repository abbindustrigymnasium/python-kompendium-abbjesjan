#Grafiskt utseende för terminalprogrammet
from os import system, name  # krävs för clear()


def line(dots=False):
    #skapar linje
    if dots:
        print("********************************")
    else:  # om dots är false
        print("--------------------------------")


def header(text):
    text = text.center(28)
    print("|", text, "|")


def echo(text):
    print("| " + text)


def prompt(text):
    user_input = input("| " + text + " > ")
    return user_input


def clear():
    #resnar skärmen

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
