# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.insert(0, os.path.abspath('C:/Users/alexc/OneDrive/Bureau/DOSSIER FAC/COURS/MASTER/SSD/M1/Développement logiciel/Project_2021_HAX712X'))

###################################### A LIRE ######################################
# Pour que sphinx trouve le module, il faut que vous modifiez le chemin d'accès ci-dessus
#####################################################################################

import stanford_theme
html_theme = 'stanford_theme'
html_theme_path = [stanford_theme.get_html_theme_path()]


# -- Project information -----------------------------------------------------

project = 'ASLTAM'
copyright = '2021, Bouarroudj Abdelmalek, Capel Alexandre, Carvaillo Thomas'
author = 'Bouarroudj Abdelmalek, Capel Alexandre, Carvaillo Thomas'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.todo',
'sphinx.ext.viewcode',
'sphinx.ext.autosectionlabel',
'sphinx_tabs.tabs'
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']