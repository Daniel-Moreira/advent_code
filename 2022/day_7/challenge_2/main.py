import sys

from tree.node import Node
from tree.types import NodeTypes
from tree.tree import Tree
from command.commands import MoveCommand, ListCommand

SPACE_AVAILABLE = 70000000
FREE_SPACE_REQUIRED = 30000000

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
    nodes_found = tree.find_directories_by_size(SPACE_AVAILABLE)

    used_space = tree.head.size
    missing_space = SPACE_AVAILABLE - used_space 
    space_needed = FREE_SPACE_REQUIRED - missing_space

    nodes_found = sorted(nodes_found, key=lambda node: node.size)
    best_directory = None
    for node in nodes_found:
        if node.size >= space_needed:
            best_directory = node
            break

    print(best_directory.size)
    return best_directory


if __name__ == "__main__":
    main()
