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
    uv sync && \
    git clone https://github.com/PixarAnimationStudios/OpenUSD.git && \
    python ./OpenUSD/build_scripts/build_usd.py ./
    rm -rf OpenUSD

# Add envrionment variables
add-env-vars:
    echo "export PYTHONPATH=\"$PWD/installation/lib/openusd\"" >> ~/.zshrc && \
    echo "export PATH=\"$PWD/bin:\$PATH\"" >> ~/.zshrc && \
    source ~/.zshrc

# Clean up
clean-up:
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
    rm -r THIRD-PARTY.md && \
    rm -r README.md && \
    cp ./readme/README.md ./README.md

# Set up OpenUSD
setup-openusd:
    . {{ VENV }}/bin/activate && \
    mv ./lib/python ./lib/openusd && \
    cd ./lib/openusd && \
    uv init && \
    cd .. && \
    cd .. && \
    uv add ./lib/openusd --editable

# Test with hello world
hello-world:
    . {{ VENV }}/bin/activate && \
    cd ./tutorials/helloWorld && \
    python ./helloWorld.py && \
    usdview HelloWorld.usda

##################################################
# Nvidia Tutorials
##################################################

# Stage/example_1
stage_example_1:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Stage && \
    python ./example_1.py && \
    usdview _assets/first_stage.usda

# Prims/example_1
prims_example_1:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Prims && \
    python ./example_1.py && \
    usdview _assets/prims.usda

# Prims/example_2
prims_example_2:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Prims && \
    python ./example_2.py && \
    usdview _assets/sphere_prim.usda

# Prims/example_3
prims_example_3:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Prims && \
    python ./example_3.py && \
    usdview _assets/prim_hierarchy.usda


# Properties/Attributes/example_1
properties_attributes_example_1:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Properties/Attributes && \
    python ./example_1.py && \
    usdview _assets/attributes_ex1.usda

# Properties/Attributes/example_2
properties_attributes_example_2:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Properties/Attributes && \
    python ./example_2.py && \
    usdview _assets/attributes_ex2.usda

# Properties/Attributes/example_3
properties_attributes_example_3:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/Properties/Attributes && \
    python ./example_3.py && \
    usdview _assets/attributes_ex3.usda

# TimeCodes-and-TimeSamples/timecode_sample
timecodes_and_timesamples_timecode_sample:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/TimeCodes-and-TimeSamples && \
    python ./timecode_sample.py && \
    usdview _assets/timecode_sample.usda

# TimeCodes-and-TimeSamples/example_1
timecodes_and_timesamples_example_1:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/TimeCodes-and-TimeSamples && \
    python ./example_1.py && \
    usdview _assets/timecode_ex1.usda

# TimeCodes-and-TimeSamples/example_2
timecodes_and_timesamples_example_2a:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/TimeCodes-and-TimeSamples && \
    python ./example_2a.py && \
    usdview _assets/timecode_ex2a.usda

# TimeCodes-and-TimeSamples/example_2b
timecodes_and_timesamples_example_2b:
    . {{ VENV }}/bin/activate && \
    cd ./nvidia-tutorials/TimeCodes-and-TimeSamples && \
    python ./example_2b.py && \
    usdview _assets/timecode_ex2b.usda

