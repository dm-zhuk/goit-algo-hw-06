"""Create a social network graph with networkX library"""

import networkx as nx
import matplotlib.pyplot as plt

# Undirected empty graph
G = nx.Graph()

# Add nodes
people = ["Ali", "Bob", "Tom", "Dana", "Noah", "Ian"]
G.add_nodes_from(people)

# Add edges
friendships = [
    ("Ali", "Bob"),
    ("Ali", "Tom"),
    ("Bob", "Tom"),
    ("Bob", "Dana"),
    ("Tom", "Dana"),
    ("Dana", "Noah"),
    ("Noah", "Ian"),
    ("Tom", "Noah"),
]
G.add_edges_from(friendships)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Degree of each node:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Graph visualization
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    font_size=12,
    node_color="lightblue",
    edge_color="gray",
)
plt.title("Social Network Graph")
plt.show()
