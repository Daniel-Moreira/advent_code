from enum import Enum
import sys
import re

REGEX = ".+x=([-|0-9]+).+y=([-|0-9]+):.+x=([-|0-9]+).+y=([-|0-9]+)"
SIZE = 10000000

class Things(Enum):
    empty = 0
    beacon = 1
    not_beacon = 2

def main():
    file_name = sys.argv[1]
    y_search = int(sys.argv[2])

    sensors: list[tuple[int, int]] = []
    beacons: list[tuple[int, int]] = []

    x_search: list[Things] = []
    for i in range(SIZE):
        x_search.append(Things.empty)

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

        if sensor[1]-manhattan_distance <= y_search and sensor[1]+manhattan_distance >= y_search:
            amount_not_beacon = 1 + 2 * abs(abs(y_search-sensor[1]) - manhattan_distance)

            x_start = int(sensor[0] - ((amount_not_beacon-1)/2))
            x_end = int(sensor[0] + ((amount_not_beacon-1)/2))

            for j in range(x_start+5, x_end+6):
                x_search[j] = Things.not_beacon
            
            if beacons[i][1] == y_search:
                x_search[beacons[i][0]+5] = Things.beacon

    result = 0
    for i in range(SIZE):
        if x_search[i] == Things.not_beacon:
            result += 1

    print(f"{result}") 

    

if __name__ == "__main__":
    main()
