import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def bfs(capacity, flow, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        current = queue.popleft()

        for neighbor in range(len(capacity)):
            if (
                neighbor not in visited
                and capacity[current][neighbor] - flow[current][neighbor] > 0
            ):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
                if neighbor == sink:
                    return True
    return False


def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0

    while bfs(capacity, flow, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow, flow


# Створення нового графа
G_new = nx.DiGraph()

# Нові вузли
nodes_new = [
    "Термінал 1",
    "Термінал 2",
    "Склад 1",
    "Склад 2",
    "Склад 3",
    "Склад 4",
    "Магазин 1",
    "Магазин 2",
    "Магазин 3",
    "Магазин 4",
    "Магазин 5",
    "Магазин 6",
    "Магазин 7",
    "Магазин 8",
    "Магазин 9",
    "Магазин 10",
    "Магазин 11",
    "Магазин 12",
    "Магазин 13",
    "Магазин 14",
]

G_new.add_nodes_from(nodes_new)

# Нові ребра з пропускними здатностями
edges_new = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

# Додавання ребер до графа
for from_node, to_node, cap in edges_new:
    G_new.add_edge(from_node, to_node, capacity=cap)


# Індексація вузлів
def get_index(node):
    return nodes_new.index(node)


capacity = [[0] * len(nodes_new) for _ in range(len(nodes_new))]

for from_node, to_node, cap in edges_new:
    capacity[get_index(from_node)][get_index(to_node)] = cap

source = get_index("Термінал 1")
sink = get_index("Магазин 3")  # Останній магазин як приклад кінцевої точки

max_flow, flow = edmonds_karp(capacity, source, sink)

print("Максимальний потік:", max_flow)
print("Фактичний потік:")
for i in range(len(nodes_new)):
    for j in range(len(nodes_new)):
        if flow[i][j] > 0:
            print(f"{nodes_new[i]} -> {nodes_new[j]}: {flow[i][j]}")

# Отримання позицій вузлів для нового графа
pos_new = {
    "Термінал 1": (2, 3),
    "Термінал 2": (4, 3),
    "Склад 1": (1, 4),
    "Склад 2": (3, 4),
    "Склад 3": (2, 2),
    "Склад 4": (4, 2),
    "Магазин 1": (0, 5),
    "Магазин 2": (1, 5),
    "Магазин 3": (2, 5),
    "Магазин 4": (3, 5),
    "Магазин 5": (4, 5),
    "Магазин 6": (5, 5),
    "Магазин 7": (0, 1),
    "Магазин 8": (1, 1),
    "Магазин 9": (2, 1),
    "Магазин 10": (3, 1),
    "Магазин 11": (4, 1),
    "Магазин 12": (5, 1),
    "Магазин 13": (6, 1),
    "Магазин 14": (7, 1),
}

# Візуалізація нового графа
plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G_new, pos_new, node_size=700, node_color="lightblue")
nx.draw_networkx_edges(G_new, pos_new, arrowstyle="->", arrowsize=20, edge_color="gray")
nx.draw_networkx_labels(G_new, pos_new, font_size=10, font_color="black")

# Додавання міток пропускної здатності
edge_labels_new = {(u, v): d["capacity"] for u, v, d in G_new.edges(data=True)}
nx.draw_networkx_edge_labels(
    G_new, pos_new, edge_labels=edge_labels_new, font_size=8, font_color="red"
)

plt.title("Логістична мережа")
plt.axis("off")
plt.show()
