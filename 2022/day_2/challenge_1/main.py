import sys

SHAPE_POINTS = {
    "X": 1, 
    "Y": 2, 
    "Z": 3,
}

SHAPES_MAP = {
    "X": "A",
    "Y": "B", 
    "Z": "C",
}

WIN_SHAPES = {
    "A": "Y",
    "B": "Z", 
    "C": "X",
}

def main():
    total_score = 0

    file_name = sys.argv[1]

    print(sys.argv[0])
    with open(file_name, "r") as file:
        for line in file:
            opponent_shape, shape_selected = line.strip().split(' ')

            if opponent_shape == SHAPES_MAP[shape_selected]:
                total_score += 3

            if WIN_SHAPES[opponent_shape] == shape_selected:
                total_score += 6

            total_score += SHAPE_POINTS[shape_selected]

    print(total_score)
    return total_score


if __name__ == "__main__":
    main()
