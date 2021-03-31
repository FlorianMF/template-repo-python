"""Root package info."""
import logging as __logging
import os

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

__author_name__ = 'AUTHOR_NAME'
__author_email__ = 'AUTHOR_EMAIL'
__maintainer_name__ = 'MAINTAINER_NAME'
__maintainer_email__ = 'MAINTAINER_EMAIL'
__license__ = 'LICENSE'
__copyright__ = f'Copyright (c) 2020-2021, {__author_name__}.'
__homepage__ = 'https://github.com/GITHUB_NAME/REPONAME'
__download_url__ = 'https://github.com/GITHUB_NAME/REPONAME'
# this has to be simple string, see: https://github.com/pypa/twine/issues/522
__docs__ = "PACKAGE_DESCRIPTION"
__long_docs__ = """
What is it?
-----------
Describe the package

Second title
----------------
Description

Another title
------------------
Description
"""

_logger = __logging.getLogger("REPONAME")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)
