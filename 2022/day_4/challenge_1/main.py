import sys


def main():
    total_fully_contained_assigments = 0

    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        for line in file:
            first_elve, second_elve = line.strip().split(",")

            first_elve_lower_bound, first_elve_higher_bound = first_elve.split("-")
            second_elve_lower_bound, second_elve_higher_bound = second_elve.split("-")

            if int(first_elve_lower_bound) <= int(second_elve_lower_bound) and int(
                first_elve_higher_bound
            ) >= int(second_elve_higher_bound):
                total_fully_contained_assigments += 1
            elif int(first_elve_lower_bound) >= int(second_elve_lower_bound) and int(
                first_elve_higher_bound
            ) <= int(second_elve_higher_bound):
                total_fully_contained_assigments += 1

    print(total_fully_contained_assigments)
    return total_fully_contained_assigments


if __name__ == "__main__":
    main()
