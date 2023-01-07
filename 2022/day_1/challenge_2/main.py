import bisect

AMOUNT_OF_LOOKUP_ELFS = 3

top_elfs = []
total_callories = 0

with open("input.txt", "r") as file:
    for i in range(AMOUNT_OF_LOOKUP_ELFS):
        top_elfs.append(0)

    for line in file:
        if line == "\n":
            # First entry or higher than lowest value
            if len(top_elfs) == 0 or total_callories > top_elfs[0]:
                # Insert the number into the list in the correct position to maintain a sorted order
                bisect.insort(top_elfs, total_callories)

            #  Remove the lowest value item from the list
            if len(top_elfs) > AMOUNT_OF_LOOKUP_ELFS:
                top_elfs.pop(0)

            total_callories = 0
            continue

        num = int(line)

        total_callories += num

print(sum(top_elfs))
