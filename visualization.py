import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import seaborn as sns
import pandas as pd

risk_map = {
    'ACC-001': 12, 'ACC-002': 18, 'ACC-003': 60,
    'ACC-004': 25, 'ACC-005': 85, 'ACC-006':  8,
    'ACC-007': 30, 'ACC-008': 78, 'ACC-009': 45,
    'ACC-010': 95, 'ACC-011':  5, 'ACC-012':  2
}

def node_color(n):
    r = risk_map.get(n, 0)
    if r >= 75: return '#FF2D55'
    if r >= 40: return '#FF9F0A'
    return '#30D158'

legend_elements = [
    mpatches.Patch(color='#FF2D55', label='High Risk (≥75%)'),
    mpatches.Patch(color='#FF9F0A', label='Medium Risk (40–74%)'),
    mpatches.Patch(color='#30D158', label='Normal (<40%)'),
]

# ── Fig 1: Full Transaction Network ──────────────────────────────────────────
def plot_graph(G):
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('#0D1117')
    ax.set_facecolor('#0D1117')

    pos = nx.spring_layout(G, seed=42, k=2.2)
    node_colors = [node_color(n) for n in G.nodes()]
    node_sizes  = [800 + risk_map.get(n, 0) * 12 for n in G.nodes()]

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='#3A4A5C',
                           width=2, alpha=0.6, arrows=True, arrowsize=20,
                           connectionstyle='arc3,rad=0.1', node_size=node_sizes)

    for n in G.nodes():
        if risk_map.get(n, 0) >= 75:
            x, y = pos[n]
            circle = plt.Circle((x, y), 0.08, color='#FF2D55', alpha=0.2, zorder=1)
            ax.add_patch(circle)

    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                           node_size=node_sizes, alpha=0.95)
    nx.draw_networkx_labels(G, pos, ax=ax,
                            font_color='white', font_size=8, font_weight='bold')

    ax.legend(handles=legend_elements, loc='upper left',
              facecolor='#1C2333', edgecolor='#3A4A5C',
              labelcolor='white', fontsize=10)
    ax.set_title('Fig 1 – Banking Transaction Network',
                 color='white', fontsize=15, fontweight='bold', pad=15)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('fig1_network_graph.png', dpi=150, bbox_inches='tight',
                facecolor='#0D1117')
    plt.show()
    print("[✓] Fig 1 saved as fig1_network_graph.png")

