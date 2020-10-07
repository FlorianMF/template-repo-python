# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sphinx.ext.doctest
from sphinx import addnodes
from docutils import nodes
import inspect
import os
import shutil
import glob
import sys
import pypandoc
import florianmf_sphinx_theme  # noqa: E402

PATH_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_ROOT = os.path.dirname(os.path.dirname(PATH_HERE))
sys.path.insert(0, os.path.abspath(PATH_ROOT))

SPHINX_MOCK_REQUIREMENTS = int(
    os.environ.get(
        'SPHINX_MOCK_REQUIREMENTS',
        True))

import REPONAME  # noqa: E402

# Copy over markdown files
for md in [
    'README.md',
]:
    md = md.lower()
    shutil.copy(os.path.join(PATH_ROOT, md), os.path.join(PATH_HERE, md))
for md in glob.glob(os.path.join(PATH_ROOT, '.github', '*.md')):
    if not os.path.basename(md).lower() == 'pull_request_template.md':
        shutil.copy(md, os.path.join(PATH_HERE, os.path.basename(md).lower()))

# Extract parts of the readme -> getting_started.rst
converted_readme = pypandoc.convert_file('readme.md', 'rst').split('\n')
os.remove('readme.md')

rst_file = []
skip = False

# TODO adapt which lines should be maintained and which skipped
# skip problematic parts
for line in converted_readme:
    if any([line.startswith(x) for x in [
        '.. container::',
        '   |PyPI|',
        '.. |PyPI|',
        '|PyPI|',
        'Why another framework?',
        '   logo',
        '.. raw:: html'
    ]
    ]):
        skip = True
    elif any([line.startswith(x) for x in [
        'What is ``PACKAGENAME``?',
        'Installation',
        'How to',
        '.. figure:: _images/logos/PACKAGENAME_logo.png'
    ]
    ]):
        skip = False

    if not skip:
        rst_file.append(
            line.replace(
                'docs/source/_images',
                '_images').replace(
                '.svg',
                '.png'))

with open('getting_started.rst', 'w') as f:
    f.write('\n'.join(rst_file))

# -- Project information -----------------------------------------------------

project = 'PACKAGENAME'
copyright = REPONAME.__copyright__
author = REPONAME.__author_name__

# The short X.Y version
version = REPONAME.__version__
# The full version, including alpha/beta/rc tags
release = REPONAME.__version__

IS_RELEASE = not (
    '+' in version or 'dirty' in version or len(version.split('.')) > 3)

# Options for the linkcode extension
# ----------------------------------
github_user = 'GITHUB_NAME'
github_repo = project

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

needs_sphinx = '2.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    # 'sphinxcontrib.mockautodoc',  # raises error: directive 'automodule' is already registered ...
    # 'sphinxcontrib.fulltoc',  # breaks pytorch-theme with unexpected kw argument 'titles_only'
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.linkcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx.ext.autosectionlabel',
    'sphinx_autodoc_typehints',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    # 'm2r',
    # 'nbsphinx',  # it seems some sphinx issue
    'sphinx_copybutton',
    'sphinx_paramlinks',
    'sphinx_togglebutton',
]

# napoleon_use_ivar = True
# Add any paths that contain templates here, relative to this directory.

templates_path = ['_templates_stable'] if IS_RELEASE else ['_templates']

# https://berkeley-stat159-f17.github.io/stat159-f17/lectures/14-sphinx..html#conf.py-(cont.)
# https://stackoverflow.com/questions/38526888/embed-ipython-notebook-in-sphinx-document
# I execute the notebooks manually in advance. If notebooks test the code,
# they should be run at build time.
nbsphinx_execute = 'never'
nbsphinx_allow_errors = True
nbsphinx_requirejs_path = ''


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
# source_suffix = ['.rst', '.md', '.ipynb']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
    '.ipynb': 'nbsphinx',
}

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    'PULL_REQUEST_TEMPLATE.md',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
# pygments_style = None # as in PACKAGENAME

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# http://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
# html_theme = 'bizstyle'
# https://sphinx-themes.org
html_theme = 'florianmf_sphinx_theme'
html_theme_path = [florianmf_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'canonical_url': REPONAME.__homepage__,
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': False,
}

