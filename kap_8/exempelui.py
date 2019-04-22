# skriver ut exemplet med funktionerna från ui-modulen
import ui

ui.line()
ui.header("EXEMPEL")
ui.line(True)
ui.echo("Detta är ett exempel på hur")
ui.echo("ett gränssnitt kan se ut.")
ui.line()
ui.header("..vad vill du göra?")
ui.line()
ui.echo("A | Visa inköpslista")
ui.echo("B | Lägg till vara")
ui.echo("C | Ta bort vara")
ui.echo("X | Stäng programmet")
ui.line()
ui.prompt("Val")
