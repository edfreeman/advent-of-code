# Find the Dockerfile at this URL
# https://github.com/devcontainers/images/tree/main/src/python
ARG VARIANT="3.11"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install Poetry and add exe to PATH
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH ${PATH}:/root/.local/bin
