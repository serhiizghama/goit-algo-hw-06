import networkx as nx
import matplotlib.pyplot as plt


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

print(
    f'Кількість верщин графу: {G.number_of_nodes()}, кількість ребер: {G.number_of_edges()}')
print(f'Ступінь центральності (Degree Centrality): {nx.degree_centrality(G)}')
print(f'Близькість вузла (Closeness Centrality): {nx.closeness_centrality(G)}')
print(
    f'Посередництво вузла (Betweenness Centrality): {nx.betweenness_centrality(G)}')

plt.figure(figsize=(12, 6))
labels = nx.get_edge_attributes(G, 'weight')
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_size=11,
        node_size=2000, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
