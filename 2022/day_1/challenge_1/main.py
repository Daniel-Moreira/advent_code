sum = 0
highest_calorie = 0

with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            sum = 0
            continue

        num = int(line)

        sum += num

        if sum > highest_calorie:
            highest_calorie = sum

print(highest_calorie)