# ── Fig 2: Centrality Bar Charts ─────────────────────────────────────────────
def plot_centrality(degree, betweenness, closeness):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.patch.set_facecolor('#0D1117')

    metrics = [
        ('Degree Centrality',      degree,      '#0A84FF'),
        ('Betweenness Centrality', betweenness, '#FF9F0A'),
        ('Closeness Centrality',   closeness,   '#30D158'),
    ]

    for ax, (title, metric, color) in zip(axes, metrics):
        ax.set_facecolor('#161B22')
        sorted_items = sorted(metric.items(), key=lambda x: -x[1])
        nodes = [i[0] for i in sorted_items]
        vals  = [i[1] for i in sorted_items]
        bar_colors = ['#FF2D55' if risk_map.get(n,0)>=75
                      else '#FF9F0A' if risk_map.get(n,0)>=40
                      else color for n in nodes]
        bars = ax.bar(nodes, vals, color=bar_colors, edgecolor='#3A4A5C', linewidth=0.8)
        ax.tick_params(colors='#8B949E', labelsize=8)
        ax.set_xticklabels(nodes, rotation=45, ha='right', color='#8B949E')
        ax.set_title(title, color='white', fontsize=12, fontweight='bold', pad=10)
        ax.set_ylabel('Score', color='#8B949E', fontsize=9)
        ax.spines[['top','right']].set_visible(False)
        ax.spines[['left','bottom']].set_color('#3A4A5C')
        ax.grid(axis='y', color='#3A4A5C', linestyle='--', alpha=0.4)
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.005,
                    f'{val:.3f}', ha='center', va='bottom',
                    color='white', fontsize=7)

    fig.suptitle('Fig 2 – Centrality Measures',
                 color='white', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('fig2_centrality.png', dpi=150, bbox_inches='tight',
                facecolor='#0D1117')
    plt.show()
    print("[✓] Fig 2 saved as fig2_centrality.png")

# ── Fig 3: Risk Score Bar + Heatmap ──────────────────────────────────────────
def plot_risk_heatmap(G, degree, betweenness, closeness):
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(16, 6))
    fig.patch.set_facecolor('#0D1117')

    accounts = list(risk_map.keys())
    risks    = list(risk_map.values())
    sorted_pairs = sorted(zip(risks, accounts), reverse=True)
    risks_s, accounts_s = zip(*sorted_pairs)

    bar_colors_risk = ['#FF2D55' if r>=75 else '#FF9F0A' if r>=40 else '#30D158'
                       for r in risks_s]
    ax_left.set_facecolor('#161B22')
    bars = ax_left.barh(accounts_s, risks_s, color=bar_colors_risk,
                        edgecolor='#3A4A5C', linewidth=0.8)
    ax_left.set_xlim(0, 110)
    ax_left.axvline(75, color='#FF2D55', linestyle='--', alpha=0.5, linewidth=1.5, label='High Risk')
    ax_left.axvline(40, color='#FF9F0A', linestyle='--', alpha=0.5, linewidth=1.5, label='Medium Risk')
    for bar, val in zip(bars, risks_s):
        ax_left.text(val+1.5, bar.get_y()+bar.get_height()/2,
                     f'{val}%', va='center', color='white', fontsize=9, fontweight='bold')
    ax_left.tick_params(colors='#8B949E')
    ax_left.set_yticklabels(accounts_s, color='#8B949E', fontsize=9)
    ax_left.set_xlabel('Risk Score (%)', color='#8B949E')
    ax_left.set_title('Fig 3a – Account Risk Scores', color='white', fontsize=13, fontweight='bold')
    ax_left.spines[['top','right']].set_visible(False)
    ax_left.spines[['left','bottom']].set_color('#3A4A5C')
    ax_left.legend(facecolor='#1C2333', edgecolor='#3A4A5C', labelcolor='#8B949E', fontsize=8)
    ax_left.grid(axis='x', color='#3A4A5C', linestyle='--', alpha=0.4)

    nodes_list = sorted(G.nodes())
    centrality_df = pd.DataFrame({
        'Degree':      [degree[n]      for n in nodes_list],
        'Betweenness': [betweenness[n] for n in nodes_list],
        'Closeness':   [closeness[n]   for n in nodes_list],
    }, index=nodes_list)

    ax_right.set_facecolor('#161B22')
    sns.heatmap(centrality_df, ax=ax_right, cmap='YlOrRd',
                annot=True, fmt='.2f', linewidths=0.5,
                linecolor='#0D1117', annot_kws={'size': 8})
    ax_right.set_title('Fig 3b – Centrality Heatmap', color='white', fontsize=13, fontweight='bold')
    ax_right.tick_params(colors='#8B949E', labelsize=8)
    ax_right.set_xticklabels(ax_right.get_xticklabels(), color='#8B949E')
    ax_right.set_yticklabels(ax_right.get_yticklabels(), color='#8B949E', rotation=0)

    plt.tight_layout()
    plt.savefig('fig3_risk_heatmap.png', dpi=150, bbox_inches='tight', facecolor='#0D1117')
    plt.show()
    print("[✓] Fig 3 saved as fig3_risk_heatmap.png")

