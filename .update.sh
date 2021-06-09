#!/bin/bash

version=$1

git commit -am "release v$version"
git tag $version -m "v$version"
git push --tags origin main

# build package
rm -rf ./dist/*
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel

# push to pypi
# twine upload dist/*

# to update docs
# cd to root dir
# mkdocs gh-deploy
