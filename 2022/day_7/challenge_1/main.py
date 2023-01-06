import sys

from tree.node import Node
from tree.types import NodeTypes
from tree.tree import Tree
from command.commands import MoveCommand, ListCommand

MAXIMUM_DIRECTORY_SIZE = 100000


def main():
    file_name = sys.argv[1]
    head = Node(NodeTypes.DIRECTORY, None)
    tree = Tree(head)

    move_command = MoveCommand(tree)
    list_command = ListCommand(tree)

    ls_is_active = False
    with open(file_name, "r") as file:
        for line in file:
            command = line.strip().split(" ")

            if command[0] == "$":
                ls_is_active = False

            if command[1] == "cd":
                move_command.execute(command[2])

            if ls_is_active:
                list_command.execute(command)

            if command[1] == "ls":
                ls_is_active = True

    tree.calculate_sizes()
    nodes_found = tree.find_directories_by_size(MAXIMUM_DIRECTORY_SIZE)

    total_size = 0

    for node in nodes_found:
        total_size += node.size

    print(total_size)
    return total_size


if __name__ == "__main__":
    main()
