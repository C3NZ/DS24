import matplotlib.pyplot as plt
import networkx as nx

graph = nx.DiGraph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "A")
graph.add_edge("D", "C")

s = sorted(
    nx.pagerank(graph, personalization=None).items(), key=lambda x: x[1], reverse=True
)

print(s)

undirected_graph = nx.Graph()
undirected_graph.add_node("A")
undirected_graph.add_node("B")
undirected_graph.add_node("C")
undirected_graph.add_node("D")
undirected_graph.add_edge("A", "B")
undirected_graph.add_edge("A", "C")
undirected_graph.add_edge("B", "C")
undirected_graph.add_edge("C", "A")
undirected_graph.add_edge("D", "C")

print(nx.density(undirected_graph))
