# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
from re import X
import typing



# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "Lucas",  # TODO: Your Battlesnake Username
        "color": "#C71585",  # TODO: Choose color
        "head": "all-seeing",  # TODO: Choose head
        "tail": "mlh-gene",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")

AnzahlFelder = 0

def flood_fill(x ,y, old, new, field, AnzahlFelder): 
    
    if x < 0 or x >= 11 or y < 0 or y >= 11:
        return AnzahlFelder
    if field[y][x] != old:
        return AnzahlFelder
    field[y][x] = new
    AnzahlFelder = AnzahlFelder + 1

    AnzahlFelder = flood_fill(x+1, y, old, new, field, AnzahlFelder)
    AnzahlFelder = flood_fill(x-1, y, old, new, field, AnzahlFelder)
    AnzahlFelder = flood_fill(x, y+1, old, new, field, AnzahlFelder)
    AnzahlFelder = flood_fill(x, y-1, old, new, field, AnzahlFelder)
    return AnzahlFelder

# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

    

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

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
    
    
    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"

    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        is_move_safe["up"] = False

    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']

    if my_head["x"] == 0:
        is_move_safe["left"] = False
    if my_head["y"] == 0:
        is_move_safe["down"] = False
    if my_head["x"] == 10:
        is_move_safe["right"] = False
    if my_head["y"] == 10:
        is_move_safe["up"] = False

    #print(is_move_safe)

    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    my_body = game_state['you']['body']
    
    #Next Move Variabeln
    next_move_down = [my_head["x"], my_head["y"]-1]
    next_move_up = [my_head["x"], my_head["y"]+1]
    next_move_left = [my_head["x"]-1, my_head["y"]]
    next_move_right = [my_head["x"]+1, my_head["y"]]
    #print(next_move_down)
    


    
    

    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    opponents = game_state['board']['snakes']
    for snake in opponents:      
        IntSnakeBody = snake['body']  
        for SnakeBody in IntSnakeBody:
            SnakeBody = [SnakeBody["x"], SnakeBody["y"]]   
            spielfeldup[SnakeBody[1]][SnakeBody[0]] = 1
            spielfelddown[SnakeBody[1]][SnakeBody[0]] = 1  
            spielfeldleft[SnakeBody[1]][SnakeBody[0]] = 1  
            spielfeldright[SnakeBody[1]][SnakeBody[0]] = 1        
            if next_move_down== SnakeBody:
                is_move_safe["down"] = False
            if next_move_right == SnakeBody:
                is_move_safe["right"] = False
            if next_move_left == SnakeBody:
                is_move_safe["left"] = False
            if next_move_up == SnakeBody:
                is_move_safe["up"] = False

    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

    # Choose arandom move from the safe ones
    next_move = random.choice(safe_moves)

    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    food = game_state['board']['food']
    
    CleanHead = [my_head["x"], my_head["y"]]

    
    AnzahlFelderDown = flood_fill(CleanHead[1]-1, CleanHead[0], 0, 3, spielfelddown, 0)
    print("D: ",AnzahlFelderDown)
    AnzahlFelderup = flood_fill(CleanHead[1]+1, CleanHead[0], 0, 3, spielfeldup, 0)
    print("U: ",AnzahlFelderup)
    AnzahlFelderLeft = flood_fill(CleanHead[1], CleanHead[0]-1, 0, 3, spielfeldleft, 0)
    print("L: ",AnzahlFelderLeft)
    AnzahlFelderRight = flood_fill(CleanHead[1], CleanHead[0]+1, 0, 3, spielfeldright, 0)
    print("R: ",AnzahlFelderRight)
    return{"move":"down"}



    # nächsteDistance = 100
    # nächstePosition = [0,0]
    # WegBeschreibung = [0,0]
    # for NächstesEssen in food:
    #     IntEssen = [NächstesEssen["x"], NächstesEssen["y"]]
    #     tempDistance = abs(IntEssen[0] - CleanHead[0]) + abs(IntEssen[1] - CleanHead[1])
    #     if tempDistance < nächsteDistance:
    #         nächsteDistance = tempDistance
    #         nächstePosition = IntEssen

    # #Wegbeschreibung + finden (print("WegBeschreibung: ",WegBeschreibung))
    # WegBeschreibung = [nächstePosition[0] - CleanHead[0], nächstePosition[1] - CleanHead[1]]
    
    # #print("Leben: ",game_state['you']['health'])
    # DeinLeben = game_state['you']['health']

    # if DeinLeben <= 100:
    #     if is_move_safe["left"] == True and WegBeschreibung[0] < 0:
    #         return{"move":"left"}
    #     if is_move_safe["right"] == True and WegBeschreibung[0] > 0:
    #         return{"move":"right"}
    #     if is_move_safe["up"] == True and WegBeschreibung[1] > 0:
    #         return{"move":"up"}
    #     if is_move_safe["down"] == True and WegBeschreibung[1] < 0:
    #         return{"move":"down"}
    
    # else:
    #     if is_move_safe["left"] == True and WegBeschreibung[0] > 0:
    #         return{"move":"left"}
    #     if is_move_safe["right"] == True and WegBeschreibung[0] < 0:
    #         return{"move":"right"}
    #     if is_move_safe["up"] == True and WegBeschreibung[1] < 0:
    #         return{"move":"up"}
    #     if is_move_safe["down"] == True and WegBeschreibung[1] > 0:
    #         return{"move":"down"}


    # print(f"MOVE {game_state['turn']}: {next_move}")
    # return {"move": next_move}

    


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
