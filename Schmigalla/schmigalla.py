import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def calculate_adjacency_matrix(details):
    allOperations = [detail["operations"] for detail in details.values()]
    combinedOperations = ''.join(allOperations)
    maxLetter = max(combinedOperations)
    
    ord_a = ord("a")
    sizeAdjMatrix = ord(maxLetter) - ord_a + 1
    adjMatrix = np.zeros((sizeAdjMatrix, sizeAdjMatrix))
    
    for detail in details.values():
        packages = detail["packages"]
        operations = detail["operations"]
        for i in range(len(operations) - 1):
            source = ord(operations[i]) - ord_a
            destination = ord(operations[i + 1]) - ord_a
            adjMatrix[source, destination] += packages
            adjMatrix[destination, source] += packages
    
    np.fill_diagonal(adjMatrix, 0)
    return adjMatrix

def find_order_of_letters(adjMatrix):
    orderArr = []
    maxValueIndex = np.unravel_index(np.argmax(adjMatrix), adjMatrix.shape)
    rowIndex, colIndex = maxValueIndex
    orderArr.append(chr(ord('a') + rowIndex))
    orderArr.append(chr(ord('a') + colIndex))
    
    letterSums = {}
    progressMade = True

    while len(orderArr) < adjMatrix.shape[0] and progressMade:
        maxValue = 0
        maxLetter = None
        progressMade = False

        for i in range(adjMatrix.shape[0]):
            if chr(ord('a') + i) not in orderArr:
                letterSum = 0
                for j in range(adjMatrix.shape[0]):
                    if chr(ord('a') + j) in orderArr:
                        letterSum += adjMatrix[i, j]

                if letterSum > maxValue:
                    maxValue = letterSum
                    maxLetter = chr(ord('a') + i)

        if maxLetter:
            orderArr.append(maxLetter)
            letterSums[maxLetter] = maxValue
            progressMade = True
    
    return orderArr

def main():
    details = {
        "detail1": {"packages": 220, "operations": "cbabdgihjf"},
        "detail2": {"packages": 120, "operations": "cabagdhijh"},
        "detail3": {"packages": 100, "operations": "acfbigfc"},
        "detail4": {"packages": 400, "operations": "cacbdgjhj"},
    }

    adjMatrix = calculate_adjacency_matrix(details)
    orderArr = find_order_of_letters(adjMatrix)
    
    m = 12
    n = 12
    G = nx.triangular_lattice_graph(m, n)
    allNeighbors = {node: set(G.neighbors(node)) for node in G.nodes()}
    firstPosition = (3, 5)
    labels = {firstPosition: orderArr[0]}

    secondPosition = random.choice(list(allNeighbors[firstPosition]))
    labels[secondPosition] = orderArr[1]

    totalCost = adjMatrix[ord(orderArr[0]) - ord('a')][ord(orderArr[1]) - ord('a')]
    chosenNodes = {firstPosition, secondPosition}

    combinedNeighbors = set(allNeighbors[firstPosition].union(allNeighbors[secondPosition]))

    for i in orderArr[2:]:
        potentialPositions = list(combinedNeighbors - chosenNodes)
        minCost = float('inf')
        nextPosition = None
        
        #print(i)
        for position in potentialPositions:
            cost = 0
            for label, node in labels.items():
                cost += adjMatrix[ord(i) - ord('a')][ord(node) - ord('a')] * nx.shortest_path_length(G, source=position, target=label)
            #print(position, cost)
            if cost < minCost:
                minCost = cost
                nextPosition = position
        #print("The best position:")
        #print(nextPosition, minCost)
        labels[nextPosition] = i
        chosenNodes.add(nextPosition)
        combinedNeighbors.update(allNeighbors[nextPosition])
        totalCost += minCost

    print("Total Cost:", totalCost)
    pos = nx.get_node_attributes(G, 'pos')
    subgraph = G.subgraph(chosenNodes)
    nx.draw(subgraph, pos=pos, with_labels=True)
    nx.draw_networkx_labels(subgraph, pos, labels=labels, font_size=16, font_color='r')
    plt.show()
    
if __name__ == "__main__":
    main()
