md# 🏦 Fraud Detection in Banking Transactions

A graph-based fraud detection system that uses **Link Analysis** and **Network Centrality Measures**
to identify suspicious financial activities in banking transaction networks.

---

## 📌 Project Overview

This project constructs a **directed transaction graph** where:
- 🔵 **Nodes** → Bank Accounts
- ➡️ **Edges** → Financial Transactions (with Amount & Frequency)

Using **NetworkX**, the system analyzes the graph structure to detect accounts that exhibit
suspicious behavior based on their centrality scores and transaction patterns.

---

## 📁 Project Structure
fraud-detection-banking/
│
├── graph.py              # Graph construction from transaction data
├── analysis.py           # Centrality measures computation
├── fraud.py              # Fraud detection logic
├── visualization.py      # All 5 output visualizations
├── main.py               # Main execution file
├── transactions.csv      # Input dataset (18 transactions, 10 accounts)
└── README.md             # Project documentation

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core programming language |
| NetworkX | Graph construction & centrality analysis |
| Pandas | Data loading and manipulation |
| Matplotlib | Graph and chart visualizations |
| Seaborn | Heatmap visualization |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fraud-detection-banking.git
cd fraud-detection-banking
```

### 2. Install Dependencies
```bash
pip install networkx matplotlib pandas seaborn
```

### 3. Run the Project
```bash
python main.py
```

---

## 📊 Output Visualizations

| Figure | Description |
|--------|-------------|
| **Fig 1** | Transaction Network Graph — full directed graph with risk-colored nodes |
| **Fig 2** | Centrality Measures — Degree, Betweenness & Closeness bar charts |
| **Fig 3** | Risk Score bar chart & Centrality Heatmap |
| **Fig 4** | Transaction Amount & Frequency scatter analysis |
| **Fig 5** | Fraud Sub-Network — isolated suspicious account cluster |

---

## 🔍 How It Works

### Step 1 — Graph Construction (`graph.py`)
Builds a **Directed Graph (DiGraph)** from the CSV file where each row is a transaction edge.

### Step 2 — Centrality Analysis (`analysis.py`)
Computes three centrality metrics for every account:
- **Degree Centrality** → Number of direct connections
- **Betweenness Centrality** → How often a node acts as a bridge
- **Closeness Centrality** → How quickly a node can reach all others

### Step 3 — Fraud Detection (`fraud.py`)
Flags accounts whose **degree centrality exceeds the threshold (0.35)**
as suspicious. Lower threshold = more accounts flagged.

### Step 4 — Visualization (`visualization.py`)
Generates 5 publication-quality dark-themed plots saved as PNG files.

---

## 🚨 Sample Output
=============================================
Suspicious Accounts: ['ACC-003', 'ACC-005', 'ACC-007', 'ACC-008', 'ACC-009', 'ACC-010']

### Risk Classification

| Account | Risk Score | Level | Status |
|---------|-----------|-------|--------|
| ACC-010 | 95% | 🔴 High Risk | 🚨 Suspicious |
| ACC-005 | 85% | 🔴 High Risk | 🚨 Suspicious |
| ACC-008 | 78% | 🔴 High Risk | 🚨 Suspicious |
| ACC-003 | 60% | 🟠 Medium Risk | 🚨 Suspicious |
| ACC-009 | 45% | 🟠 Medium Risk | 🚨 Suspicious |
| ACC-001 | 12% | 🟢 Normal | ✅ Clear |
| ACC-002 | 18% | 🟢 Normal | ✅ Clear |
| ACC-004 | 25% | 🟢 Normal | ✅ Clear |
| ACC-006 | 8% | 🟢 Normal | ✅ Clear |
| ACC-007 | 30% | 🟢 Normal | ✅ Clear |

---

## 📈 Key Findings

- **ACC-010** is the primary fraud hub — highest scores across all 3 centrality measures
- **ACC-005** and **ACC-008** form a fraud cluster with circular transaction patterns
- High-risk accounts consistently show **high frequency + high amount** transactions
- The fraud sub-network reveals a **money laundering loop**: ACC-010 → ACC-005 → ACC-008 → ACC-010

---

## 🔧 Configuration

To tune fraud sensitivity, edit the threshold in `fraud.py`:

```python
def detect_fraud(degree, threshold=0.35):  # Lower = more accounts flagged
```

| Threshold | Accounts Flagged | Sensitivity |
|-----------|-----------------|-------------|
| 0.10 | All 10 accounts | Too sensitive |
| 0.35 | 6 accounts ✅ | Recommended |
| 0.60 | 2 accounts | Too strict |

---

## 🎓 Academic Context

- **Subject**: Data Analytics Lab
- **Topic**: Graph Analytics & Link Analysis
- **Mini Project No.**: 22
- **Algorithm**: Network Centrality-based Anomaly Detection

---

## 📚 References

- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- Barabási, A.L. (2016). *Network Science* — Cambridge University Press

---

## 📄 License

This project is created for academic purposes under the Data Analytics Lab curriculum.

---

> **Note**: All account names (ACC-001 to ACC-010) are synthetic and generated for
> educational demonstration only. No real banking data is used.