# ── Fig 4: Amount & Frequency Analysis ───────────────────────────────────────
def plot_transactions(df):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.patch.set_facecolor('#0D1117')

    top_senders = df.groupby('Sender')['Amount'].sum().sort_values(ascending=False)
    ax_left = axes[0]
    ax_left.set_facecolor('#161B22')
    cols = ['#FF2D55' if risk_map.get(s,0)>=75
            else '#FF9F0A' if risk_map.get(s,0)>=40
            else '#30D158' for s in top_senders.index]
    ax_left.bar(top_senders.index, top_senders.values/1000,
                color=cols, edgecolor='#3A4A5C', linewidth=0.8)
    ax_left.set_title('Fig 4a – Total Amount per Account (₹K)',
                      color='white', fontsize=12, fontweight='bold')
    ax_left.set_ylabel('Amount (₹K)', color='#8B949E')
    ax_left.tick_params(colors='#8B949E', labelsize=8)
    ax_left.set_xticklabels(top_senders.index, rotation=45, ha='right', color='#8B949E')
    ax_left.spines[['top','right']].set_visible(False)
    ax_left.spines[['left','bottom']].set_color('#3A4A5C')
    ax_left.grid(axis='y', color='#3A4A5C', linestyle='--', alpha=0.4)

    ax_right = axes[1]
    ax_right.set_facecolor('#161B22')
    scatter_colors = ['#FF2D55' if risk_map.get(row.Sender,0)>=75
                      else '#FF9F0A' if risk_map.get(row.Sender,0)>=40
                      else '#30D158' for _, row in df.iterrows()]
    ax_right.scatter(df['Frequency'], df['Amount']/1000,
                     c=scatter_colors, s=80, alpha=0.8,
                     edgecolors='#0D1117', linewidths=0.5)
    for _, row in df.iterrows():
        if risk_map.get(row.Sender, 0) >= 75:
            ax_right.annotate(row.Sender,
                              (row.Frequency, row.Amount/1000),
                              textcoords='offset points', xytext=(6, 4),
                              color='#FF2D55', fontsize=7)
    ax_right.set_xlabel('Transaction Frequency', color='#8B949E')
    ax_right.set_ylabel('Amount (₹K)', color='#8B949E')
    ax_right.set_title('Fig 4b – Frequency vs Amount',
                       color='white', fontsize=12, fontweight='bold')
    ax_right.tick_params(colors='#8B949E')
    ax_right.spines[['top','right']].set_visible(False)
    ax_right.spines[['left','bottom']].set_color('#3A4A5C')
    ax_right.grid(color='#3A4A5C', linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig('fig4_transactions.png', dpi=150, bbox_inches='tight', facecolor='#0D1117')
    plt.show()
    print("[✓] Fig 4 saved as fig4_transactions.png")

# ── Fig 5: Fraud Sub-Network ──────────────────────────────────────────────────
def plot_fraud_subgraph(G, fraud_nodes):
    neighbours = set(fraud_nodes)
    for n in fraud_nodes:
        neighbours |= set(G.successors(n)) | set(G.predecessors(n))
    subG = G.subgraph(neighbours)

    fig, ax = plt.subplots(figsize=(12, 9))
    fig.patch.set_facecolor('#0D1117')
    ax.set_facecolor('#0D1117')

    pos = nx.spring_layout(subG, seed=7, k=2.5)
    sub_colors = [node_color(n) for n in subG.nodes()]
    sub_sizes  = [1000 + risk_map.get(n, 0) * 14 for n in subG.nodes()]

    for n in subG.nodes():
        if risk_map.get(n, 0) >= 75:
            x, y = pos[n]
            for radius, alpha in [(0.12, 0.12), (0.08, 0.2)]:
                circle = plt.Circle((x, y), radius, color='#FF2D55', alpha=alpha, zorder=1)
                ax.add_patch(circle)

    nx.draw_networkx_edges(subG, pos, ax=ax, edge_color='#FF6B6B',
                           width=2.5, alpha=0.5, arrows=True, arrowsize=22,
                           connectionstyle='arc3,rad=0.12', node_size=sub_sizes)
    nx.draw_networkx_nodes(subG, pos, ax=ax, node_color=sub_colors,
                           node_size=sub_sizes, alpha=0.95)
    nx.draw_networkx_labels(subG, pos, ax=ax,
                            font_color='white', font_size=9, font_weight='bold')

    ax.legend(handles=legend_elements, loc='upper left',
              facecolor='#1C2333', edgecolor='#3A4A5C',
              labelcolor='white', fontsize=10)
    ax.set_title('Fig 5 – Fraud Sub-Network (Suspicious Cluster)',
                 color='white', fontsize=15, fontweight='bold', pad=18)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('fig5_fraud_subgraph.png', dpi=150, bbox_inches='tight', facecolor='#0D1117')
    plt.show()
    print("[✓] Fig 5 saved as fig5_fraud_subgraph.png")