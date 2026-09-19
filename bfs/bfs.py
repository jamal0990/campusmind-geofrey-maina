from collections import deque

# Campus graph
campus = {
    "Main Gate": ["Administration Block", "Cafeteria"],
    "Administration Block": ["Main Gate", "Library", "Science Laboratory"],
    "Library": ["Administration Block"],
    "Science Laboratory": ["Administration Block", "Student Affairs"],
    "Student Affairs": ["Science Laboratory", "Cafeteria"],
    "Cafeteria": ["Main Gate", "Student Affairs"]
}


def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        for neighbour in campus[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = path + [neighbour]
                queue.append(new_path)

    return None


# Test: Main Gate -> Science Laboratory
start = "Main Gate"
goal = "Science Laboratory"

path = bfs(start, goal)

print("BFS Path:")
print(" -> ".join(path))