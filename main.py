import graph.graphloader as gl
from interaction import interactor, model, opinion
from neighborhood import algorithms
import collections


def run():
    dataset = gl.GraphLoader("D:/Study/RumorDatasets/facebook_combined.txt/facebook_combined.txt")
    SIRModel = model.SIR(dataset.G)
    opinion_updater = opinion.opinion_updater(0.2)
    interaction = interactor()


    total_nodes = len(dataset.G.nodes())
    s_nodes = round(total_nodes*0.3)
    r_nodes = round(total_nodes*0.2)
    SIRModel.initialize_model(s_nodes, r_nodes)

    interaction.interact(dataset, SIRModel, opinion_updater, 20)

    neighborhoodAlgo = algorithms.neighborhood
    sorted_nodes_by_opinion = neighborhoodAlgo.nei_Op_and_Deg_Dist(SIRModel)

    print(collections.orderedDict(sorted_nodes_by_opinion[:20]))



