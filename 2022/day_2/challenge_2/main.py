import sys

SHAPE_POINTS = {
    "A": 1, 
    "B": 2, 
    "C": 3,
}

WIN_SHAPES = {
    "A": "B",
    "B": "C", 
    "C": "A",
}

LOSING_SHAPES = {
    "A": "C",
    "B": "A", 
    "C": "B",
}

def main():
    total_score = 0

    file_name = sys.argv[1]

    print(sys.argv[0])
    with open(file_name, "r") as file:
        for line in file:
            opponent_shape, round_play = line.strip().split(' ')

            # Should lose
            if round_play == "X":
                total_score += 0 + SHAPE_POINTS[LOSING_SHAPES[opponent_shape]]

            # Should draw
            if round_play == "Y":
                total_score += 3 + SHAPE_POINTS[opponent_shape]

            # Should win
            if round_play == "Z":
                total_score += 6 + SHAPE_POINTS[WIN_SHAPES[opponent_shape]]

    print(total_score)
    return total_score


if __name__ == "__main__":
    main()
