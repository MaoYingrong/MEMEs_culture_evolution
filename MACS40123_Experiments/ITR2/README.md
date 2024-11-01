# ITR2
## Scripts

- **[nn_clustering.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/MACS40123_Experiments/ITR2/nn_clustering.py)**:
  - This file uses neural network-based feature extraction, calculated pairwise similarity, and clustered meme images.  

- **[distribution.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/MACS40123_Experiments/ITR2/distribution.py)**:
  - A script used to draw the graph of the distribution of cluster size. 

- **[extract_features_p.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/MACS40123_Experiments/ITR2/extract_features_p.py)**:
  - This script extracts image features for each meme. For each image, the feature is a 2048-dimensional vector.

- **[extract_features_p.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/MACS40123_Experiments/ITR2/extract_features_p.sbatch)**:
  - This Slurm batch script is used to submit extract_features_p.py.

- **[hds_trial_p.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/MACS40123_Experiments/ITR2/hds_trial_p.py)**:
  - This script applies hierarchical density-based clustering directly on all image features. 
 
- **[hds_trial_p.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/MACS40123_Experiments/ITR2/hds_trial_p.sbatch)**:
  - This sbatch file is used to run the hds_trial_p.py.
