
import networkx as nx
import pandas as pd

def create_graph(df):
    G = nx.from_pandas_edgelist(df, 'Sender', 'Receiver', edge_attr='Amount', create_using=nx.DiGraph())
    return G
