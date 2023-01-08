import sys


class Monkey:
    items: list[int]
    operation: callable
    test: callable
    inspect_count: int

    def __init__(self, items: list[int], operation: callable, test: callable) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspect_count = 0

    def get_item(self, item: int) -> None:
        self.items.append(item)

    def inspect_item(self) -> None:
        self.items[0] = self.operation(self.items[0])
        self.inspect_count += 1

    def bored(self) -> None:
        self.items[0] = self.items[0] // 3

    def throw_item(self) -> tuple[int, int]:
        item_to_throw = self.items.pop(0)
        return (item_to_throw, self.test(item_to_throw))


def define_operation(signal: str, second_term: str) -> callable:
    if signal == "*":
        return lambda x: x * (x if second_term == "old" else int(second_term))

    return lambda x: x + (x if second_term == "old" else int(second_term))


def define_test(amount: int, if_true: int, otherwise: int) -> callable:
    return lambda x: if_true if x % amount == 0 else otherwise


ROUNDS = 20


def main():
    file_name = sys.argv[1]

    monkeys: list[Monkey] = []
    with open(file_name, "r") as file:
        lines = file.readlines()

        for i in range(1, len(lines), 7):
            _, items = lines[i].split(": ")
            items = items.split(",")
            items = [int(item) for item in items]

            _, operation = lines[i + 1].split("old ")
            signal, second_term = operation.strip().split(" ")
            operation = define_operation(signal=signal, second_term=second_term)

            _, divisible_amount = lines[i + 2].split("by ")
            _, if_true = lines[i + 3].split("monkey ")
            _, otherwise = lines[i + 4].split("monkey ")

            test = define_test(
                amount=int(divisible_amount),
                if_true=int(if_true),
                otherwise=int(otherwise),
            )

            monkeys.append(
                Monkey(
                    items=items,
                    operation=operation,
                    test=test,
                )
            )

        for _ in range(ROUNDS):
            for monkey in monkeys:
                while len(monkey.items) > 0:
                    monkey.inspect_item()
                    monkey.bored()
                    item, monkey_i = monkey.throw_item()

                    monkeys[monkey_i].get_item(item)

    monkeys = sorted(monkeys, key=lambda x: x.inspect_count, reverse=True)

    print(monkeys[0].inspect_count * monkeys[1].inspect_count)
    return monkeys


if __name__ == "__main__":
    main()
