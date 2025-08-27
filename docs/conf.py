import os
import sys

# Allow Sphinx to import your project packages
sys.path.insert(0, os.path.abspath('..'))  # project root (where manage.py lives)

# --- Django setup for autodoc ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySite.settings')
import django
django.setup()

# Root document
root_doc = 'index'

# -- Project information -----------------------------------------------------
project = 'mySite'
author = 'Vittorio'
copyright = '2025, Vittorio'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',   # Google/NumPy docstring support
]

templates_path = ['_templates']

# Exclude build artifacts, OS files, and Django migrations from docs
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'personal.migrations*',
]

# Use English (or comment this line out to use default)
language = 'en'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Optional: nicer type hints in signatures (keeps docstrings clean)
# autodoc_typehints = 'description'
