ITR4

- extract_text.py and extract_text.sbatch files are used to extract text from images with OCR packages.  

- encoding.py and encoding.sbatch use a pre-trained model to embed combined text (text extracted from images, title, and comments) to vectors.

- diversity_trial.ipynb shows the exploration of the trend of different types of content diversity, such as the distance of all pairs within one month, the distance of all pairs within three month, and the distance between current instances with all historical instances.

- relationship.ipynb shows the process of correlation analysis and the construction of different linear regression models.

- arimax.ipynb shows the experiments on ARIMAX models. 
