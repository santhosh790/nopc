import graph.graphloader as gl
from interaction import interactor, model, opinion
from neighborhood import algorithms
import collections
import os
from dotenv import find_dotenv
from dotenv import load_dotenv

env_file = find_dotenv(".env.dev")
load_dotenv(env_file)


def run():
    dataset = gl.GraphLoader(os.getenv('FILE_PATH'))
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



