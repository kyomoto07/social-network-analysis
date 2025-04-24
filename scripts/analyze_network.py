import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load data
# Script нь 'scripts' хавтаст байгаа тул '../data/' гэж нэг түвшин дээшээ зааж өгнө.
data = pd.read_csv(r"C:\Users\ganbo\Desktop\Niigem git\social-network-analysis\data\got-s1-edges.csv")
graph = nx.from_pandas_edgelist(data, source='Source', target='Target')

# Visualize the graph
print("Drawing graph...") # Нэмэлт мэдээлэл хэвлэх
nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
print("Showing graph...")

# Графикийг results хавтаст хадгалах
save_path = "./results/network_visualization.png"
plt.savefig(save_path)
print(f"Graph saved to {save_path}")

print("Showing graph...")
plt.show() # Графикийг дэлгэцэнд харуулах
# ... (дараах код) ...
plt.show() # Графикийг дэлгэцэнд харуулах

print("Script finished.")