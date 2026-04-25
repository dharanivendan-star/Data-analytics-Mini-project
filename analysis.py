
import networkx as nx

def compute_centrality(G):
    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    return degree, betweenness, closeness
