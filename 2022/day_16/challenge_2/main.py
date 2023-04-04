import sys
import re 


REGEX = "Valve ([A-Z]+).+=([0-9]+).+valve[s]* (.+)"
FISRT_NODE = "AA"
MAX_MINUTES = 26

class Node():
    name: str
    pressure: int
    next: list["Node"]

def main():
    file_name = sys.argv[1]

    nodes: dict[str, Node] = {}
    valve_open: set[str] = set()
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
    
    paths = minimum_path(nodes)

    new_n = {}
    for k in nodes.keys():
        if nodes[k].pressure != 0:
            new_n[k] = nodes[k]
    
    result = get_pressures(new_n, paths)

    print(result)

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

def get_pressures(nodes: dict[str, Node], paths: dict[str, dict[str, int]]):
    pressures: dict[str, int] = {}
    minutes: dict[str, int] = {}
    all_pressures: dict[str, int]

    paths_from_node = paths[FISRT_NODE]
    # AA to all possible valves
    minutes = { key_node_to: (MAX_MINUTES - (paths_from_node[key_node_to]+1)) for key_node_to in nodes.keys() }
    pressures = { key_node_to: (MAX_MINUTES - (paths_from_node[key_node_to]+1)) * nodes[key_node_to].pressure for key_node_to in nodes.keys() }

    all_pressures = pressures
    for i in range(1, len(nodes)):
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

    pressures_sorted = dict(sorted(all_pressures.items(), key=lambda item: item[1], reverse=True))
    first_key: str = None
    optimal_pressure: int = 0
    for valve_path, pressure_release in pressures_sorted.items():
        open_valves: set[str] = set(valve_path.split("-"))

        if valve_path == first_key:
            break

        for elephant_valve_path, elephant_pressure_release in pressures_sorted.items():
            elephant_open_valves: set[str] = set(elephant_valve_path.split("-"))

            if len(open_valves.intersection(elephant_open_valves)) > 0:
                continue

            if elephant_valve_path == first_key:
                break
            if pressure_release + elephant_pressure_release > optimal_pressure:
                optimal_pressure = pressure_release + elephant_pressure_release
                if not first_key:
                    first_key = elephant_valve_path
                    break

    return optimal_pressure

if __name__ == "__main__":
    main()

