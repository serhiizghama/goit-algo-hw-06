def print_table(distances):
    # Верхній рядок таблиці
    print("{:<15} {:<15}".format("Вершина", "Відстань"))
    print("-" * 25)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        print("{:<15} {:<15}".format(vertex, distance))


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    return distances


graph = {
    'Київ': {'Харків': 479, 'Одеса': 471, 'Львів': 544},
    'Харків': {'Київ': 479, 'Одеса': 565, 'Дніпро': 224},
    'Одеса': {'Київ': 471, 'Харків': 565, 'Дніпро': 476},
    'Львів': {'Київ': 544, 'Харків': 795, 'Дніпро': 807},
    'Дніпро': {'Київ': 486, 'Харків': 224, 'Одеса': 476, 'Львів': 807}
}


for city in graph.keys():
    print()
    print(f'Найкоротший шлях між вершиною {city} та іншими вершинами графу')
    print_table(dijkstra(graph, city))
