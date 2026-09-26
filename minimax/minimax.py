from collections import deque


# CampusMind graph
GRAPH = {
    "Main Gate": ["Administration Block", "Cafeteria"],
    "Administration Block": ["Main Gate", "Library", "Science Laboratory"],
    "Library": ["Administration Block"],
    "Science Laboratory": ["Administration Block", "Student Affairs"],
    "Cafeteria": ["Main Gate", "Student Affairs"],
    "Student Affairs": ["Science Laboratory", "Cafeteria"],
}


def hop_distance(start, destination):
    """Return the number of edges between two locations."""
    if start == destination:
        return 0

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, distance = queue.popleft()

        for neighbor in GRAPH[current]:
            if neighbor == destination:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return None


def utility(location):
    """Utility = distance to Library - distance to Cafeteria."""
    return (
        hop_distance(location, "Library")
        - hop_distance(location, "Cafeteria")
    )


def legal_moves(location):
    """Return locations directly connected to the current location."""
    return GRAPH[location]


if __name__ == "__main__":
    print("CampusMind Game")

    print("Main Gate moves:", legal_moves("Main Gate"))

    print("Utility of Main Gate:", utility("Main Gate"))
    print("Utility of Administration Block:", utility("Administration Block"))
    print("Utility of Cafeteria:", utility("Cafeteria"))

    print("\nHop distances from Main Gate:")
    print("Library:", hop_distance("Main Gate", "Library"))
    print("Cafeteria:", hop_distance("Main Gate", "Cafeteria"))