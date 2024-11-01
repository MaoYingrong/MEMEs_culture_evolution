# ITR2
## Scripts

- **[nn_clustering.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/hashing_clustering.py)**:
  - This Python script applies perceptual hashing (pHash) and DBSCAN, to cluster meme images. Parameters such as `hash_size` and `eps` (epsilon) are adjustable to optimize the clustering performance.  

- **[distribution.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/clustering.sbatch)**:
  - A batch script for submitting the clustering job to the HPC system, allowing for the efficient clustering of large datasets by utilizing parallel processing.

- **[extract_features_p.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/check_fp.py)**:
  - This script is used to check false positives within clusters. It helps identify and flag images that have been incorrectly clustered together by comparing them based on their visual features.

- **[extract_features_p.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/check_fp.sbatch)**:
  - This Slurm batch script is used to submit the `check_fp.py` script to the high-performance computing (HPC) system, automating the false positive checking process for large datasets.

- **[hds_tril_p.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/image_lsh.py)**:
  - This script tests the application of Locality-Sensitive Hashing (LSH) on the meme dataset. It assesses the feasibility of LSH for clustering images but has shown limitations due to the image characteristics, such as noise and textual overlays.
 
- **[hds_tril_p.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/image_lsh.py)**:
  - This script tests the application of Locality-Sensitive Hashing (LSH) on the meme dataset. It assesses the feasibility of LSH for clustering images but has shown limitations due to the image characteristics, such as noise and textual overlays.
