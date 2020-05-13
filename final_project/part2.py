import part1

G = part1.G
nx = part1.nx
plt = part1.plt

print("\nPart 2 of the final project for CSC453")

print("Is G connected:", nx.is_connected(G))
print("The Degree Centrality of G:")
dc = nx.degree_centrality(G)
plt.figure()
plt.hist(list(dc.values()))
plt.show()

print("The Closeness Centrality of G:")
cc = nx.closeness_centrality(G)
plt.figure()
plt.hist(list(cc.values()))
plt.show()

print("The Betweenness Centrality of G:")
bc = nx.betweenness_centrality(G)
plt.figure()
plt.hist(list(bc.values()))
plt.show()

print("The Harmonic Centrality of G:")
hc = nx.harmonic_centrality(G)
plt.figure()
plt.hist(list(hc.values()))
plt.show()

print("The Eigenvector Centrality of G:")
ec = nx.eigenvector_centrality(G)
plt.figure()
plt.hist(list(ec.values()))
plt.show()

print("The Page Rank of G:")
pr = nx.pagerank(G)
plt.figure()
plt.hist(list(pr.values()))
plt.show()

print("The average clustering coefficient fo G:", nx.average_clustering(G))
cco = nx.clustering(G)
plt.figure()
plt.hist(list(cco.values()))
plt.show()
