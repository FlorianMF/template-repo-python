#!/usr/bin/env python
# Copyright The AUTHOR_NAME team.
#
# Licensed under the LICENSE;
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at LICENSE_URL ...
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

import REPONAME
import versioneer
from REPONAME import setup_tools

PATH_ROOT = os.path.dirname(__file__)


# https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras
# Define package extras. These are only installed if you specify them.
# From remote, use like `pip install REPONAME[dev, docs]`
# From local copy of repo, use like `pip install ".[dev, docs]"`
def _prepare_extras():
    extras = {
        'docs': setup_tools.load_requirements(file_name='docs.txt'),
        'examples': setup_tools.load_requirements(file_name='examples.txt'),
        'extra': setup_tools.load_requirements(file_name='extra.txt'),
        'test': setup_tools.load_requirements(file_name='test.txt')
        #     'loggers':     setup_tools.load_requirements(file_name='loggers.txt')
    }
    extras['dev'] = extras['extra'] + extras['test'] + extras['docs']
    extras['all'] = extras['dev'] + extras['examples']
    return extras


# Configure the package build and distribution
#   @see https://github.com/pypa/setuptools_scm
#
# To record the files created use:
#   python setup.py install --record files.txt
setup(
    name='PACKAGENAME',  # Required
    version=versioneer.get_version(),  # Required
    cmdclass=versioneer.get_cmdclass(),  # Optional
    author=REPONAME.__author_name__,  # Optional
    author_email=REPONAME.__author_email__,  # Optional
    maintainer=REPONAME.__maintainer_name__,  # Optional
    maintainer_email=REPONAME.__maintainer_name__,  # Optional
    url=REPONAME.__homepage__,  # Optional
    download_url='https://github.com/GITHUB_NAME/REPONAME',  # Optional
    license=REPONAME.__license__,
    description='Program/Package to ...',  # Optional
    long_description=setup_tools.read_file(
        os.path.join(PATH_ROOT, "README.md")
    ),
    # Optional
    # long_description=load_long_description(),  # Optional
    long_description_content_type='text/markdown',  # Optional

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    # A list of strings or a comma-separated string providing descriptive
    # meta-data.
    keywords=['keyword1', 'keyword2', 'keyword3', 'keywordn'],  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    packages=find_packages(exclude=['tests', 'tests/*', 'benchmarks', 'docs']
                           ),  # Required
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    setup_requires=[],
    install_requires=setup_tools.load_requirements(file_name='install.txt'
                                                   ),  # Optional
    extras_require=_prepare_extras(),
    python_requires='>=3.6',

    # test_suite='setup.get_test_suite',
    # tests_require=["coverage"],
    project_urls={
        "Bug Tracker": "https://github.com/GITHUB_NAME/REPONAME/issues",
        # "Documentation": "https://REPONAME.rtfd.io/en/latest/",
        "Source Code": "https://github.com/GITHUB_NAME/REPONAME",
    },

    # Classifiers help users find your project by categorizing it.
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: AUDIENCE1',
        'Intended Audience :: AUDIENCE2',
        'Topic :: Scientific/Engineering :: TOPIC1',
        'Topic :: Scientific/Engineering :: TOPIC2',
        # Pick your license as you wish
        'License :: OSI Approved :: {} License'.format(REPONAME.__license__),
        'Operating System :: OS Independent',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={'console_scripts': ['script_name = folder.script:main']}
)
