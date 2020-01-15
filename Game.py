import networkx as nx
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 50)

G = nx.Graph()

# The first three of the following four bots will use different fixed strategies throughout the game.
# You can figure out their strategies by observing their behavior.
# Hint: network models, network growth models
# At t=0, all bots made random links
# Bot4 does not have a fixed strategy and might use smarter methods while playing the game
G.add_node('Bot1')
G.add_node('Bot2')
G.add_node('Bot3')
G.add_node('Bot4')

"""# t = 0"""

t0_addLinks = [

    ('Elif', 'Enes'),
    ('Elif', 'Hilmi'),
    ('Mahsun', 'Enes'),
    ('Mahsun', 'Serkan'),
    ('Hilmi', 'Enes'),
    ('Hilmi', 'Elif'),
    ('Serkan', 'Pinar'),
    ('Serkan', 'Elif'),
    ('Pinar', 'Mahsun'),
    ('Pinar', 'Elif'),
    ('Enes', 'Mahsun'),
    ('Enes', 'Hilmi'),
    ('Osman', 'Serkan'),
    ('Osman', 'Malek'),
    ('Malek', 'Enes'),
    ('Malek', 'Osman'),

    ('Bot1', 'Osman'),
    ('Bot1', 'Bot3'),
    ('Bot2', 'Malek'),
    ('Bot2', 'Bot4'),
    ('Bot3', 'Bot2'),
    ('Bot3', 'Pinar'),
    ('Bot4', 'Enes'),
    ('Bot4', 'Bot2')

]

G.add_edges_from(t0_addLinks)

nx.draw(G, with_labels=True)

# we use default parameters for all functions in this section
deg = nx.degree_centrality(G)
eig = nx.eigenvector_centrality(G)
ktz = nx.katz_centrality(G)
pgr = nx.pagerank(G)
btw = nx.betweenness_centrality(G)
cls = nx.closeness_centrality(G)
hub, aut = nx.hits(G)

t0_results = pd.DataFrame.from_dict([deg, eig, ktz, pgr, btw, cls, hub, aut]).transpose().round(2)
t0_results.columns = ['Degree', 'Eigen', 'Katz', 'PageRank', 'Betweenness', 'Closeness', 'Hub', 'Authority']
print(t0_results.sort_values(by='Betweenness', ascending=False))

"""# t = 1"""

t1_addLinks = [
    ('Enes', 'Elif'),  # Enes already had a link with Elif. Enes received -0.5
    ('Osman', 'Enes'),
    ('Serkan', 'Malek'),
    ('Mahsun', 'Elif'),
    ('Hilmi', 'Mahsun'),
    ('Elif', 'Bot2'),
    ('Pinar', 'Enes'),
    # Malek did not participate in this round, received -1
    ('Bot1', 'Bot2'),
    ('Bot2', 'Elif'),
    ('Bot3', 'Serkan'),
    ('Bot4', 'Mahsun')
]

t1_remLinks = [

    ('Enes', 'Hilmi'),
    ('Osman', 'Malek'),
    ('Serkan', 'Mahsun'),
    ('Mahsun', 'Serkan'),
    ('Hilmi', 'Enes'),
    ('Elif', 'Hilmi'),
    ('Pinar', 'Elif'),
    # Malek did not participate in this round, received -1
    ('Bot1', 'Bot3'),
    ('Bot2', 'Malek'),
    ('Bot3', 'Bot1'),
    ('Bot4', 'Enes')

]

G.add_edges_from(t1_addLinks)
G.remove_edges_from(t1_remLinks)

nx.draw(G, with_labels=True)

# we use default parameters for all functions in this section
deg = nx.degree_centrality(G)
eig = nx.eigenvector_centrality(G)
ktz = nx.katz_centrality(G)
pgr = nx.pagerank(G)
btw = nx.betweenness_centrality(G)
cls = nx.closeness_centrality(G)
hub, aut = nx.hits(G)

t1_results = pd.DataFrame.from_dict([deg, eig, ktz, pgr, btw, cls, hub, aut]).transpose().round(2)
t1_results.columns = ['Degree', 'Eigen', 'Katz', 'PageRank', 'Betweenness', 'Closeness', 'Hub', 'Authority']
print(t1_results.sort_values(by='Betweenness', ascending=False))

"""# t = 2"""

t2_addLinks = [

    ('Malek', 'Bot4'),
    ('Elif', 'Bot1'),
    ('Enes', 'Bot4'),
    ('Hilmi', 'Serkan'),
    ('Mahsun', 'Osman'),
    ('Serkan', 'Hilmi'),
    # Pinar did not participate at this round and received -1.
    # Osman did not participate at this round and received -1.
    ('Bot1', 'Malek'),
    ('Bot2', 'Enes'),
    ('Bot3', 'Mahsun'),
    ('Bot4', 'Hilmi'),

]
G.remove_edges_from('Elif', 'Mahsun')
G.add_edges_from(t2_addLinks)

nx.draw(G, with_labels=True)

# we use default parameters for all functions in this section
deg = nx.degree_centrality(G)
eig = nx.eigenvector_centrality(G)
ktz = nx.katz_centrality(G)
pgr = nx.pagerank(G)
btw = nx.betweenness_centrality(G)
cls = nx.closeness_centrality(G)
hub, aut = nx.hits(G)

t2_results = pd.DataFrame.from_dict([deg, eig, ktz, pgr, btw, cls, hub, aut]).transpose().round(2)
t2_results.columns = ['Degree', 'Eigen', 'Katz', 'PageRank', 'Betweenness', 'Closeness', 'Hub', 'Authority']
print(t2_results.sort_values(by='Betweenness', ascending=False))