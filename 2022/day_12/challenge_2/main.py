import sys
    
def find_character(map: list[list[int]], character: int) -> tuple[int, int]:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == character:
                return (i, j)

def main():
    file_name = sys.argv[1]

    with open(file_name, "r") as file:
            lines = [line.strip() for line in file]
            map = [[ord(character) for character in line] for line in lines]
            
            s_position = find_character(map, ord("S"))
            map[s_position[0]][s_position[1]] = ord("a")
            x, y = find_character(map, ord("E"))
            map[x][y] = ord("z")

            visited: set[tuple[int, int]] = {(x, y)}
            queue: list[tuple[tuple[int, int], int]] = [((x, y), 0)]
            while len(queue) > 0:
                position, distance = queue.pop(0)
                character = map[position[0]][position[1]]

                if character == ord("a"):
                    print(distance)
                    break

                x, y = position
                if x+1 < len(map) and (x+1, y) not in visited and map[x+1][y] >= character-1:
                    queue.append(((x+1, y), distance+1))
                    visited.add((x+1, y))
                if x-1 >= 0 and (x-1, y) not in visited and map[x-1][y] >= character-1:
                    queue.append(((x-1, y), distance+1))
                    visited.add((x-1, y))
                if y+1 < len(map[position[0]]) and (x, y+1) not in visited and map[x][y+1] >= character-1:
                    queue.append(((x, y+1), distance+1))
                    visited.add((x, y+1))
                if y-1 >= 0 and (x, y-1) not in visited and map[x][y-1] >= character-1:
                    queue.append(((x, y-1), distance+1))
                    visited.add((x, y-1))

if __name__ == "__main__":
    main()
