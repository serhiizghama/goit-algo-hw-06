import networkx as nx
from collections import deque


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return

    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Граф деяких автошляхів Ukraine
G = nx.Graph()
G.add_nodes_from(['Київ', 'Харків', 'Одеса', 'Дніпро', 'Донецьк'])
G.add_edges_from([('Київ', 'Харків'), ('Київ', 'Одеса'), ('Київ', 'Дніпро'),
                  ('Харків', 'Одеса'), ('Харків', 'Дніпро'), ('Одеса', 'Дніпро'),
                  ('Дніпро', 'Донецьк'), ('Донецьк', 'Харків')
                  ])
G['Київ']['Харків']['weight'] = 479
G['Київ']['Одеса']['weight'] = 471
G['Київ']['Дніпро']['weight'] = 478
G['Харків']['Одеса']['weight'] = 565
G['Харків']['Дніпро']['weight'] = 224
G['Одеса']['Дніпро']['weight'] = 476
G['Дніпро']['Донецьк']['weight'] = 567
G['Донецьк']['Харків']['weight'] = 305

# Алгоритм BFS (рекурсивно)
print('Breadth-first search (BFS):')
bfs_recursive(G, deque(['Київ']))
print()
# Алгоритм DFS (рекурсивно)
print('Depth-first search (DFS):')
dfs_recursive(G, 'Київ')
