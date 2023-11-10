#!/bin/bash

# Update to the latest files
# conda_env_name="iitd_ocr_ulca_apis_deploy"

# Source conda initialization script
# if [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
#     source "$HOME/anaconda3/etc/profile.d/conda.sh"
# elif [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
#     source "$HOME/miniconda3/etc/profile.d/conda.sh"
# else
#     echo "Conda initialization script not found."
#     exit 1
# fi

# if conda env list | grep -q "$conda_env_name"; then
#     echo "Activating existing conda environment: $conda_env_name"
#     conda activate "$conda_env_name"
# else
#     echo "Creating and activating new conda environment: $conda_env_name"
#     conda create -n "$conda_env_name" python=3.9
#     conda activate "$conda_env_name"
    
#     echo "Installing dependencies from requirements.txt using pip"
#     pip install -r requirements.txt
# fi

python3 update_files.py # Update the files


# Load the docker images

cd files

# cat foo.txt

# docker load -i text-recognizer-apis--parseq-based.tar

# docker run -it --network="host" -e PORT=8003 text-recognizer-apis--parseq-based
