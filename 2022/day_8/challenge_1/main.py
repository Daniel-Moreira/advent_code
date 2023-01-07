from enum import Enum
import sys


class Direction(Enum):
    TOP = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 3


def main():
    file_name = sys.argv[1]
    florest: list[list[int]] = []

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            trees = []
            for char in line:
                trees.append(int(char))

            florest.append(trees)

    highest_trees: list[list[list[int]]]
    highest_trees = [
        [[0 for _ in range(4)] for _ in range(len(florest[0]))]
        for _ in range(len(florest))
    ]

    for i in range(len(florest)):
        for j in range(len(florest[0])):
            if i - 1 < 0:
                highest_trees[i][j][Direction.TOP.value] = -1
            else:
                highest_trees[i][j][Direction.TOP.value] = (
                    florest[i - 1][j]
                    if florest[i - 1][j] > highest_trees[i - 1][j][Direction.TOP.value]
                    else highest_trees[i - 1][j][Direction.TOP.value]
                )

            if j - 1 < 0:
                highest_trees[i][j][Direction.LEFT.value] = -1
            else:
                highest_trees[i][j][Direction.LEFT.value] = (
                    florest[i][j - 1]
                    if florest[i][j - 1] > highest_trees[i][j - 1][Direction.LEFT.value]
                    else highest_trees[i][j - 1][Direction.LEFT.value]
                )

    for i in range(len(florest) - 1, -1, -1):
        for j in range(len(florest[0]) - 1, -1, -1):
            if i + 1 > len(florest) - 1:
                highest_trees[i][j][Direction.BOTTOM.value] = -1
            else:
                highest_trees[i][j][Direction.BOTTOM.value] = (
                    florest[i + 1][j]
                    if florest[i + 1][j]
                    > highest_trees[i + 1][j][Direction.BOTTOM.value]
                    else highest_trees[i + 1][j][Direction.BOTTOM.value]
                )

            if j + 1 > len(florest[0]) - 1:
                highest_trees[i][j][Direction.RIGHT.value] = -1
            else:
                highest_trees[i][j][Direction.RIGHT.value] = (
                    florest[i][j + 1]
                    if florest[i][j + 1]
                    > highest_trees[i][j + 1][Direction.RIGHT.value]
                    else highest_trees[i][j + 1][Direction.RIGHT.value]
                )

    visible_count = 0
    for i in range(len(florest)):
        for j in range(len(florest[0])):
            current_tree = florest[i][j]

            for direction in Direction:
                if current_tree > highest_trees[i][j][direction.value]:
                    visible_count += 1
                    break

    print(visible_count)
    return visible_count


if __name__ == "__main__":
    main()
