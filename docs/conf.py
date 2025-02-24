# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('source'))

master_doc = 'index'  # This points to docs/source/index.rst
project = 'SemanticST'
copyright = '2025, Roxana'
author = 'Roxana'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Auto-generate API docs
    'sphinx.ext.napoleon',  # Support Google-style docstrings
    'myst_nb',              # Enable Jupyter Notebook support
]
edit_on_github = True

# Allow Markdown and Jupyter notebooks
nb_execution_mode = "off"  # Prevents execution of notebooks during build
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static','source/notebooks/IMG_notebook']



