from tree.node import Node
from tree.types import NodeTypes


class Tree:
    head: Node
    current_node: Node

    def __init__(self, head: Node) -> None:
        self.head = head
        self.current_node = None

    def move_to(self, directory_name: str) -> None:
        if self.current_node == None:
            self.current_node = self.head
            return

        if directory_name == "..":
            self.current_node = self.current_node.parent
            return

        self.current_node = self.current_node.children[directory_name]

    def calculate_sizes(self) -> None:
        self._recursive_size_calculation(self.head)

    def _recursive_size_calculation(self, node: Node) -> None:
        for child in node.children.values():
            self._recursive_size_calculation(child)
            node.size += child.size

    def find_directories_by_size(self, max_size: int) -> list[Node]:
        nodes_found = []
        self._recursive_find_directories_by_size(self.head, nodes_found, max_size)

        return nodes_found

    def _recursive_find_directories_by_size(
        self, node: Node, nodes_found: list[Node], max_size: int
    ) -> None:
        if node.node_type == NodeTypes.FILE:
            return

        for child in node.children.values():
            self._recursive_find_directories_by_size(child, nodes_found, max_size)

        if node.size <= max_size:
            nodes_found.append(node)
