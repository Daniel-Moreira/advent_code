import sys


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

    highest_scenic_score = 0
    for i in range(len(florest)):
        for j in range(len(florest[0])):
            scenic_score = 1
            current_tree = florest[i][j]

            scenic_score *= get_steps_until_blocked(
                current_tree, florest, keep=(1, j), start=i - 1, end=-1, step=-1
            )
            scenic_score *= get_steps_until_blocked(
                current_tree, florest, keep=(1, j), start=i + 1, end=len(florest)
            )
            scenic_score *= get_steps_until_blocked(
                current_tree, florest, keep=(0, i), start=j - 1, end=-1, step=-1
            )
            scenic_score *= get_steps_until_blocked(
                current_tree, florest, keep=(0, i), start=j + 1, end=len(florest[0])
            )

            if highest_scenic_score < scenic_score:
                highest_scenic_score = scenic_score

    print(highest_scenic_score)
    return highest_scenic_score


def get_steps_until_blocked(
    current_height: int,
    florest: list[list[int]],
    keep: tuple[int, int],
    start: int,
    end: int,
    step: int = 1,
) -> int:
    steps = 0
    for i in range(start, end, step):
        steps += 1
        if (
            current_height
            <= florest[keep[1] if keep[0] == 0 else i][keep[1] if keep[0] == 1 else i]
        ):
            break

    return steps


if __name__ == "__main__":
    main()
