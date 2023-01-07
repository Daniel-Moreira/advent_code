import sys

AMOUNT_KNOTS = 2


def is_adjacent(head_position: tuple[int, int], tail_position: tuple[int, int]) -> bool:
    return (
        head_position[0] + 1 >= tail_position[0]
        and head_position[0] - 1 <= tail_position[0]
        and head_position[1] + 1 >= tail_position[1]
        and head_position[1] - 1 <= tail_position[1]
    )


def move(position: tuple[int, int], direction: str) -> tuple[int, int]:
    if direction == "R":
        return (position[0] + 1, position[1])
    if direction == "L":
        return (position[0] - 1, position[1])
    if direction == "U":
        return (position[0], position[1] - 1)

    return (position[0], position[1] + 1)


def get_movement_direction(position_difference: int) -> int:
    movement = 0
    if position_difference > 0:
        movement = 1
    elif position_difference < 0:
        movement = -1

    return movement


def main():
    file_name = sys.argv[1]
    places_visited = set()

    knots_positions = [(0, 0) for _ in range(AMOUNT_KNOTS)]

    places_visited.add(knots_positions[AMOUNT_KNOTS - 1])
    with open(file_name, "r") as file:
        for line in file:
            movement, steps = line.strip().split(" ")

            for _ in range(int(steps)):
                knots_positions[0] = move(knots_positions[0], movement)

                for i in range(AMOUNT_KNOTS - 1):
                    if not is_adjacent(knots_positions[i], knots_positions[i + 1]):
                        x_movement = get_movement_direction(
                            knots_positions[i][0] - knots_positions[i + 1][0]
                        )
                        y_movement = get_movement_direction(
                            knots_positions[i][1] - knots_positions[i + 1][1]
                        )

                        knots_positions[i + 1] = (
                            knots_positions[i + 1][0] + x_movement,
                            knots_positions[i + 1][1] + y_movement,
                        )
                        if i == AMOUNT_KNOTS - 2:
                            places_visited.add(knots_positions[i + 1])
                    else:
                        break

    print(len(places_visited))
    return places_visited


if __name__ == "__main__":
    main()
