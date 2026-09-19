# CampusMind - Depth First Search (DFS)

graph = {
    "Main Gate": ["Administration Block", "Library"],
    "Administration Block": ["Science Laboratory", "Lecture Hall"],
    "Library": ["Lecture Hall"],
    "Science Laboratory": ["Computer Lab"],
    "Lecture Hall": ["Computer Lab"],
    "Computer Lab": []
}


def dfs(graph, start, destination):
    visited = set()
    path = []

    def search(node):
        if node in visited:
            return False

        visited.add(node)
        path.append(node)

        if node == destination:
            return True

        for neighbour in graph[node]:
            if search(neighbour):
                return True

        path.pop()
        return False

    if search(start):
        return path

    return None


start = "Main Gate"
destination = "Computer Lab"

result = dfs(graph, start, destination)

if result:
    print("DFS Path:")
    print(" -> ".join(result))
else:
    print("No path found.")