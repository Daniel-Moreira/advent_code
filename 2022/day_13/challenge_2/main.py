from functools import cmp_to_key
import sys
import bisect
from typing import Any


DIVIDER_PACKETS = [[2], [6]]


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
    return v_1 - v_2


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

        for packet in DIVIDER_PACKETS:
            all_lists.append(packet)

        all_lists.sort(key=cmp_to_key(compare_lists))
        decoder_key = 1
        for packet in DIVIDER_PACKETS:
            packet_idx = (
                bisect.bisect_left(
                    all_lists,
                    cmp_to_key(compare_lists)(packet),
                    key=cmp_to_key(compare_lists),
                )
                + 1
            )
            decoder_key *= packet_idx

        print(decoder_key)
        return decoder_key


if __name__ == "__main__":
    main()
