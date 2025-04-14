import networkx as nx
import matplotlib.pyplot as plt

# Create an empty undirected graph
G = nx.Graph()

# Add nodes (people)
people = ["Alice", "Bob", "Charlie", "Dana", "Eve", "Frank"]
G.add_nodes_from(people)

# Add edges
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Charlie"),
    ("Bob", "Dana"),
    ("Charlie", "Dana"),
    ("Dana", "Eve"),
    ("Eve", "Frank"),
    ("Charlie", "Eve"),
]
G.add_edges_from(friendships)

# Analyze basic characteristics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Degree of each node:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Visualize the graph
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
plt.title("Social Network Graph")
plt.show()
