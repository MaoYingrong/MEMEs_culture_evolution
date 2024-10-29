#!/bin/bash

#SBATCH --job-name=hashing

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --partition=caslake
#SBATCH --account=macs40123
#SBATCH --array=0-19             # 20 tasks (4 hash sizes * 5 eps values)
#SBATCH --output=logs/check_fp_%A_%a.out  # Use %A for job ID and %a for array task ID
#SBATCH --error=logs/check_fp_%A_%a.err   # Use %A for job ID and %a for array task ID

# List of eps and hashsize values
EPS_LIST=(0.10 0.15 0.20 0.25 0.30)
HASHSIZE_LIST=(8 12 16 20)

# Calculate eps and hashsize for this job
HASHSIZE_IDX=$((SLURM_ARRAY_TASK_ID / 5))
EPS_IDX=$((SLURM_ARRAY_TASK_ID % 5))

EPS=${EPS_LIST[$EPS_IDX]}
HASHSIZE=${HASHSIZE_LIST[$HASHSIZE_IDX]}


module load python/anaconda-2022.05 

python check_fp.py --hashsize $HASHSIZE --eps $EPS
