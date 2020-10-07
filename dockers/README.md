# Builds

You can build it on your own, note it takes lots of time, be prepared.

```bash
git clone https://github.com/GITHUB_NAME/REPONAME.git
docker image build -t DOCKER_REPONAME:latest -f dockers/conda/Dockerfile .
```

or with specific arguments

```bash
git clone https://github.com/GITHUB_NAME/REPONAME.git
docker image build \
    -t DOCKER_REPONAME:py3.8 \
    -f dockers/conda/Dockerfile \
    --build-arg PYTHON_VERSION=3.8 \
    .
```

To run your docker use

```bash
docker image list
docker run --rm -it DOCKER_REPONAME:latest bash
```

and if you do not need it anymore, just clean it:

```bash
docker image list
docker image rm DOCKER_REPONAME:latest
```
