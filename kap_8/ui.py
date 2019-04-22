# modulen för 8.3
from os import system, name  # krävs för clear()


def line(dots=False):
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

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