html_logo = '_images/logos/PACKAGENAME_logo.svg'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_images', '_templates', '_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = project + '-doc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
     project
     + '.tex',
     project
     + ' Documentation',
     author,
     'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project, project + ' Documentation', [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, project + ' Documentation', author, project,
     'One line description of project.', 'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'PIL': ('https://pillow.readthedocs.io/en/stable/', None),
    'dill': ('https://dill.readthedocs.io/en/stable', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Disable docstring inheritance
autodoc_inherit_docstrings = True

# https://github.com/rtfd/readthedocs.org/issues/1139
# I use sphinx-apidoc to auto-generate API documentation for my project.
# Right now I have to commit these auto-generated files to my repository
# so that RTD can build them into HTML docs. It'd be cool if RTD could run
# sphinx-apidoc for me, since it's easy to forget to regen API docs
# and commit them to my repo after making changes to my code.

PACKAGES = [
    REPONAME.__name__,
]

# Prolog and epilog to each notebook:
# https://nbsphinx.readthedocs.io/en/0.7.0/prolog-and-epilog.html

ENABLE_DOWNLOAD_LINK = True

nbsphinx_kernel_name = 'python3'

github_path = r'https://github.com/%s/%s/blob/master/notebooks/{{ env.doc2path(env.docname, base=None) }}' % (
    github_user, github_repo)
colab_path = github_path.replace(
    'https://github.com',
    'https://colab.research.google.com/github')
nbsphinx_execute = 'never'

# copy all notebooks to local folder
nb_suffix = 'notebooks'
path_nbs = os.path.join(PATH_HERE, nb_suffix)
os.makedirs(path_nbs, exist_ok=True)
for path_ipynb in glob.glob(os.path.join(PATH_ROOT, nb_suffix, '*.ipynb')):
    path_ipynb2 = os.path.join(path_nbs, os.path.basename(path_ipynb))
    shutil.copy(path_ipynb, path_ipynb2)

if ENABLE_DOWNLOAD_LINK:
    nbsphinx_prolog = r"""
    .. raw:: html
            <div class="pytorch-call-to-action-links">
                <a href="%s">
                <div id="google-colab-link">
                <img class="call-to-action-img" src="_static/_images/pytorch-colab.svg"/>
                <div class="call-to-action-desktop-view">Run in Google Colab</div>
                <div class="call-to-action-mobile-view">Colab</div>
                </div>
                </a>
                <a href="%s" download>
                <div id="download-notebook-link">
                <img class="call-to-action-notebook-img" src="_static/_images/pytorch-download.svg"/>
                <div class="call-to-action-desktop-view">Download Notebook</div>
                <div class="call-to-action-mobile-view">Notebook</div>
                </div>
                </a>
                <a href="%s">
                <div id="github-view-link">
                <img class="call-to-action-img" src="_static/_images/pytorch-github.svg"/>
                <div class="call-to-action-desktop-view">View on GitHub</div>
                <div class="call-to-action-mobile-view">GitHub</div>
                </div>
                </a>
            </div>
    """ % (colab_path, r"{{ env.doc2path(env.docname, base=None) }}", github_path)

else:
    nbsphinx_prolog = r"""
    .. raw:: html
            <div class="pytorch-call-to-action-links">
                <a href="%s">
                <div id="google-colab-link">
                <img class="call-to-action-img" src="_static/_images/pytorch-colab.svg"/>
                <div class="call-to-action-desktop-view">Run in Google Colab</div>
                <div class="call-to-action-mobile-view">Colab</div>
                </div>
                </a>
                <a href="%s">
                <div id="github-view-link">
                <img class="call-to-action-img" src="_static/_images/pytorch-github.svg"/>
                <div class="call-to-action-desktop-view">View on GitHub</div>
                <div class="call-to-action-mobile-view">GitHub</div>
                </div>
                </a>
            </div>
    """ % (colab_path, github_path)

# only run doctests marked with a ".. doctest::" directive
# Without this, doctest adds any example with a `>>>` as a test
doctest_test_doctest_blocks = ''
doctest_default_flags = sphinx.ext.doctest.doctest.ELLIPSIS

# Ignoring Third-party packages
# https://stackoverflow.com/questions/15889621/sphinx-how-to-exclude-imports-in-automodule

# Ignoring Third-party packages
# https://stackoverflow.com/questions/15889621/sphinx-how-to-exclude-imports-in-automodule


def package_list_from_file(file):
    mocked_packages = []
    with open(file, 'r') as fp:
        for ln in fp.readlines():
            found = [ln.index(ch) for ch in list(',=<>#') if ch in ln]
            pkg = ln[:min(found)] if found else ln
            if pkg.rstrip():
                mocked_packages.append(pkg.rstrip())
    return mocked_packages


MOCK_REQUIRE_PACKAGES = []
if SPHINX_MOCK_REQUIREMENTS:
    # mock also base packages when we are on RTD since we don't install them
    # there
    MOCK_REQUIRE_PACKAGES += package_list_from_file(
        os.path.join(PATH_ROOT, 'requirements/install.txt'))
    # MOCK_PACKAGES += package_list_from_file(os.path.join(PATH_ROOT, 'requirements/extra.txt'))

# TODO: better parse from package since the import name and package name
# may differ
MOCK_MANUAL_PACKAGES = [
    'numpy',
    'dill'
]
autodoc_mock_imports = MOCK_REQUIRE_PACKAGES + MOCK_MANUAL_PACKAGES
# for mod_name in MOCK_REQUIRE_PACKAGES:
#     sys.modules[mod_name] = mock.Mock()


# Resolve function
# This function is used to populate the (source) links in the API
def linkcode_resolve(domain, info):
    def find_source():
        # try to find the file and line number, based on code from numpy:
        # https://github.com/numpy/numpy/blob/master/doc/source/conf.py#L286
        obj = sys.modules[info['module']]
        for part in info['fullname'].split('.'):
            obj = getattr(obj, part)
        fname = inspect.getsourcefile(obj)
        # https://github.com/rtfd/readthedocs.org/issues/5735
        if any([s in fname for s in ('readthedocs', 'rtfd', 'checkouts')]):
            # /home/docs/checkouts/readthedocs.org/user_builds/PACKAGENAME/checkouts/
            #  devel/PACKAGENAME/utilities/cls_experiment.py#L26-L176
            path_top = os.path.abspath(os.path.join('..', '..', '..'))
            fname = os.path.relpath(fname, start=path_top)
        else:
            # Local build, imitate master
            fname = 'master/' + \
                os.path.relpath(fname, start=os.path.abspath('..'))
        source, lineno = inspect.getsourcelines(obj)
        return fname, lineno, lineno + len(source) - 1

    if domain != 'py' or not info['module']:
        return None
    try:
        filename = '%s#L%d-L%d' % find_source()
    except Exception:
        filename = info['module'].replace('.', '/') + '.py'
    # import subprocess
    # tag = subprocess.Popen(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE,
    #                        universal_newlines=True).communicate()[0][:-1]
    branch = filename.split('/')[0]
    # do mapping from latest tags to master
    branch = {'latest': 'master', 'stable': 'master'}.get(branch, branch)
    filename = '/'.join([branch] + filename.split('/')[1:])
    return "https://github.com/%s/%s/blob/%s" \
           % (github_user, github_repo, filename)


autodoc_member_order = 'groupwise'
autoclass_content = 'both'
# the options are fixed and will be soon in release,
#  see https://github.com/sphinx-doc/sphinx/issues/5459
autodoc_default_options = {
    'members': None,
    'methods': None,
    # 'attributes': None,
    'special-members': '__call__',
    'exclude-members': '_abc_impl',
    'show-inheritance': True,
    'private-members': True,
    'noindex': True,
}

# Sphinx will add “permalinks” for each heading and description environment as paragraph signs that
#  become visible when the mouse hovers over them.
# This value determines the text for the permalink; it defaults to "¶". Set it to None or the empty
#  string to disable permalinks.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_add_permalinks
html_add_permalinks = "¶"

# True to prefix each section label with the name of the document it is in, followed by a colon.
#  For example, index:Introduction for a section called Introduction that appears in document index.rst.
#  Useful for avoiding ambiguity when the same section heading appears in different documents.
# http://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
autosectionlabel_prefix_document = True

html_show_sphinx = False

coverage_skip_undoc_in_source = True