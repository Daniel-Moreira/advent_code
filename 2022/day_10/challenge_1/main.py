import sys

COMMANDS_CYCLES = {"addx": 2, "noop": 1}


def main():
    file_name = sys.argv[1]

    x = 1
    cycle = 1

    get_cycle = 20
    cycle_increment = 40
    signal_strengths = []
    with open(file_name, "r") as file:
        for line in file:
            previous_x = x
            command = line.strip().split(" ")

            cycle += COMMANDS_CYCLES[command[0]]

            if command[0] == "addx":
                x += int(command[1])

            if cycle >= get_cycle:
                signal_strengths.append(
                    get_cycle * (previous_x if cycle > get_cycle else x)
                )

                get_cycle += cycle_increment

    print(sum(signal_strengths))
    return signal_strengths


if __name__ == "__main__":
    main()
