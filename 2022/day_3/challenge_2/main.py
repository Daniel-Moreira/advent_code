import sys

GROUP_SIZE = 3


def main():
    badge_group = set()
    elfs_group = 0
    total_priority = 0

    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if elfs_group == 0:
                badge_group = set(line)
            else:
                badge_group = badge_group.intersection(set(line))

            if elfs_group == GROUP_SIZE - 1:
                for common_item in badge_group:
                    base_to_subtract = ord("A") if common_item.isupper() else ord("a")
                    base_to_add = 27 if common_item.isupper() else 1
                    total_priority += base_to_add + ord(common_item) - base_to_subtract

            elfs_group = (elfs_group + 1) % GROUP_SIZE

    print(total_priority)
    return total_priority


if __name__ == "__main__":
    main()
