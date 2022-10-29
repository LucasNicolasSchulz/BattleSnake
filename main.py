# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>

import random
from re import X
import typing


def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "Lucas",  # TODO: Your Battlesnake Username
        "color": "#C71585",  # TODO: Choose color
        "head": "all-seeing",  # TODO: Choose head
        "tail": "mlh-gene",  # TODO: Choose tail
    }

#Game Starten

def start(game_state: typing.Dict):
    print("GAME START")

#AnzahlFelder = 0 ist eine Variabel welche für die flood_fill Funktion ist
AnzahlFelder = 0

#flood_fill Funktion berechnet die Anzahl der Felder
def flood_fill(x, y, old, new, field, AnzahlFelder):
    if x < 0 or x >= 11 or y < 0 or y >= 11:
        return AnzahlFelder
    if field[y][x] != old:
        return AnzahlFelder
    field[y][x] = new
    AnzahlFelder = AnzahlFelder +1

    AnzahlFelder = flood_fill( y,x+1, old, new, field, AnzahlFelder)
    AnzahlFelder = flood_fill( y,x-1, old, new, field, AnzahlFelder)
    AnzahlFelder = flood_fill( y+1,x, old, new, field, AnzahlFelder)
    AnzahlFelder = flood_fill( y-1,x, old, new, field, AnzahlFelder)
    return AnzahlFelder

#Die end Funktion ist dafür da um das spiel zu beenden und dir eine Nachricht zu schreiben wenn du Gestorben bist
def end(game_state: typing.Dict):
    print("GAME OVER\n")

#Die Funktion move wir jede runde aufgerufen und gibt deinen nächsten Zug zurück
def move(game_state: typing.Dict) -> typing.Dict:
    #is_move_safe setzt die möglichen bewegungen auf True
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    #Die vier verschiedenen Spielfelder werden gemacht für die vier möglichen bewegungen

    #Spielfeld für Oben
    spielfeldup = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    ]

    #Spielfeld für Unten
    spielfelddown = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    ]

    #Spielfeld für Links
    spielfeldleft = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    ]

    #Spielfeld für Rechts
    spielfeldright = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    ]

    #Next Move Variabeln
    next_move_down = [my_head["x"], my_head["y"]-1]
    next_move_up = [my_head["x"], my_head["y"]+1]
    next_move_left = [my_head["x"]-1, my_head["y"]]
    next_move_right = [my_head["x"]+1, my_head["y"]]

    #Verhindert das die Schlange in seinen eigenen Nacken geht 
    my_head = game_state["you"]["body"][0] #Coordinaten von deinem Kopf
    Intmy_head = [my_head["x"], my_head["y"]] #Coordinaten von deinem Kopf reines Int
    my_neck = game_state["you"]["body"][1] #Coordinaten von deinem Nacken
    Intmy_neck = [my_neck["x"], my_neck["y"]] #Coordinaten von deinem Nacken reines Int
    food = game_state['board']['food']#Coordinaten von dem Essen auf dem Feld
    IntFood = [food["x"], food["y"]]
    #Schlangen eintragen ins Flood Fill
    opponents = game_state['board']['snakes']
    for snake in opponents:
        IntSnakeBody = snake['body']
        for Snakebody in IntSnakeBody:
            Snakebody = [Snakebody["x"], Snakebody["y"]]
            spielfeldup[Snakebody[1]][Snakebody[0]] = 1
            spielfelddown[Snakebody[1]][Snakebody[0]] = 1  
            spielfeldleft[Snakebody[1]][Snakebody[0]] = 1  
            spielfeldright[Snakebody[1]][Snakebody[0]] = 1  

    # TODO: - Essen finden und essen mit Flood Fill
    nächsteDistance = 100
    nächstePosition = [0,0]
    WegBeschreibung = [0,0]
    for NächstesEssen in food:
        IntEssen = [NächstesEssen["x"], NächstesEssen["y"]]
        tempDistance = abs(IntEssen[0] - Intmy_head[0]) + abs(IntEssen[1] - Intmy_head[1])
        if tempDistance < nächsteDistance:
            nächsteDistance = tempDistance
            nächstePosition = IntEssen

    #Best Move Herausfinden
    AnzahlFelderDown = flood_fill(Intmy_head[1]-1, Intmy_head[0], 0, 1, spielfelddown, 0)
    AnzahlFelderup = flood_fill(Intmy_head[1]+1, Intmy_head[0], 0, 1, spielfeldup, 0)
    AnzahlFelderLeft = flood_fill(Intmy_head[1], Intmy_head[0]-1, 0, 1, spielfeldleft, 0)
    AnzahlFelderRight = flood_fill(Intmy_head[1], Intmy_head[0]+1, 0, 1, spielfeldright, 0)

    
    BestMove = "down"
    if AnzahlFelderDown < AnzahlFelderup and AnzahlFelderLeft < AnzahlFelderup and AnzahlFelderRight < AnzahlFelderup:
        BestMove = "up"
    if AnzahlFelderup < AnzahlFelderLeft and AnzahlFelderDown < AnzahlFelderLeft and AnzahlFelderRight < AnzahlFelderLeft:
        BestMove = "left"
    if AnzahlFelderLeft < AnzahlFelderRight and AnzahlFelderDown < AnzahlFelderRight and AnzahlFelderup < AnzahlFelderRight:
        BestMove = "right"

    #Wegbeschreibung + finden (print("WegBeschreibung: ",WegBeschreibung))
    WegBeschreibung = [nächstePosition[0] - Intmy_head[0], nächstePosition[1] - Intmy_head[1]]

    if next_move_left == True and WegBeschreibung[0] < 0:
        return{"move":"left"}
    if next_move_right == True and WegBeschreibung[0] > 0:
        return{"move":"right"}
    if next_move_up == True and WegBeschreibung[1] > 0:
        return{"move":"up"}
    if next_move_down == True and WegBeschreibung[1] < 0:
        return{"move":"down"}
    print(BestMove)
    return{"move":BestMove}
    