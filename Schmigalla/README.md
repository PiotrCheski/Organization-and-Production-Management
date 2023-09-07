## Machine Placement on a Triangular Grid

This script not only performs a task related to optimizing the order of operations or tasks based on certain package requirements and their relationships but also demonstrates a method for placing machines on a triangular grid. The triangular grid is created using NetworkX and serves as the spatial layout for various machines or nodes.

### How It Works

1. **Triangular Lattice Graph**: The script utilizes NetworkX to generate a triangular lattice graph, which represents the positions or nodes where machines can be placed. This graph structure provides a visually appealing and efficient way to organize machines.

2. **Initial Machine Placement**: The script selects an initial pair of positions on the triangular grid and labels them with the first two letters from the optimized order of operations. This demonstrates the process of placing the initial machines in a strategic manner.

3. **Iterative Machine Placement**: For the remaining letters in the order of operations, the script iteratively selects positions on the grid based on their cost of placement. It calculates the cost by considering the distance to already placed machines and the associated package requirements.

4. **Total Cost Calculation**: The script computes the total cost of machine placement, reflecting the optimization process. This total cost represents the efficiency and effectiveness of the chosen machine layout.

### Visualization

The script not only optimizes the order of operations but also visualizes the placement of machines on the triangular grid. This visualization can help users understand how an optimized order of tasks can translate into an efficient spatial layout of machines.

Feel free to explore the graphical representation of the machine placement in the accompanying code and README to gain insights into how these two aspects are interconnected.
![obraz](https://github.com/PiotrCheski/Production-Management/assets/61555492/d0097967-bee5-4b67-af17-0b161388e71e)


This combined approach showcases the versatility and applicability of the script, making it a valuable tool for tasks involving both task scheduling and spatial organization.
