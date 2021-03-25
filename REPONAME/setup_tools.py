import os
from typing import List
import unittest
import REPONAME
from REPONAME import _PROJECT_ROOT


def get_test_suite():
    """
    Prepare a test-suite callable with:
        python setup.py test
    """
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


def load_requirements(
        path_dir: str = os.path.join(_PROJECT_ROOT, 'requirements'),
        file_name: str = 'install.txt',
        comment_char: str = '#'
) -> List[str]:
    """Load requirements from a file
    """
    with open(os.path.join(path_dir, file_name), 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    requirements = []
    for ln in lines:
        # import linked requirements file
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
        pxd_torch.__homepage__,
        'raw',
        pxd_torch.__version__,
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


def get_test_suite():
    """
    Prepare a test-suite callable with:
        python setup.py test
    """
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite
