import sys
from typing import Any


def is_list(value: Any) -> bool:
    return type(value) == list


def compare_lists(v_1: list, v_2: list) -> int:
    value = 0
    for l, r in zip(v_1, v_2):
        if is_list(l) and is_list(r):
            value = compare_lists(l, r)
        elif is_list(l) and not is_list(r):
            value = compare_lists(l, [r])
        elif not is_list(l) and is_list(r):
            value = compare_lists([l], r)
        elif not is_list(l) and not is_list(r):
            value = compare_integers(l, r)

        if value != 0:
            return value

    return compare_integers(len(v_1), len(v_2))


def compare_integers(v_1: int, v_2: int) -> bool:
    return v_2 - v_1


def read_input(input):
    cur_list = []
    i = 0
    while i < len(input):
        character = input[i]
        if character == "]":
            return cur_list, i + 1
        if character == ",":
            i += 1
            continue
        if character == "[":
            l, j = read_input(input[i + 1 : len(input)])
            i += j
            cur_list.append(l)
        else:
            number = ""
            while input[i] not in ["]", ","]:
                number += input[i]
                i += 1
            cur_list.append(int(number))
            i -= 1

        i += 1


def main():
    file_name = sys.argv[1]

    all_lists = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            l, _ = read_input(line[1 : len(line)])
            all_lists.append(l)
            # all_lists.append(eval(line))

        indexes = []
        for i in range(0, len(all_lists), 2):
            if compare_lists(all_lists[i], all_lists[i + 1]) > 0:
                indexes.append((i // 2) + 1)

        print(sum(indexes))
        return indexes


if __name__ == "__main__":
    main()
