# Experiments

This directory contains the scripts and output files related to meme clustering and image similarity detection experiments. The main objective of these experiments is to cluster meme images based on visual similarities using various hashing methods and clustering techniques. Below is a description of each file:

## Scripts

- **[hashing_clustering.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/hashing_clustering.py)**:
  - This Python script applies perceptual hashing (pHash) and DBSCAN, to cluster meme images. Parameters such as `hash_size` and `eps` (epsilon) are adjustable to optimize the clustering performance.  

- **[clustering.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/clustering.sbatch)**:
  - A batch script for submitting the clustering job to the HPC system, allowing for the efficient clustering of large datasets by utilizing parallel processing.

- **[check_fp.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/check_fp.py)**:
  - This script is used to check false positives within clusters. It helps identify and flag images that have been incorrectly clustered together by comparing them based on their visual features.

- **[check_fp.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/check_fp.sbatch)**:
  - This Slurm batch script is used to submit the `check_fp.py` script to the high-performance computing (HPC) system, automating the false positive checking process for large datasets.

- **[image_lsh.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/image_lsh.py)**:
  - This script tests the application of Locality-Sensitive Hashing (LSH) on the meme dataset. It assesses the feasibility of LSH for clustering images but has shown limitations due to the image characteristics, such as noise and textual overlays.

## Output Files

- **[hashing_24271809_0.out](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/hashing_24271809_0.out)**:
  - These are output logs from the hashing and clustering experiments. They contain information such as execution time, the number of clusters formed, and the number of images stored in clusters. 

- **[output_10000_hs08_eps10.json](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/output_10000_hs08_eps10.json)**:
  - This file contains the results from running the clustering algorithm on a sample of 10,000 meme images with parameters `hash_size=8` and `eps=0.10`. It stores details about the clusters generated during the experiment.

- **[check_fp_24280231_0.out](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/check_fp_24280231_0.out)**:
  - These are output logs from the checking False Positives experiments. They contain information such as similarity level in each cluster, and weighted mean value.

- **[similarity_ratios_hs01_eps10.csv](https://github.com/MaoYingrong/MEMEs_culture_evolution/edit/main/Experiments/similarity_ratios_hs01_eps10.csv)**:
  - A CSV file that summarizes the similarity ratios across different clusters using the parameters `hash_size=8` and `eps=0.10`. It likely contains metrics that evaluate the effectiveness of the clustering process, such as the percentage of images correctly grouped together.

## Notes

- All code for these experiments is available in this repository. To reproduce the results, please run the appropriate Python scripts (`hashing_clustering.py`, `check_fp.py`) using the provided SBATCH scripts for parallel processing on an HPC system.
- Further details about the experiment methodology, including parameter tuning and performance evaluation, can be found in the LaTeX project reports.

---

For more information on the experiment results and methodology, refer to the full project report and code documentation in this repository: [MEMEs_culture_evolution](https://github.com/MaoYingrong/MEMEs_culture_evolution).
