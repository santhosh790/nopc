Quick Start
===========

In this section, we go over everything you need to know to start loading graphs
and finding most influencers using nopc, the Python Package for NOpC. It's fun and
easy. Let's get started.

Prerequisites
-------------

:Python Knowledge: You need to know at least a little Python to use nopc; it's a Python package
                   after all. NOpC supports `Python 3.5+`_. If you are stuck on a problem,
                   `r/learnpython`_ is a great place to ask for help.

:Networkx Knowledge: Though this package uses Networkx package to load and manipulate bigger graphs, the users are not 
						expected to know about Networkx.


.. _`Python 3.5+`: https://docs.python.org/3/tutorial/index.html
.. _`r/learnpython`: https://www.reddit.com/r/learnpython/


.. _`First Steps Guide`:
   https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

With these prerequisites satisfied, you are ready to learn how to do some of
the most common tasks with Reddit's API.

Steps for calculating NOpC
------------
In order to calculate Neighborhood Opinion Centrality, we need to have a social network with opinions of people updated every interaction.
To simulate the interaction and calculate the NOpC, we will do few steps as follows:


Load your network using GraphLoader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First task in this module is to load the graph. A graph can be loaded using a input file.
Input file will look like this:
		.. code-block:: python
			
		   0 3
		   0 4
		   1 3
		   2 3
	
In this, the edge will be created between node 0 to node 3.

You need an instance of the :class:`.GraphLoader` class to do *anything* with
PRAW. After loading the dataset, next step is to define your interaction model:
:ref:`Define Model <read-only>`, and interaction between nodes :ref:`opinionUpdate <opinionUpdate>`.

.. _read-only:

Define your Model or Use SIR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a model using SIR, create :class:`.SIR` instance. For this, you need three pieces of
information:

1) Rate of Transition from State I to S
2) Rate of Transition from State S to R
3) Rate of Transition from State I to R

You may choose to provide these by passing in three keyword arguments when
calling the initializer of the :class:`.SIR` Values of this transition rates will typically be from 0 to 1.
For example:

.. code-block:: python

   import nopc

   dataset = nopc.graph.graphloader.GraphLoader("/path/to/dataset.txt")
   SIRModel = nopc.interaction.model.SIR(dataset.G, 0.1, 0.2, 0.1)

When you instantiate the model, all nodes will be available in state 'I'. You can keep different number of nodes in each state 'S', 'I', and 'R. To do this, you can initialize the model.

.. code-block:: python

   total = len(dataset.G.nodes())

   s_nodes = round(total*0.3)
   r_nodes = round(total*0.2)

   SIRModel.initialize_model(s_nodes,r_nodes)

 
With this, 50% of the nodes are in 'I' state, 30% are in state 'S' and 20% are in state 'R'.


.. _opinionUpdate:

Define Intraction and Opinion Update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next step is to simulate the interaction between nodes using the SIR model and update the opinions of individuals during interaction.
Now we need to initiate the interactor and opinion updator.

.. code-block:: python

   opinion_updater = nopc.interaction.opinion.opinion_updater(0.2)
   interaction = nopc.interaction.interactor()

Here, **0.2** is the belief threshold of the opinion update. Opinions of the interacting individuals can be updated only if it is above to this value.


Simulate the interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to simulate the interaction, we need to pass the dataset, model and opinion updater along with the batch size.

.. code-block:: python

   interaction.interact(dataset, SIRModel, opinion_updater, 20)
   
batch size defines the number of interaction occurs between nodes.


Calculate Neighborhood Opinion Centrality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After this interaction, we know opinions of the individuals are updated. We can now calculate the NOpC.

.. code-block:: python

    neighborhoodAlgo = nopc.neighborhood.algorithms.neighborhood()
    

Sort Nodes and Find most influential Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Final step is to sort the nodes based on interaction influence. After that top nodes (required numbers)
can be taken as most influential nodes.

.. code-block:: python

   sorted_nodes_by_opinion = neighborhoodAlgo.nei_Op_and_Deg_Dist(SIRModel)
   print(collections.orderedDict(sorted_nodes_by_opinion[:20]))

.. note:: In this example we have taken first 20 nodes as most influential nodes. This number is depending on the requirements.
