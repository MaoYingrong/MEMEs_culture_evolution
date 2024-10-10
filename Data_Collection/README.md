1. [images_scraping.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/images_scraping.py): used to scrape all available image data.
2. [images_names.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/images_names.py): store all names of images downloaded (image names are posts ID)
3. [change_structure.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/change_structure.py): used to make the original submission file (list of dictionaries) become a dictionary of dictionaries, in which keys are the posts ID.
4. [filter_post.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/filter_post.py): based on the image names, filter all the posts with images downloaded.
5. [filter_comments.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/filter_comments.py): based on the filtered posts, get all comments under those posts.
6. [sbatch_file.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/sbatch_file.sbatch): use to execute the programs running in Midway HPC
