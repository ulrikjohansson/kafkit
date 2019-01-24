import os
import sys

from documenteer.sphinxconfig.utils import form_ltd_edition_name
import lsst_sphinx_bootstrap_theme


# Work around Sphinx bug related to large and highly-nested source files
sys.setrecursionlimit(2000)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'numpydoc',
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
    'documenteer.sphinxext'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Kafkit'
copyright = '2019 Association of Universities for Research in Astronomy'
author = 'LSST Data Management'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if os.getenv('TRAVIS_BRANCH', default='master') == 'master':
    # Use the current release as the version tag if on master
    version = 'Current'
    release = version
else:
    # Use branch name as the version tag
    version = form_ltd_edition_name(
        git_ref_name=os.getenv('TRAVIS_BRANCH', default='master'))
    release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'README.rst'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The reST default role cross-links Python (used for this markup: `text`)
default_role = 'py:obj'

# Intersphinx

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'aiohttp': ('https://aiohttp.readthedocs.io/en/stable/', None),
    'aiokafka': ('https://aiokafka.readthedocs.io/en/stable/', None),
    'fastavro': ('https://fastavro.readthedocs.io/en/latest/', None),
}

# This is added to the end of RST files - a good place to put substitutions
# to be used globally.
rst_epilog = """
.. _Confluent Schema Registry: https://docs.confluent.io/current/schema-registry/docs/index.html
.. _aiokafka: https://aiokafka.readthedocs.io/en/stable/
.. _aiohttp: https://aiohttp.readthedocs.io/en/stable/
"""

# -- Options for linkcheck builder ----------------------------------------

numpydoc_show_class_members = False
autosummary_generate = True
automodsumm_inherited_members = True
autodoc_inherit_docstrings = True
autoclass_content = "class"
autodoc_default_flags = ["show-inheritance", "special-members"]

# -- Options for linkcheck builder ----------------------------------------

linkcheck_retries = 2

linkcheck_ignore = ['http://registry:8081']

# -- Options for HTML output ----------------------------------------------

templates_path = [
    '_templates',
    lsst_sphinx_bootstrap_theme.get_html_templates_path()
]

html_theme = 'lsst_sphinx_bootstrap_theme'
html_theme_path = [lsst_sphinx_bootstrap_theme.get_html_theme_path()]


html_context = {
    # Enable "Edit in GitHub" link
    'display_github': True,
    # https://{{ github_host|default("github.com") }}/{{ github_user }}/
    #     {{ github_repo }}/blob/
    #     {{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'lsst-sqre',
    'github_repo': 'kafkit',
    'conf_py_path': 'docs/',
    # TRAVIS_BRANCH is available in CI, but master is a safe default
    'github_version': os.getenv('TRAVIS_BRANCH', default='master') + '/'
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'logotext': project}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
