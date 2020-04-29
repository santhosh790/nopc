import random
import graph.graphloader as gl
import matplotlib.pyplot as plt

class SIR:
    '''
    This class defines the **propagation model**
    each states and it's transition rates, defined by users
    | EPIDEMIC MODEL - SIR
    | S - Spreader - People who spread the information
    | I - Ignorant - People who don't know about the information
    | R - Recovered - People who stopped spreading the information
    | At any time S+I+R = Number of nodes (N)
    '''


    def __init__(self, graph, i_to_s_rate=0.1, s_to_r_rate=0.1, i_to_r_rate=0.1):
        '''
        :param graph: The input graph
        :param i_to_s_rate: Rate of Transition from State I to S
        :param s_to_r_rate: Rate of Transition from State S to R
        :param i_to_r_rate: Rate of Transition from State I to R

        This function is used to instantiate the SIR model with inputs such as graph and transition rates.
        '''
        self.graph = graph
        self.i_to_s_rate = i_to_s_rate
        self.s_to_r_rate = s_to_r_rate
        self.i_to_r_rate = i_to_r_rate


    def initialize_model(self, s_nodes, r_nodes):
        '''
        :param s_nodes: State S nodes
        :param r_nodes: State R nodes
        :return:

        I nodes are calculated as I = N - (S+R)
        | N is total number of nodes
        '''
        total_node_list = self.graph.nodes()
        total_nodes = len(total_node_list)
        i_nodes = total_nodes - (s_nodes+r_nodes)
        def find_elements(node_list, no_of_nodes, state, other_state_nodes):
            elements = set()
            count = 0
            while count < no_of_nodes:
                if len(elements) == count:
                    count = count + 1
                node_id = random.choice(node_list)
                #print(node_id)
                if node_id not in other_state_nodes:
                    elements.add(node_id)
                    self.graph.node[node_id]['state'] = state
                    self.graph.node[node_id]['b'] = random.randrange(0,100)/100
            return list(elements)
        s_node_list = find_elements(total_node_list,s_nodes,'S',[])
        #print(len(s_node_list))
        r_node_list = find_elements(total_node_list,r_nodes,'R',s_node_list)
        #print(len(r_node_list))


    def get_nodes_in_state(self, state):
        '''
        :param state:
        :return:

        Returns all the nodes of graph belonging to a state
        '''

        node_list = self.graph.nodes()
        state_node = []

        for each in node_list:
            if self.graph.node[each]['state'] == state:
                state_node.append(each)
        return state_node

    def current_state(self, states = ['S','I','R']):
        '''
        :param states: Different states
        :return: a list containing number of nodes belonging to each state
        Used to calculate the nodes belonging to each state at current time
        '''
        state_list = [len(self.graph.nodes())]
        for each in states:
            state_list.append(len(self.get_nodes_in_state(each)))
        return state_list


    def show_current_state(self, states=['S','I','R']):
        '''
        :param states: Different states
        :return: It visualizes the current state of nodes
        '''

        states.insert(0,'total')
        nodes_by_state = self.current_state(states)
        plt.bar(states, nodes_by_state)
        plt.xlabel('States')
        plt.ylabel('Number of Nodes')
        plt.title('Current State of Nodes in Graph')
        plt.show()

'''
dataset = gl.GraphLoader("D:/Study/RumorDatasets/facebook_combined.txt/facebook_combined.txt")
total = len(dataset.G.nodes())

s_nodes = round(total*0.3)
r_nodes = round(total*0.2)
print(s_nodes)
print(r_nodes)
model = SIR(dataset.G)
model.initialize_model(s_nodes,r_nodes)
model.show_current_state()
'''