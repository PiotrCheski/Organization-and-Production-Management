import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

details = {
    "detail1": {"packages": 500, "operations": "abcdcefg"},
    "detail2": {"packages": 1000, "operations": "acdeg"},
    "detail3": {"packages": 5000, "operations": "babc"},
    "detail4": {"packages": 2000, "operations": "cagdf"},
}

all_operations = [detail["operations"] for detail in details.values()]
combined_operations = ''.join(all_operations)
max_letter = max(combined_operations)

# Oblicz rozmiar macierzy sąsiedztwa na podstawie maksymalnej litery
ord_a = ord("a")
size_adj_matrix = ord(max_letter) - ord_a + 1

# Inicjuj macierz sąsiedztwa jako macierz zerową
adj_matrix = np.zeros((size_adj_matrix, size_adj_matrix))

# Wypełnij macierz sąsiedztwa na podstawie operacji i pakietów
for detail in details.values():
    packages = detail["packages"]
    operations = detail["operations"]
    for i in range(len(operations) - 1):
        source = ord(operations[i]) - ord_a
        destination = ord(operations[i + 1]) - ord_a
        adj_matrix[source, destination] += packages
        adj_matrix[destination, source] += packages

# Ustaw wartości powyżej przekątnej na 0
np.fill_diagonal(adj_matrix, 0)
# Znajdź kolejność liter na podstawie sum pakietów
kolejnosc = []
while len(kolejnosc) < adj_matrix.shape[0]:
    sums = np.sum(adj_matrix, axis=1)
    remaining_letters = [chr(ord('a') + i) for i in range(adj_matrix.shape[0]) if chr(ord('a') + i) not in kolejnosc]
    max_letter = max(remaining_letters, key=lambda letter: sums[ord(letter) - ord_a])
    kolejnosc.append(max_letter)

m = 10
n = 10
G = nx.triangular_lattice_graph(m, n)
all_neighbors = {node: set(G.neighbors(node)) for node in G.nodes()}


first_position = (2, 5)
labels = {first_position: kolejnosc[0]}

second_position = random.choice(list(all_neighbors[first_position]))
labels[second_position] = kolejnosc[1]

total_cost = adj_matrix[ord(kolejnosc[0]) - ord('a')][ord(kolejnosc[1]) - ord('a')]
chosen_nodes = {first_position, second_position}

combined_neighbors = set(all_neighbors[first_position].union(all_neighbors[second_position]))

for i in kolejnosc[2:]:
    potential_positions = list(combined_neighbors - chosen_nodes)
    min_cost = float('inf')
    next_position = None
    
    for position in potential_positions:
        cost = 0
        for label, node in labels.items():
            cost += adj_matrix[ord(i) - ord('a')][ord(node) - ord('a')] * nx.shortest_path_length(G, source=position, target=label)
        
        if cost < min_cost:
            min_cost = cost
            next_position = position
    
    labels[next_position] = i
    chosen_nodes.add(next_position)
    combined_neighbors.update(all_neighbors[next_position])
    total_cost += min_cost

print("Total Cost:", total_cost)


pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_labels(G, pos, labels=labels, font_size=16, font_color='r')
plt.show()