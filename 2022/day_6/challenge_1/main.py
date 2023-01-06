import sys

SEQUENCE_STREAK = 14

def main():
    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        characters = file.readline().strip()

        for i in range(len(characters)-4):
            end_interval = i+SEQUENCE_STREAK
            if (len(set(characters[i:end_interval])) == SEQUENCE_STREAK):
                print(end_interval)
                return end_interval

if __name__ == "__main__":
    main()
