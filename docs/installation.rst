Installation
============

The SemanticST package is developed based on the PyTorch framework and is compatible with both CPU and GPU. 
For optimal performance, we recommend running the package on GPU. Please ensure that PyTorch and CUDA are installed correctly.

To run SemanticST, all dependencies listed in the 'requirements.txt' file need to be installed. We provide two installation methods for the SemanticST package: using pip or through Anaconda.

Please note that the current version of SemanticST is fully supported on Linux. 

1. Python Installation
----------------------

To install SemanticST using pip, follow these steps:

.. code-block:: bash

   pip install semanticst

   or

   git clone https://github.com/yourusername/SemanticST.git

   cd SemanticST

   pip install -r requirements.txt
   
   # To install the package:
   python setup.py install --user

2. Anaconda Installation
-------------------------

For convenience, we suggest using a separate conda environment to run SemanticST. Please ensure Anaconda is installed.

To create a conda environment and install the SemanticST package, follow these steps:

.. code-block:: bash

   # Create a conda environment called SemanticST
   conda create -n SemanticST python=3.9

   # Activate your environment
   conda activate SemanticST

   # Install dependencies
   pip install -r requirements.txt

   # Install SemanticST package
   python setup.py install --user

   # To use the environment in Jupyter Notebook, add the Python kernel for this environment:
   pip install ipykernel

   python -m ipykernel install --user --name=SemanticST
Required Dependencies
====================

To install the dependencies using pip, you can simply run:

.. code-block:: bash

   pip install -r requirements.txt
