# Justfile

VENV := ".venv"
PYTHON_VER := "3.13"


# list all tasks
default:
  @just --list

# Install uv
install-uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up Python virtual environment
venv: install-uv
    #!/usr/bin/env sh
    if [ "$(uname)" = "Darwin" ] || [ "$(uname)" = "Linux" ]; then
        echo "Installing virtual env on Darwin or Linux..."
        uv venv {{ VENV }} --python {{ PYTHON_VER }}
        . {{ VENV }}/bin/activate
    else
        echo "Installing virtual env on Windows..."
        uv venv {{ VENV }} --python {{ PYTHON_VER }}
        . {{ VENV }}/Scripts/activate
    fi

# Build OpenUSD
build-openusd: venv
    . {{ VENV }}/bin/activate && \
    uv add pyside6 PyOpenGL && \
    git clone https://github.com/PixarAnimationStudios/OpenUSD.git && \
    python ./OpenUSD/build_scripts/build_usd.py ./
    rm -rf OpenUSD && \
    echo "export PYTHONPATH='$PWD/installation/lib/python'" >> ~/.zshrc && \
    echo "export PATH='$PWD/bin:\$PATH'" >> ~/.zshrc && \
    source ~/.zshrc

# Clean up
clean-up: build-openusd
    mkdir -p tutorials && \
    cp -rp ./share/usd/tutorials/* ./tutorials
    rm -rf share &&\
    rm -rf build && \
    rm -rf cmake && \
    rm -rf include && \
    rm -rf libraries && \
    rm -rf src && \
    rm -r CHANGELOG.md && \
    rm -r pxrConfig.cmake && \
    rm -r THIRD-PARTY.md

# Set up OpenUSD
setup-openusd: clean-up
    . {{ VENV }}/bin/activate && \
    mv ./lib/python ./lib/openusd && \
    cd ./lib/openusd && \
    uv init && \
    cd .. && \
    cd .. && \
    uv add ./lib/openusd --editable
