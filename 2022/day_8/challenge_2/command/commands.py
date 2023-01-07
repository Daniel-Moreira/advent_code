from tree.tree import Tree
from tree.node import Node
from tree.types import NodeTypes


class Command:
    directory_tree: Tree

    def __init__(self, directory_tree: Tree) -> None:
        self.directory_tree = directory_tree

    def execute(self, *args) -> None:
        raise NotImplementedError


class MoveCommand(Command):
    def execute(self, *args) -> None:
        path = args[0]
        self.directory_tree.move_to(path)


class ListCommand(Command):
    def execute(self, *args) -> None:
        command = args[0]
        if command[0] == "dir":
            node = Node(NodeTypes.DIRECTORY, self.directory_tree.current_node)
        else:
            node = Node(
                NodeTypes.FILE, self.directory_tree.current_node, size=int(command[0])
            )

        self.directory_tree.current_node.add_child(command[1], node)
