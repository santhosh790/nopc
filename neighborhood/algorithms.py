

import collections

class neighborhood:
    '''
    This class is responsible for finding the influencers for anti-rumor propagation
    '''


    def __init__(self):
        print("influencer finder")

    def get_nodes_in_comm(self, graph, node_list, community):
        '''
        :param graph: Input graph
        :param node_list: List of nodes
        :param community: Community
        :return: list of nodes available in community
        It finds the list of nodes from given node list that belonging to a community
        '''
        node_in_state = []
        for each in node_list:
            if graph.node[each]['state'] == community:
                node_in_state.append(each)
        return node_in_state

    def seeds_by_random(self, node_list, seed_count):
        return random.sample(node_list,seed_count)


    def sort_nodes_by_belief(self, graph, node_list):
        '''

        :param graph:
        :param node_list:
        :return: a sorted list of nodes based on belief strength will be returned

        This sorting, sorts based on the belief of nodes in the node_list
        '''
        node_by_belief = {}
        for each in node_list:
            node_by_belief[each] = graph.node[each]['b_strength']
        sorted_nodes_by_belief = sorted(node_by_belief.items(), key=lambda kv: kv[1])
        return sorted_nodes_by_belief

        ## Herding influencer method - Identifying the influencers within the community

    def neiOpDist(self, graph):
        for node in graph.nodes():
            print(node)

    def neiDegDist(self, graph):
        for node in graph.nodes():
            print(node)

    def nei_Op_and_Deg_Dist(self, model):
        '''
        :param model: An interaction model containing the graph
        :return: A sorted list of nodes based on the opinion distance at current time

        This function is responsible for calculating NOpC. Overall algorithm is described in
        `NOpC`_
        .. _NOpC: https://link.springer.com/article/10.1007/s42452-019-1436-x
        '''
        degrees = model.graph.degree()
        nodes_by_belief_strength = {}

        for each in model.graph.nodes():
            deg_strength = 0

            for neighbor in model.graph.neighbors(each):
                deg_strength = deg_strength + degrees[each] + degrees[neighbor]

            #print("degStre"+str(deg_strength))
            model.graph.node[each]['deg_strength'] = deg_strength
            model.graph.node[each]['b_strength'] = deg_strength * dataset.G.node[each]['b']
            nodes_by_belief_strength[each] = deg_strength * dataset.G.node[each]['b']

        return sorted(nodes_by_belief_strength.items(), key=lambda kv: kv[1], reverse=True)

    def herding_influencer(self, graph, r_d, com_dict,prev_infln):
        print("herding influencer")
        herd_inf = []
        for comm in com_dict:
            pro_nodes = self.get_nodes_in_comm(graph, com_dict[comm] ,"P")
            ig_nodes = self.get_nodes_in_comm(graph, com_dict[comm] ,"I")
            seed_count = round(r_d*(0.4*(len(pro_nodes)+len(ig_nodes)))/len(com_dict))
            #print(seed_count)
            #filter(lambda i: i not in remove_list, test_list)
            influencers = self.sort_nodes_by_belief(graph, com_dict[comm])
            final_list = [x for x in influencers if x not in prev_infln]
            #print(str(final_list))
            herd_inf.extend(final_list[:seed_count])
            #print(herd_inf)

        return herd_inf

        ## Gateway Influencer method - Identifying the influencers on the bridge of two communities
    def gateway_influencer(self, graph, r_d, com_dict,prev_infln):
        print("gateway influencer")
        gate_inf = []
        for comm in com_dict:
            new_list = []
            for each_node in com_dict[comm]:
                gate_inf = [node for node in graph.neighbors(each_node) if node not in com_dict[comm]]
            gate_inf.extend(new_list)
        return gate_inf

        ## This method returns the combined herding and gateway influencers
        ## Parameters Graph, rumor density, community dictionary
    def influence_finder(self, graph, r_d, com_dict, prev_infln):
        print("Influence Combine")
        list1= self.herding_influencer(graph, r_d, com_dict,prev_infln)

        #print(list1)
        list2 = self.gateway_influencer(graph, r_d, com_dict,prev_infln)
        #print(list2)
        list1.extend(list2)
        #print(list1)
        return list1#self.herding_influencer(graph, r_d, com_dict,prev_infln).extend(self.gateway_influencer(graph, r_d, com_dict,prev_infln))

'''
dataset = gl.GraphLoader("D:/Study/RumorDatasets/facebook_combined.txt/facebook_combined.txt")
nh = neighborhood()
dataset.graph = dataset.G
print(nh.nei_Op_and_Deg_Dist(dataset))
'''
