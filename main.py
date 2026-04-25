import pandas as pd
from graph import create_graph
from analysis import compute_centrality
from fraud import detect_fraud
from visualization import (plot_graph, plot_centrality,
                            plot_risk_heatmap, plot_transactions,
                            plot_fraud_subgraph)

# Load data
df = pd.read_csv("transactions.csv")

# Build graph
G = create_graph(df)

# Compute centrality
degree, betweenness, closeness = compute_centrality(G)

# Detect fraud
fraud_nodes = detect_fraud(degree)
print("=" * 45)
print("  Suspicious Accounts:", fraud_nodes)
print("=" * 45)

# Generate all 5 visualizations
plot_graph(G)                                      
plot_centrality(degree, betweenness, closeness)    
plot_risk_heatmap(G, degree, betweenness, closeness)  
plot_transactions(df)                              
plot_fraud_subgraph(G, fraud_nodes)                