"""Pathfinding Dijkstra Algorithm in a Social Network"""

from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt

# Create the weighted graph
G = nx.Graph()
people = ["Ali", "Bob", "Tom", "Dana", "Noah", "Ian"]
G.add_nodes_from(people)

# Add edges with weights
weighted_friendships = [
    ("Ali", "Bob", 4),
    ("Ali", "Tom", 2),
    ("Bob", "Tom", 1),
    ("Bob", "Dana", 3),
    ("Tom", "Dana", 5),
    ("Tom", "Noah", 3),
    ("Dana", "Noah", 2),
    ("Noah", "Ian", 6),
]
G.add_weighted_edges_from(weighted_friendships)


# Compute shortest paths using Dijkstra's algorithm
def dijkstra_all_pairs(graph):
    all_shortest_paths = {}
    all_shortest_lengths = {}

    for source, target in combinations(graph.nodes(), 2):
        try:
            path = nx.dijkstra_path(graph, source, target, weight="weight")
            length = nx.dijkstra_path_length(graph, source, target, weight="weight")
            all_shortest_paths[(source, target)] = path
            all_shortest_lengths[(source, target)] = length
        except nx.NetworkXNoPath:
            all_shortest_paths[(source, target)] = None
            all_shortest_lengths[(source, target)] = float("inf")

    return all_shortest_paths, all_shortest_lengths


# Compute shortest paths and lengths
shortest_paths, shortest_lengths = dijkstra_all_pairs(G)

print("Shortest paths and lengths between all pairs of nodes:")
for (source, target), path in shortest_paths.items():
    length = shortest_lengths[(source, target)]
    print(f"{source} to {target}: Path = {path}, Length = {length}")

# Visualize the graph with weights
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=500,
    font_size=12,
    edge_color="gray",
)

# Add edge labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Social Network Graph with Weights")
plt.show()
