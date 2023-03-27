#!/bin/bash

# conda 
source  ~/.bashrc
conda activate compressai

# cuda 11.3
# ml purge
# ml load cuda/11.3

# code
cd ~/compressai/codes
python -u examples/train.py -exp MS_LSQ_8bit_q5 -m ms-relu -q 5 --lambda 0.0250 -b ../experiments/MS_q5/checkpoints/checkpoint_best_loss.pth.tar --config configs/ms_8bit_lsq.yaml -d ~/flicker
# -b ../experiments/MS_q1/checkpoints/checkpoint_best_loss.pth.tar
# --config configs/gmm_8bit_lsq.yaml
# exp, model, quality + lambda, config(model_bit_func.yaml), pretrain/checkpoint, dataset
# -c ~/compressai/experiments/{}/checkpoints/checkpoint_best_loss.pth.tar