from __future__ import annotations
from tree.types import NodeTypes


class Node:
    node_type: NodeTypes
    children: map[str, Node]
    parent: Node
    size: int

    def __init__(self, node_type: NodeTypes, parent: Node, size: int = 0):
        self.node_type = node_type
        self.children = {}
        self.parent = parent
        self.size = size

    def add_child(self, child_name: str, child: Node) -> None:
        self.children[child_name] = child
