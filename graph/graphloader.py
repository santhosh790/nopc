'''
@author: Santhoshkumar S
@email: santhoshramuk@gmail.com

This file is used to load the dataset as graph.

'''


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import community

class GraphLoader:
    '''
    A Class for loading the graph
    It takes the edge list as input and generates the graph
    '''

    def __init__(self, file_path='', initial_state='I'):
        '''
        :param file_path:
        :param initial_state:

        It receives file path and initial state. File path is having edge list and
        initial_state indicates the initial state of every node.
        It is also initializes the belief of every node to some random number, between 0 to 1.
        '''

        ## Initializes the networkx graph and loads the text file that contains edge details
        G = nx.Graph()
        data_adj = np.loadtxt(file_path, delimiter=' ').astype(int)

        ## Creates tuple to for edge creation, then removes the nodes which are isolated
        data_tuple = list(map(tuple, data_adj))
        G.add_edges_from(data_tuple)
        G.remove_nodes_from(list(nx.isolates(G)))

        '''
        Initializes the state of every node to be ignorant and random belief is assigned.
        Default state is set 
        Belief value of individual node is set
        '''
        node_list = G.nodes()
        for each in node_list:
            G.node[each]['state'] = initial_state
            G.node[each]['b'] = random.randrange(0,100)/100

        '''
        Creates the community 
        '''
        #partition = community.best_partition(G)
        #nodes_in_community = {}
        #for key, value in partition.items():
        #    nodes_in_community.setdefault(value, []).append(key)

        self.G = G
        #self.comm_dict = nodes_in_community

    def get_nodes_with_belief(self, belief):
        '''
        :param belief:
        :return: a list of nodes
        Returns all the nodes of graph of particular belief value
        '''
        node_list = self.G.nodes()
        belief_node = []

        for each in node_list:
            if self.G.node[each]['b'] == belief:
                belief_node.append(each)
        return belief_node

    def show_graph(self):
        '''
        :return: an image
        It draws an image of the graph loaded.
        '''
        nx.draw(self.G, with_label = True)
        plt.show()

    def show_and_save_graph(self, path="graph.svg"):
        '''
        :param path:
        :return: an image
        It draws an image of the graph loaded and stores it in given path.
        '''
        nx.draw(self.G, with_label = True)
        plt.savefig(path)
        plt.show()


'''
dataset = GraphLoader("D:/Study/RumorDatasets/facebook_combined.txt/facebook_combined.txt")
print(dataset.G.nodes())
dataset.show_and_save_graph()
'''