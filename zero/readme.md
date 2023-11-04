# Setup python environment on docker

## Setup conda basic

```bash
docker build -t conda-base -f Dockerfile.basic .
```

## Setup conda using environment.yaml

```bash
docker build -t conda-env -f Dockerfile.env .
```

## Run docker container

```bash
# for conda basic
docker run --rm -it  conda-base
# for conda using environment.yaml
docker run --rm -it  conda-env
```

## Generate environment.yaml

```
conda env export --no-builds > environment.yaml
```
