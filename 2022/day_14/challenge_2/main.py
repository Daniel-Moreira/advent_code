import sys
from enum import Enum

class THINGS(Enum):
    SAND = 0
    AIR = 1
    ROCK = 2

SAND_LOCATION = 500
MAP_SIZE = 1000

def main():
    file_name = sys.argv[1]

    map_scan: list[list[THINGS]] = []

    for i in range(MAP_SIZE):
        map_scan.append([])
        for _ in range(MAP_SIZE):
            map_scan[i].append(THINGS.AIR)

    largest_y = 0
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            
            positions: list[str] = line.split(" -> ")

            x_ant: int = 0
            y_ant: int = 0
            for position in positions:
                x, y = position.split(",")

                x = int(x)
                y = int(y)

                if y > largest_y:
                    largest_y = y

                h_min = y_ant if x == x_ant else y
                h_max = y

                if h_min > h_max:
                    aux = h_min
                    h_min = h_max
                    h_max = aux

                w_min = x_ant if y == y_ant else x
                w_max = x

                if w_min > w_max:
                    aux = w_min
                    w_min = w_max
                    w_max = aux

                for current_x in range(w_min, w_max+1):
                    map_scan[current_x][y] = THINGS.ROCK

                for current_y in range(h_min, h_max+1):
                    map_scan[x][current_y] = THINGS.ROCK
                
                x_ant = x
                y_ant = y
    
    map_scan[SAND_LOCATION][0] = THINGS.SAND
    for x in range(MAP_SIZE):
        map_scan[x][largest_y+2] = THINGS.ROCK

    blocked: bool = True
    rest_sand: int = 0
    while blocked:
        blocked = False

        x = SAND_LOCATION
        for y in range(1, MAP_SIZE):
            blocked_bellow = map_scan[x][y] in [THINGS.SAND, THINGS.ROCK]
            blocked_bellow_left = map_scan[x-1][y] in [THINGS.SAND, THINGS.ROCK]
            blocked_bellow_right = map_scan[x+1][y] in [THINGS.SAND, THINGS.ROCK]

            if any([not blocked_bellow, not blocked_bellow_left, not blocked_bellow_right]):
                x = x + (-1 * blocked_bellow * (not blocked_bellow_left)) + (1 * blocked_bellow * blocked_bellow_left * (not blocked_bellow_right))
            else: 
                if y-1 == 0:
                    break

                blocked = True
                map_scan[x][y-1] = THINGS.SAND
                rest_sand+=1
                break

    print(f"{rest_sand}\n")
    

if __name__ == "__main__":
    main()
