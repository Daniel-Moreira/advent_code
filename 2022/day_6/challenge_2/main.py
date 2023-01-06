import sys

# Remove the n top crates from a stack and return the new stack formation and the crates to be moved
def remove_crates(crates: str, n: int) -> tuple[str, str]:
    return crates[: len(crates) - n], crates[len(crates) - n :]


def main():
    stacks = []

    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        while True:
            crates = file.readline().replace(" ", "").strip()
            if crates == "":
                break
            stacks.append(crates)

        for command in file.readlines():
            _, amount_crates, _, origin_stack, _, destination_stack = command.split(" ")

            new_crates, to_be_moved_crates = remove_crates(
                stacks[int(origin_stack) - 1], int(amount_crates)
            )
            stacks[int(origin_stack) - 1] = new_crates
            stacks[int(destination_stack) - 1] += to_be_moved_crates

        result = ""
        for stack in stacks:
            result += stack[-1]

        print(result)
        return result


if __name__ == "__main__":
    main()
