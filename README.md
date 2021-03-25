<div align="center">

![Logo](docs/source/_images/logos/PACKAGENAME_logo.svg)

# template-repo-python

**This repository contains a fully-functional package structure including CI/CD workflows and (empty) tests.**

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="https://PACKAGENAME.readthedocs.io/en/stable/">Docs</a> •
  <a href="#examples">Examples</a> •
  <!-- <a href="#community">Community</a> • -->
  <a href="#licence">Licence</a>
</p>

**Change all occurrences of FlorianMF and template-repo-python. They are used set here only to check that the code works.**

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PACKAGENAME)](https://pypi.org/project/PACKAGENAME)
[![PyPI Package Version](https://badge.fury.io/py/PACKAGENAME.svg)](https://badge.fury.io/py/PACKAGENAME)
[![PyPI Version](https://img.shields.io/pypi/v/PACKAGENAME)](https://pypi.org/project/PACKAGENAME)
[![PyPI Status](https://pepy.tech/badge/PACKAGENAME)](https://pepy.tech/project/PACKAGENAME)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/PACKAGENAME)](https://pypi.org/project/PACKAGENAME)

[![DockerHub](https://img.shields.io/docker/pulls/DOCKER_AUTHOR_NAME/DOCKER_REPONAME.svg)](https://hub.docker.com/r/DOCKER_AUTHOR_NAME/DOCKER_REPONAME)

[![codecov](https://codecov.io/gh/AUTHOR_NAME/PACKAGENAME/branch/main/graph/badge.svg)](https://codecov.io/gh/AUTHOR_NAME/PACKAGENAME)
[![Coverage](https://img.shields.io/codecov/c/github/AUTHOR_NAME/PACKAGENAME)](https://codecov.io/gh/AUTHOR_NAME/PACKAGENAME)

[![Status](https://img.shields.io/pypi/status/PACKAGENAME)](https://pypi.org/project/template-repo-python)
![Docs](https://github.com/FlorianMF/template-repo-python/workflows/Docs%20Check/badge.svg)
[![ReadTheDocs](https://readthedocs.org/projects/PACKAGENAME/badge/?version=stable)](https://PACKAGENAME.readthedocs.io/en/stable/)
[![Slack](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://join.slack.com/t/PACKAGENAME/shared_invite/zt-f6bl2l0l-JYMK3tbAgAmGRrlNr00f1A)
[![Discourse status](https://img.shields.io/discourse/status?server=https%3A%2F%2Fforums.AUTHOR_NAME.ai)](https://forums.AUTHOR_NAME.ai/)
[![License](https://img.shields.io/badge/License-LICENSE-blue.svg)](https://github.com/FlorianMF/template-repo-python/blob/main/LICENSE)
[![Next Release](https://img.shields.io/badge/Next%20Release-Jan%202021-red.svg)](https://shields.io/)

[![Implementation](https://img.shields.io/pypi/implementation/PACKAGENAME)](https://pypi.org/project/PACKAGENAME)

[![Vulnerabilities](https://img.shields.io/snyk/vulnerabilities/github/AUTHOR_NAME/PACKAGENAME)](https://github.com/FlorianMF/template-repo-python/network/alerts)

[![Version tag](https://img.shields.io/github/v/tag/AUTHOR_NAME/PACKAGENAME)](https://github.com/FlorianMF/template-repo-python/releases)

| Python Version | Platform | Unittests | NotebookTests |
---              | ---      |  ---      | ---           |
| ![Python](https://img.shields.io/badge/python-3.6/3.7/3.8-orange) | ![System](https://img.shields.io/badge/Linux-blue) | ![Unittests Linux](https://github.com/FlorianMF/template-repo-python/workflows/Unittests%20Linux/badge.svg) | ![NotebookTests Linux](https://github.com/FlorianMF/template-repo-python/workflows/NotebookTests%20Linux/badge.svg) |
| ![Python](https://img.shields.io/badge/python-3.6/3.7/3.8-orange) | ![System](https://img.shields.io/badge/Windows-blue) | ![Unittests Windows](https://github.com/FlorianMF/template-repo-python/workflows/Unittests%20Windows/badge.svg) | ![NotebookTests Windows](https://github.com/FlorianMF/template-repo-python/workflows/NotebookTests%20Windows/badge.svg) |
| ![Python](https://img.shields.io/badge/python-3.6/3.7/3.8-orange) | ![System](https://img.shields.io/badge/MacOS-blue)   | ![Unittests macOS](https://github.com/FlorianMF/template-repo-python/workflows/Unittests%20MacOS/badge.svg)    | ![NotebookTests MacOS](https://github.com/FlorianMF/template-repo-python/workflows/NotebookTests%20MacOS/badge.svg) |

**For more badges check <https://github.com/badges/shields>. You can as well copy the badge code directly from the actions tab in your GitHub repo.**

</div>

## <span style="color:red">*Info about this template*</span>

## Template Content

It's features include (but are not limited to):

* An already working package structure
* A working requirement handling
* Automatic PyPI releases
* Pre-Configured CI/CD (with Github Actions or CircleCI)
* Code coverage analysis
* Python Code Style Checks
* Issue and pull request templates

> If you want to add something to this repo, please submit a PR. Contributions are very welcome.

## Scripts

The script [`scripts/configure`](scripts/configure.py) allows to replace the following in all files defined in the script:

* `REPONAME` : The name of your Git repository
* `PACKAGENAME` : The name of your package
* `GITHUB_NAME` : The name of GitHub account under which the repo is hosted
* `AUTHOR_NAME` : The name of author of the repo/package
* `AUTHOR_EMAIL` : The email of author of the repo/package
* `MAINTAINER_NAME` : The name of maintainer of the repo/package
* `MAINTAINER_EMAIL` : The email of maintainer of the repo/package

## Inspiration

This template took inspiration from several repos, including:

* [Justus Schock's template repo](https://github.com/justusschock/template-repo-python)
* [Pytorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning)
* [Pytorch Lightning Bolts](https://github.com/PyTorchLightning/pytorch-lightning-bolts)

<hr style="border:2px solid green"> </hr>

## <span style="color:red">*What to maintain*</span>

---

## Key Features

Describe the key features of your package.

## How to Use

### Step 0: Install locally

```bash
# clone project
git clone https://github.com/GITHUB_NAME/REPONAME.git

# install project
cd REPONAME
pip install .
pip install -r requirements/install.txt
```

### Step 0: Install from remote

Simple installation from PyPI

```bash
pip install PACKAGENAME
```

From Conda

```bash
conda install PACKAGENAME -c conda-forge
```

### Step 1: ...

Describe step 1

```python
Python examples
```

### Step 2: ...

Describe step 2

```python
Python examples
```

---

## Examples

#### Hello world

[hello world example](url)

#### Example category 2

[example 1](url)

[example 2](url)

---

## Asking for help

If you have any questions please:

1. [Read the docs](https://PACKAGENAME.rtfd.io/en/latest/).
1. [Look it up in our forum (or add a new question)](https://forums.PACKAGENAME.ai/)
1. [Search through the issues](https://github.com/GITHUB_NAME/REPONAME/issues?utf8=%E2%9C%93&q=my++question).
1. [Join our slack](https://join.slack.com/t/PACKAGENAME/shared_invite/zt-f6bl2l0l-JYMK3tbAgAmGRrlNr00f1A).
1. [Ask on stackoverflow](https://stackoverflow.com/questions/ask?guided=false) with the tag PACKAGENAME.

---

## Licence

Please observe the LICENSE license that is listed in this repository.

## BibTeX

If you want to cite the framework feel free to use this:

```bibtex
@misc{ARTICLE_NAME,
 title={TITLE},
 author={AUTHOR_NAME},
 journal={GitHub. Note: https://github.com/GITHUB_NAME/REPONAME},
 volume={VOLUME},
 year={YEAR}
}
```

**_You should modify everything in CAPS._**

<hr style="border:2px solid green"> </hr>

## <span style="color:red">*What to change*</span>

To customize this repo, you need to have a look at the following chapters.

### Directory-Name

You might want to customize your package-name.

To do this, you simply have to rename the `REPONAME` directory to whatever you want.
> Make sure, to also change the `PACKAGENAME` in the [`setup.py`](setup.py#L96), or you won't be able to install your package anymore!

### Main/Master branch

This template repo uses `main` as name for the principal branch. If you still use master, change all occurrences of `main` to `master`.

### Python Package Metadata

To customize your python package, you just have to change your [`setup.py`](setup.py) file.

The minimal setup looks like this:

```python
setup(
    name='PACKAGENAME',
    version=_version,
    packages=find_packages(),
    url='https://github.com/GITHUB_NAME/REPONAME',
    test_suite="unittest",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    tests_require=["coverage"],
    python_requires=">=3.6",
    author="AUTHOR_NAME",
    author_email="AUTHOR_EMAIL",
    license=license,
)
```

This includes the default information and must be adjusted to your needs:

* `name` provides the package-name you can later import
* `version` provides the package-version (which will currently be extracted from your package's `__init__.py`, but be also set manually)
* `packages` is a list defining all packages (and their sub-packages and the sub-packages of their sub-packages and so on...), that should be installed. This is automatically extracted by `find_packages`, which also accepts some sub-packages to ignore (besides some other arguments).
* `url` specifies the packages homepage (in this case the current GitHub repo); You might want to change it to your repos homepage.
* `test_suite` defines the test-suite to use for your unittests. In this repo template, we'll python's built-in framework `unittest`, but you can change this too; *Just make sure to also change this, when we get to CI/CD.*
* `long_description` does what it sayes: It provides a long description of your package. Currently this is parsed from your `README.md`
* `long_description_content_type` defines your description type; I set it to markdown in most cases
* `install_requires` is a list containing all your package requirements. They are automatically parsed from a `requirements.txt` file
* `tests_require` does the same thing for your unittests.
* `python_requires` specifies the python version, your package can be installed to (here it's been set to python 3.5 or above, since this is what I usually use). *Depending on the version you specify here, you might not be able to use all of python's latest features*
* `author` and `author_email` specify who you are.
* `license` specifies the license you want to release your code with. This is parsed from a `LICENSE` file.

There are still many other options to include here, but these are the most basic ones.

### Unittests

If you want to add/change some unit-tests, you should do this in a new python file starting with `test_`. [Here](https://docs.python.org/3/library/unittest.html) is a good introduction on how to write unittests with the `unittest` framework. After you added these tests, you may run them with either `coverage run -m unittest` or `python -m unittest`.

They are basically doing the same, but `coverage` additionally checks, how many of your code-lines are currently covered by your tests.

The unittests are also automatically triggered within [CI/CD](#cicd)

### Specifying Codecov

The [`.codecov.yml`](.codecov.yml) file specifies, how coverage should behave, how to calculate the coverage (i.e. what files to include for line counting) etc.

### Requirements

If you want to add new requirements, simply add them to the [`requirements/install.txt`](requirements/install.txt) file.
Special requirements for testing or docs building can be set [here](requirements/unittests.txt) and [here](requirements/docs.txt).

### Packaging on PyPI

If you plan to release your package on PyPI, ship wheels for it, you might need the [`MANIFEST.in`](MANIFEST.in) file, since it specifies (among other things), which files to include and which to exclude from your binaries.

### Setup.cfg

The [`setup.cfg`](setup.cfg) file defines the rules for flake8 and pycodestyle syntax checking, versioneer, coverage, building wheel and the metadata which shall be included.

### Gitignore

The `.gitignore` file is a real life saver. It prevents files and directories that match certain patterns from being added to your git repository, when you push new stuff to it. You may append more specific patterns [here](.gitignore#L149).

### CI/CD

This repository uses [`GitHub Actions`](https://github.com/features/actions) and/or [`CircleCI`](https://circleci.com/) as CI/CD.

Choose which one you want to use. Maybe both?
Modify the .yaml files to your will, erase them or add new ones.

#### YAML-Specifications

The files inside the folders [`.github/workflows`](.github/workflows) and  [`.circleci`](.circleci) specify the CI/CD behavior. Currently, are run:

* [`Style Check`](.github/workflows/autopep8.yml) according to PEP8 with automatic fixing and committing.
* unittests for Python 3.6, 3.7 and 3.8 on [`Linux`](.github/workflows/notebooktests_linux.yml), [`Windows`](.github/workflows/notebooktests_windows.yml) and [`Mac`](.github/workflows/notebooktests_mac.yml).
* tests of the notebooks for Python 3.6, 3.7 and 3.8 on [`Linux`](.github/workflows/unittests_linux.yml), [`Windows`](.github/workflows/unittests_windows.yml) and [`Mac`](.github/workflows/unittests_mac.yml).
* [`Build Docs`](.github/workflows/build_docs.yml) to generate the html versions of the `.rst` files in the [`source`](docs/source) folder
* [`PyPI Release`](.github/workflows/pypi_release.yml) to automatically publish the package on pyPI.
* [`Issue and pr Labeling`](.github/workflows/label.yml) to automatically label issues and pull requests. You can define your custom [`here`](.github/labeler.yml).
* [`Team Labeling`](.github/workflows/team_labeler.yml) to automatically pull requests based on the team in which the user is. The teams can be defined [`here`](.github/teams.yml).
* [`Stale Checker`](.github/workflows/stale.yml) for issues and pull requests.
* [`Greetings`](.github/workflows/greetings.yml) for first issues and pr and automatic labeling are also implemented.
* [`Rebase`](.github/workflows/rebase.yml) to autom. rebase the branch of a pull request when commenting `/rebase`.
* [`Install package`](.github/workflows/rebase.yml) to autom. check if the created package can be build.
* #TODO add code-formatting.yml
* #TODO add ci-testing.yml
* #TODO add docker-builds.yml

You may add additional GitHub actions. Check out the [marketplace](https://github.com/marketplace?type=actions) for actions created by the community.

**For the moment several of these workflows are disabled. Remove the line `if: false` or replace the condition if you want to use these workflows.**

### Docker

If you want to use GitHub and CircleCi workflows for Docker you need to do the following [here](.github\workflows\docker-builds.yml) and [here](.circleci\config.yml):

* Replace `DOCKER_AUTHOR_NAME` with your name on Docker
* Replace `DOCKER_REPONAME` with the name of your package on Docker

Your should also modify the `Dockerfiles` in the subdirs of the [dockers](dockers) folder to create your personal Docker workflows.

### Badges and logo

You can adapt the badges to your will. You can maintain the above, the links to GitHub will automatically modified when running `scripts/configure.py`. See [here](#scripts).

To modify the logo simply place a new one in formats `.svg` and `.png` [here](docs/source/_images/logos).

### Documentation

The documentation is build using Sphinx. The resulting html files are in the [`build`](docs/build) folder.

You should modify the [`conf.py`](docs/source/conf.py) to fit your needs.
Especially it's part on extracting lines from the README has to be adapted in order to use the getting_started.rst.

Next rewrite the .rst file in the [`source`](docs/source) folder.

If you need some guidelines on how to use the .rst files, run the [`build_docs`](docs/build_docs.sh) script and read the built html files.
