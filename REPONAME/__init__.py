__version__ = '0.0.1'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__author_name__ = 'AUTHOR_NAME'
__author_email__ = 'AUTHOR_EMAIL'
__maintainer_name__ = 'MAINTAINER_NAME'
__maintainer_email__ = 'MAINTAINER_EMAIL'
__license__ = 'LICENSE'
__copyright__ = 'Copyright (c) 2020, %s.' % __author_name__
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
