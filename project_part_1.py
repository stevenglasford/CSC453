import scipy.io as sio
from scipy.sparse import csc_matrix as csc
import networkx as nx
import matplotlib.pyplot as plt

mat_contents = sio.loadmat("Homo_sapiens.mat")
dense = mat_contents['network'].todense()
print(dense)

#G=nx.read_edgelist(dense)
G = nx.from_numpy_matrix(dense)

print(nx.info(G))
print(nx.is_directed(G))

nx.draw(G)
plt.show()
