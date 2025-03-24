#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Clone the repository
git clone https://github.com/chauthehan/ai-toolkit
cd ai-toolkit

# Initialize and update submodules
git submodule update --init --recursive

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install PyTorch with CUDA 12.4
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu124

# Install other dependencies
pip install -r requirements.txt

# Run the training script
python run.py config/train_lora_flux_24gb.yaml