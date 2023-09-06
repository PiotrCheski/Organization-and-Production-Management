import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

details = {
    "detail1": {"packages": 220, "operations": "cbabdgihjf"},
    "detail2": {"packages": 120, "operations": "cabagdhijh"},
    "detail3": {"packages": 100, "operations": "acfbigfc"},
    "detail4": {"packages": 400, "operations": "cacbdgjhj"},
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


print(adj_matrix)

kolejnosc = []
max_value_index = np.unravel_index(np.argmax(adj_matrix), adj_matrix.shape)
row_index, col_index = max_value_index
kolejnosc.append(chr(ord('a') + row_index))

kolejnosc.append(chr(ord('a') + col_index))
print(kolejnosc)
k
letter_sums = {}

while len(kolejnosc) < adj_matrix.shape[0]:
    max_value = 0
    max_letter = None

    for i in range(adj_matrix.shape[0]):
        if chr(ord('a') + i) not in kolejnosc:
            letter_sum = 0  # Zainicjuj letter_sum jako 0
            for j in range(adj_matrix.shape[0]):
                if chr(ord('a') + j) in kolejnosc:
                    letter_sum += adj_matrix[i, j]  # Dodaj wartość do letter_sum

            if letter_sum > max_value:
                max_value = letter_sum
                max_letter = chr(ord('a') + i)

    if max_letter:
        kolejnosc.append(max_letter)
        letter_sums[max_letter] = max_value

print(kolejnosc)