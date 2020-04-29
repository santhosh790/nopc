import random


class interactor:
    """
    A class file responsible for opinion based interaction.

    """
    def __init__(self, dataset, model, opinionupdater ):
        '''

        :param dataset:
        :param model:
        :param opinionupdater:

        While instantiating the interactor dataset, model and opinionupdater are passed as parameters
        '''
        self.dataset = dataset
        self.model = model
        self.opinionupdater = opinionupdater


    def interact(self, propagation_batch=20, no_of_batch=10):
        '''
        :param propagation_batch: The number of inital nodes for each interaction
        :param no_of_batch: number of interactions
        :return: state_flow: the list of nodes in each state after every interaction

        This function does the Actual interaction between the nodes.
        It updates the opinion of individuals after each interactions. User can extend this function
        to write their own interaction logic
        '''
        SI_nodes = self.dataset.get_nodes_in_state('S') + self.dataset.get_nodes_in_state('I')
        initial_nodes  =  random.sample(SI_nodes, propagation_batch)
        iter_node = 0
        #print(initial_nodes)
        state_flow = dict()
        while(iter_node < no_of_batch):
            for each_node in initial_nodes:
                state = self.model.graph.node[each_node]['state']
                #print("parent_state"+str(state))
                for each in self.model.graph.neighbors(each_node):
                    interaction_rate = random.uniform(0,1)
                    #print("interaction rate"+str(interaction_rate))
                    if self.model.graph.node[each]['b'] > interaction_rate:
                        #print(model.graph.node[each]['state'])
                        #model.graph.node[each]['state'] = state
                        self.opinionupdater.belief_update(self.model.graph, each_node, each)

            initial_nodes  =  random.sample(SI_nodes, propagation_batch)
            iter_node = iter_node + 1
            state_flow[iter_node] = self.model.current_state(['S','I','R'])

        return state_flow