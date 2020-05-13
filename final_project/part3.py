import part2

G = part2.G
nx = part2.nx
plt = part2.plt

print("\nPart 3 of CSC 453 final project.")
print("Circular Layout of G:")
nx.draw_circular(G)
plt.show()

print("The Kamanda-Kawai force-directed layout of G:")
nx.draw_kamada_kawai(G)
plt.show()

print("The plannar layout of G")
nx.draw_planar(G)
plt.show()

print("Random layout of G")
nx.draw_random(G)
plt.show()

print("Spectral Layout of G")
nx.draw_spectral(G)
plt.show()

print("Spring Layout of G")
nx.draw_spring(G)
plt.show()

print("Shell Layout of G")
nx.draw_shell(G)
plt.show()

print("No layout looks well for our network since our network is extremely large.")

# Read the new file created by deepwalk
f = open("deeper", "r")
arr = []

# read the file in line by line
for line in f:
    col = []
    # save only the last 2 columns
    i = 0
    for j in line.split():
        col.append(j)
    arr.append(col)

# close the file after reading
f.close()

# # The next two lines are only for testing and not used in production
# for line in arr:
#     print(line[1], line[2])

# The following for statement saves the first column into an x variable
# used for the x variable in the graph
x = []
for line in arr:
    x.append(line[1])

# The following for statement saves the first column into an y variable
# used for the y variable in the graph
y = []
for line in arr:
    y.append(line[2])

# The following two lines make the scatter plot for the assignment
plt.scatter(x, y)
# remove the x and y axis names in the plot as they too bunched up to
# proved any real meaningful details
plt.xticks([])
plt.yticks([])
plt.show()

# plt.scatter(arr[:, 0], arr[:, 1])


