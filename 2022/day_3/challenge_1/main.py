import sys

def main():
    total_priority = 0

    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            half = len(line) // 2
            first_compartment = set(line[:half])
            second_compartment = set(line[half:])

            common_items = first_compartment.intersection(second_compartment)

            for common_item in common_items:
                base_to_subtract = ord("A") if common_item.isupper() else ord("a")
                base_to_add = 27 if common_item.isupper() else 1
                total_priority += base_to_add + ord(common_item) - base_to_subtract

    print(total_priority)
    return total_priority


if __name__ == "__main__":
    main()
