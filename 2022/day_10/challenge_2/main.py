import sys

COMMANDS_CYCLES = {"addx": 2, "noop": 1}

SCREEN_SIZE = (40, 6)
SPRITE = "###"


def main():
    file_name = sys.argv[1]

    x = 1
    cycle = 1

    screen = ""
    with open(file_name, "r") as file:
        for line in file:
            command = line.strip().split(" ")

            sprite_position_l = x - 1
            sprite_position_h = sprite_position_l + len(SPRITE) - 1

            time_to_execute_command = COMMANDS_CYCLES[command[0]]
            for _ in range(time_to_execute_command):
                screen_position = (cycle - 1) % 40

                if (
                    screen_position >= sprite_position_l
                    and screen_position <= sprite_position_h
                ):
                    screen += "#"
                else:
                    screen += "."

                if cycle % 40 == 0:
                    screen += "\n"

                cycle += 1

            if command[0] == "addx":
                x += int(command[1])

    print(screen)
    return screen


if __name__ == "__main__":
    main()
