import sys
import re 


REGEX = "Valve ([A-Z]+).+=([0-9]+).+valve[s]* (.+)"
FISRT_NODE = "AA"
MAX_MINUTES = 30

class Node():
    name: str
    pressure: int
    next: list["Node"]

def main():
    file_name = sys.argv[1]

    nodes: dict[str, Node] = {}
    valve_open: dict[str, bool] = {}
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            
            regex_search = re.search(rf"{REGEX}", line)

            groups = regex_search.groups()
            node_name = groups[0]
            node_pressure = int(groups[1])
            next_nodes_names = groups[2].replace(" ", "").split(",")
            
            node = nodes.get(node_name)
            if not node:
                node = Node()
            
            node.name = node_name
            node.pressure = node_pressure
            nodes_list: list[Node] = []
            for next in next_nodes_names:
                next_node = nodes.get(next)

                if not next_node:
                    next_node = Node()
                
                nodes[next] = next_node
                nodes_list.append(next_node)
            
            node.next = nodes_list
            nodes[node_name] = node
            valve_open[node_name] = False
    
    # root: Node = nodes[FISRT_NODE]

    paths = minimum_path(nodes)

    new_n = {}
    for k in nodes.keys():
        if nodes[k].pressure != 0:
            new_n[k] = nodes[k]
    
    # result = brute_force_op(MAX_MINUTES, MAX_MINUTES, root, root, valve_open, new_n, paths)
    result = get_pressures(new_n, paths)
    
    print(result)

def get_pressures(nodes: dict[str, Node], paths: dict[str, dict[str, int]]):
    pressures: dict[str, int] = {}
    minutes: dict[str, int] = {}

    paths_from_node = paths[FISRT_NODE]
    # AA to all possible valves
    minutes = { key_node_to: (MAX_MINUTES - (paths_from_node[key_node_to]+1)) for key_node_to in nodes.keys() }
    pressures = { key_node_to: (MAX_MINUTES - (paths_from_node[key_node_to]+1)) * nodes[key_node_to].pressure for key_node_to in nodes.keys() }

    all_pressures = pressures
    for _ in range(1, len(nodes)):
        new_pressures: dict[str, int] = {}
        new_minutes: dict[str, int] = {}

        for pressure_key in pressures.keys():
            open_valves: list[str] = pressure_key.split("-")
            last_node: str = pressure_key.split("-")[-1]

            paths_from_node = paths[last_node]

            for key_node_to in nodes.keys():
                if key_node_to in open_valves:
                    continue

                distance = paths_from_node[key_node_to]
                if (minutes[pressure_key] - (distance+1)) < 0:
                    continue

                pressure_release = (minutes[pressure_key] - (distance+1)) * nodes[key_node_to].pressure

                new_pressures[f"{pressure_key}-{key_node_to}"] = pressures[pressure_key] + pressure_release
                new_minutes[f"{pressure_key}-{key_node_to}"] = minutes[pressure_key] - (distance+1)
    
        if len(new_pressures) == 0:
            break

        pressures = new_pressures
        minutes = new_minutes
        all_pressures = { **all_pressures, **new_pressures }

    optimal_pressure: int = 0
    for pressure in all_pressures.values():
        if pressure > optimal_pressure:
            optimal_pressure = pressure

    return optimal_pressure

def minimum_path(nodes: dict[str, Node]) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}

    for key in nodes.keys():
        node: Node = nodes[key]
        node_to_all: dict[str, int] = {}
        visited: set[str] = set()
        nodes_stack: list[tuple(Node, int)] = [(node, 0)]

        node_to_all[node.name] = 0
        visited.add(node.name)
        while len(nodes_stack) > 0:
            curr_node, distance = nodes_stack.pop(0)
            distance += 1
            for child_node in curr_node.next:
                if child_node.name not in visited:
                    visited.add(child_node.name)
                    node_to_all[child_node.name] = distance
                    nodes_stack.append((child_node, distance))

        result[node.name] = node_to_all

    return result

def brute_force_op(minute: int, curr_node: Node, valve_open: dict[str, bool], nodes: dict[str, Node], paths: dict[str, dict[str, int]]) -> int:
    if minute == 0:
        return 0

    paths_from_node = paths[curr_node.name]
    highest_pressure_release = 0
    for key_node_to in paths_from_node.keys():
        distance = paths_from_node[key_node_to]
        if valve_open[key_node_to] or minute - (distance+1) < 0 or nodes[key_node_to].pressure == 0 :
            continue

        pressure_release = (minute - (distance+1)) * nodes[key_node_to].pressure
        valve_open[nodes[key_node_to].name] = True
        child_pressure = brute_force_op(minute - (distance+1), nodes[key_node_to], valve_open, nodes, paths)
        
        if pressure_release + child_pressure > highest_pressure_release:
            highest_pressure_release = pressure_release + child_pressure
        
        valve_open[nodes[key_node_to].name] = False

    return highest_pressure_release

if __name__ == "__main__":
    main()
