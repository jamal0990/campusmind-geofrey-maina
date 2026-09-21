# CampusMind - A* Search Algorithm

import heapq

graph = {
    "Main Gate": {
        "Administration Block": 4,
        "Library": 6
    },
    "Administration Block": {
        "Main Gate": 4,
        "Science Laboratory": 3,
        "Lecture Hall": 5
    },
    "Library": {
        "Main Gate": 6,
        "Lecture Hall": 2
    },
    "Science Laboratory": {
        "Administration Block": 3,
        "Computer Lab": 4
    },
    "Lecture Hall": {
        "Administration Block": 5,
        "Library": 2,
        "Computer Lab": 3
    },
    "Computer Lab": {
        "Science Laboratory": 4,
        "Lecture Hall": 3
    }
}

heuristic = {
    "Main Gate": 11,
    "Administration Block": 7,
    "Library": 5,
    "Science Laboratory": 4,
    "Lecture Hall": 3,
    "Computer Lab": 0
}


def a_star(graph, start, destination):
    priority_queue = [(heuristic[start], 0, start)]

    g_cost = {node: float("inf") for node in graph}
    g_cost[start] = 0

    previous = {node: None for node in graph}

    while priority_queue:
        f_cost, current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == destination:
            break

        for neighbour, weight in graph[current_node].items():
            new_cost = current_cost + weight

            if new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                previous[neighbour] = current_node

                f_cost = new_cost + heuristic[neighbour]

                heapq.heappush(
                    priority_queue,
                    (f_cost, new_cost, neighbour)
                )

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if g_cost[destination] == float("inf"):
        return None, float("inf")

    return path, g_cost[destination]


start = "Main Gate"
destination = "Computer Lab"

path, distance = a_star(graph, start, destination)

if path:
    print("A* Shortest Path:")
    print(" -> ".join(path))
    print("Total Distance:", distance)
else:
    print("No path found.")