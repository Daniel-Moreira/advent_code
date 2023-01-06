import sys

MEASUREMENT_WINDOW = 3


def compare_measurement_sums(numbers: list[int]) -> bool:
    sum_a = 0
    sum_b = 0

    for i in range(MEASUREMENT_WINDOW):
        sum_a = sum_a + numbers[i]
        sum_b = sum_b + numbers[i + 1]

    return sum_b > sum_a


def main():
    numbers = []
    measurement_count = 0
    count = 0

    file_name = sys.argv[1]

    print(sys.argv[0])
    with open(file_name, "r") as file:
        for line in file:
            numbers.append(int(line))

            if measurement_count >= MEASUREMENT_WINDOW and compare_measurement_sums(
                numbers
            ):
                count += 1

            if measurement_count >= MEASUREMENT_WINDOW:
                numbers.pop(0)

            measurement_count += 1

    print(count)
    return count


if __name__ == "__main__":
    main()
