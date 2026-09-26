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


# Count terminal states evaluated by minimax
terminal_count = 0


def hop_distance(start, destination):
    """Return the number of hops between two locations."""

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
    """
    Utility function:
    distance to Library - distance to Cafeteria
    """

    return (
        hop_distance(location, "Library")
        - hop_distance(location, "Cafeteria")
    )


def legal_moves(location):
    """Return all locations directly connected to the current location."""

    return GRAPH[location]


def minimax(location, depth, maximizing_player):
    """
    Minimax algorithm for the CampusMind game.

    MAX tries to maximize the utility.
    MIN tries to minimize the utility.
    The game lasts for 3 plies.
    """

    global terminal_count

    # Terminal state after 3 plies
    if depth == 3:
        terminal_count += 1
        return utility(location)

    # MAX player's turn
    if maximizing_player:
        best_value = float("-inf")

        for move in legal_moves(location):
            value = minimax(move, depth + 1, False)
            best_value = max(best_value, value)

        return best_value

    # MIN player's turn
    else:
        best_value = float("inf")

        for move in legal_moves(location):
            value = minimax(move, depth + 1, True)
            best_value = min(best_value, value)

        return best_value


if __name__ == "__main__":

    print("CampusMind Game")

    print("Main Gate moves:", legal_moves("Main Gate"))

    print("Utility of Main Gate:", utility("Main Gate"))
    print("Utility of Administration Block:",
          utility("Administration Block"))
    print("Utility of Cafeteria:", utility("Cafeteria"))

    print("\nHop distances from Main Gate:")
    print("Library:", hop_distance("Main Gate", "Library"))
    print("Cafeteria:", hop_distance("Main Gate", "Cafeteria"))

    print("\nMinimax results:")

    # Administration branch
    admin_value = minimax(
        "Administration Block",
        1,
        False
    )

    # Cafeteria branch
    cafeteria_value = minimax(
        "Cafeteria",
        1,
        False
    )

    # Reset counter before evaluating the complete game
    terminal_count = 0

    # Complete game from Main Gate
    full_game_value = minimax(
        "Main Gate",
        0,
        True
    )

    print("Admin branch:", admin_value)
    print("Cafeteria branch:", cafeteria_value)
    print("Full game:", full_game_value)
    print("Terminal states evaluated:", terminal_count)