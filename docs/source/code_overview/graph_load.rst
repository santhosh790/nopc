The Graph Loader
===================
This Class is responsible for loading the graph structure from a file.

Input format
############

The dataset should contain the input as follows:
	
	.. code-block:: python
		
		0 1
		1 2
		4 3
		2 3
		2 5
		0 4

From line #1, the graph will create an edge from node '0' to node '1'. If node not available, it will be created before creating an edge 


Graph Loader
############

.. autoclass:: graph.GraphLoader
   :inherited-members:
   
.. autofunction:: graph.GraphLoader.__init__


	