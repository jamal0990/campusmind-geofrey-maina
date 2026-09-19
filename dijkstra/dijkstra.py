# CampusMind - Dijkstra's Shortest Path Algorithm

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


def dijkstra(graph, start, destination):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == destination:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                previous[neighbour] = current_node
                heapq.heappush(priority_queue, (distance, neighbour))

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if distances[destination] == float("inf"):
        return None, float("inf")

    return path, distances[destination]


start = "Main Gate"
destination = "Computer Lab"

path, distance = dijkstra(graph, start, destination)

if path:
    print("Dijkstra Shortest Path:")
    print(" -> ".join(path))
    print("Total Distance:", distance)
else:
    print("No path found.")