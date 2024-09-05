# dados-qdd-fonte-95

[![Updated](https://github.com/splor-mg/dados-qdd-fonte-95/actions/workflows/all.yaml/badge.svg)](https://github.com/splor-mg/dados-qdd-fonte-95/actions/)

## Pré-requisitos

Esse projeto utiliza Docker para gerenciamento das dependências. Para fazer _build_  da imagem execute:

```bash
docker build --tag dados-qdd-fonte-95 .
```

## Uso

Para executar o container

```bash
docker run -it --rm --mount type=bind,source=$(PWD),target=/project dados-qdd-fonte-95 bash
```

Uma vez dentro do container execute os comandos do make

```bash
make all
```

_Gerado a partir de [cookiecutter-datapackage@ea4bda2](https://github.com/splor-mg/cookiecutter-datapackage/commit/ea4bda27d7c478f451df33f5f08b97a7aa159153)_
