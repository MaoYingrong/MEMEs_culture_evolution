#!/bin/bash

#SBATCH --job-name=hashing
#SBATCH --output=logs/hashing_%j_%t.out  # Output file will have job ID and task ID
#SBATCH --error=logs/hashing_%j_%t.err   # Error file will have job ID and task ID
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=2G
#SBATCH --partition=caslake
#SBATCH --account=macs40123
#SBATCH --array=0-19             # 20 tasks (4 hash sizes * 5 eps values)


# List of eps and hashsize values
EPS_LIST=(0.10 0.15 0.20 0.25 0.30)
HASHSIZE_LIST=(8 12 16 20)

# Calculate eps and hashsize for this job
HASHSIZE_IDX=$((SLURM_ARRAY_TASK_ID / 5))
EPS_IDX=$((SLURM_ARRAY_TASK_ID % 5))

EPS=${EPS_LIST[$EPS_IDX]}
HASHSIZE=${HASHSIZE_LIST[$HASHSIZE_IDX]}

module load python/anaconda-2022.05 

python hashing_clustering.py --hashsize $HASHSIZE --eps $EPS
