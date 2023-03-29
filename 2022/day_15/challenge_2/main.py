from enum import Enum
import sys
import re

REGEX = ".+x=([-|0-9]+).+y=([-|0-9]+):.+x=([-|0-9]+).+y=([-|0-9]+)"
SIZE = 4000000
FREQUENCY = 4000000
INVALID = -1

class Things(Enum):
    empty = 0
    beacon = 1
    not_beacon = 2

def main():
    file_name = sys.argv[1]

    sensors: list[tuple[int, int]] = []
    beacons: list[tuple[int, int]] = []

    map: list[list[tuple[int, int]]] = []
    for i in range(SIZE):        
        map.append([(INVALID, INVALID)])

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            
            regex_search = re.search(rf"{REGEX}", line)

            groups = regex_search.groups()
            sensor_x = int(groups[0])
            sensor_y = int(groups[1])
            beacon_x = int(groups[2])
            beacon_y = int(groups[3])

            sensors.append((sensor_x, sensor_y))
            beacons.append((beacon_x, beacon_y))


    for i, sensor in enumerate(sensors):
        manhattan_distance = abs(sensor[0]-beacons[i][0]) + abs(sensor[1]-beacons[i][1])

        y_start = int(sensor[1] - manhattan_distance)
        y_end = int(sensor[1] + manhattan_distance)+1

        y_start = 0 if y_start < 0 else y_start
        y_end = SIZE if y_end > SIZE else y_end
        for y_search in range(y_start, y_end):
            amount_not_beacon = 1 + 2 * abs(abs(y_search-sensor[1]) - manhattan_distance)

            x_start = int(sensor[0] - ((amount_not_beacon-1)/2))
            x_end = int(sensor[0] + ((amount_not_beacon-1)/2))

            x_start = 0 if x_start < 0 else x_start
            x_end = SIZE if x_end > SIZE else x_end
            
            map[y_search].append((x_start, x_end))

    for i in range(SIZE):
        map[i].pop(0)

    for i in range(SIZE):
        map[i] = sorted(map[i])
        x_start = map[i][0][0]
        x_end = map[i][0][1]

        if x_start != 0:
            print(f"{i}")

        for not_beacon in map[i]:
            if not_beacon[0] > x_end+1: 
                print(f"{(x_end+1)*FREQUENCY+i}")
            
            x_end = not_beacon[1] if not_beacon[1] > x_end else x_end
        
        if x_end < SIZE:
            print(f"{(x_end+1)*FREQUENCY+i}")

if __name__ == "__main__":
    main()
