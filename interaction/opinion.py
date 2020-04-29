class opinion_updater:
    '''
    This class updates the opinions of individuals
    '''

    def __init__(self, belief_threshold):
        '''
        :param belief_threshold: A threshold value
        Belief threshold is initialized. The interaction between any pair of nodes can happen only if the belief of a person is
        greater than this belief threshold
        '''
        print("opinion update")
        self.belief_threshold = belief_threshold

        ## Check if given two nodes are neighbors in the graph
    def is_neighbors(self, graph, node1, node2):
        return node2 in graph.neighbors(node1)
        """neighbor = [each for each in graph.neighbors(node1) if each == node2]
        #if len(neighbor)>0:
        #    return True
        return False"""

    def belief_update(self, graph, node1, node2):
        '''
        :param graph: Input graph
        :param node1: Sender
        :param node2: Receiver
        :return:

        After every interaction, the belief of the participants gets updated only when it is higher than belief threshold
        '''
        #print("updates the belief of individuals")
        node1_val = graph.node[node1]
        node2_val = graph.node[node2]
        if graph.has_node(node1) and graph.has_node(node1) and self.is_neighbors(graph, node1, node2):
            #print(node1_val['b']-node2_val['b'])
            if node1_val['b']-node2_val['b'] > self.belief_threshold:
                graph.node[node1]['b'] = node1_val['b'] + node2_val['b']
                #print("opinion updated for "+str(node1)+ "value:"+str(graph.node[node1]['b']))
            elif node2_val['b']-node1_val['b'] > self.belief_threshold:
                #print("opinion value"+str(graph.node[node2]['b']))
                graph.node[node2]['b'] = node1_val['b'] + node2_val['b']
                #print("opinion updated for "+str(node2)+ "value:"+str(graph.node[node1]['b']))

        ## Belief Distance of a node among their neighbors
    def belief_distance(self, graph, node):
        belief_sum = 0
        if graph.has_node(node):
            for each in graph.neighbors(node):
                belief_sum = belief_sum+graph.node[each]['b']
        return belief_sum

        ## Closeness of a node among their neigbors
    def belief_closeness(self, graph, node):
        return 1/self.belief_distance(graph, node)

'''
opinion_updater(0.53)
'''