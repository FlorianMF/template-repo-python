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

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import versioneer
import os
import unittest
import REPONAME

PATH_ROOT = os.path.dirname(__file__)


def get_test_suite():
    """
    Prepare a test-suite callable with:
        python setup.py test
    """
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


def load_requirements(
        path_dir=PATH_ROOT,
        file_name='install.txt',
        comment_char='#'):
    with open(os.path.join(path_dir, 'requirements', file_name), 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    requirements = []
    for ln in lines:
        if ln.startswith("-r"):
            requirements += load_requirements(path_dir, ln.split(" ")[1])
        # filer all comments
        if comment_char in ln:
            ln = ln[:ln.index(comment_char)].strip()
        # skip directly installed dependencies
        if ln.startswith('http'):
            continue
        if ln:  # if requirement is not empty
            requirements.append(ln)
    return requirements


def load_long_description():
    url = os.path.join(
        REPONAME.__homepage__,
        'raw',
        REPONAME.__version__,
        'docs')
    text = open('README.md', encoding='utf-8').read()
    # replace relative repository path to absolute link to the release
    text = text.replace('](docs', f']({url}')
    # SVG images are not readable on PyPI, so replace them  with PNG
    text = text.replace('.svg', '.png')
    return text


def read_file(file):
    with open(file) as f:
        content = f.read()
    return content


# https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras
# Define package extras. These are only installed if you specify them.
# From remote, use like `pip install PACKAGENAME[dev, docs]`
# From local copy of repo, use like `pip install ".[dev, docs]"`
extras = {
    #     'docs':     load_requirements(file_name='docs.txt'),
    #     'examples': load_requirements(file_name='examples.txt'),
    #     'extra':    load_requirements(file_name='extra.txt'),
    #     'test':     load_requirements(file_name='test.txt')
}
# extras['dev'] = extras['extra'] + extras['test']
# extras['all'] = extras['dev'] + extras['examples'] + extras['docs']


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
    long_description=read_file(
        os.path.join(
            PATH_ROOT,
            "README.md")),
    # Optional
    # long_description=load_long_description(),  # Optional
    long_description_content_type='text/markdown',  # Optional

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    # A list of strings or a comma-separated string providing descriptive
    # meta-data.
    keywords=[
        'keyword1',
        'keyword2',
        'keyword3',
        'keywordn'
    ],  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    packages=find_packages(
        exclude=[
            'tests',
            'tests/*',
            'benchmarks',
            'docs']),  # Required
    include_package_data=True,
    zip_safe=False,

    platforms='any',
    setup_requires=[],
    install_requires=load_requirements(),   # Optional
    extras_require=extras,
    python_requires='>=3.6*',

    test_suite='setup.get_test_suite',
    tests_require=["coverage"],

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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    entry_points={
        'console_scripts': [
            'script_name = folder.script:main'
        ]}
)
