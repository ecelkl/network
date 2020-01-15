import numpy as np
import netwulf as wulf
import networkx as nx


# Create a network
G = nx.random_partition_graph([10, 10, 10], .25, .01)

# Change 'block' node attribute to 'group'
for k, v in G.nodes(data=True):
    v['group'] = v['block']; del v['block']

# Or detect communities and encode them in 'group' attribute
# import community
# bb = community.best_partition(G)
# nx.set_node_attributes(G, bb, 'group')

# Set node 'size' attributes
for n, data in G.nodes(data=True):
    data['size'] = np.random.random()

# Set link 'weight' attributes
for n1, n2, data in G.edges(data=True):
    data['weight'] = np.random.random()

wulf.visualize(G)