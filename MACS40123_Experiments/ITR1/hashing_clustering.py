import os
from PIL import Image, UnidentifiedImageError
import imagehash
import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import hamming
from datetime import datetime
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument( "--hashsize", type=int, default=8, help="Hash size for pHash computation. Default is 8.")
parser.add_argument("--eps", type=float, default=0.2, help="threshold for hashing. Default=0.2")
args = parser.parse_args()
OUTPUT_FILE = f'output_10000_hs{args.hashsize:02d}_eps{int(100*args.eps):02d}.json'
print(f"hash_size: {args.hashsize:02d}; eps: {args.eps}")

# Step 1: pHash Extraction Function
def compute_phash(image_path):
    """
    Compute the perceptual hash (pHash) for a given image.
    """
    try:
        image = Image.open(image_path)
    except UnidentifiedImageError:
        print(f"Error: {image_path}")
        return None
    return imagehash.phash(image, hash_size=args.hashsize)


# Step 2: Hamming Distance Function
def hamming_distance(hash1, hash2):
    """
    Compute the Hamming distance between two hashes.
    """
    return hamming(np.array(list(hash1.hash.flatten())), np.array(list(hash2.hash.flatten())))


# Step 3: Cluster the Images
def cluster_images(image_paths, eps=args.eps, min_samples=1):
    """
    Cluster images based on their pHash values using DBSCAN.
    """
    # Step 3.1: Extract pHashes for each image
    phashes = []
    valid_image_paths = []
    for image_path in image_paths:
        phash = compute_phash(image_path)
        if phash is not None:
            phashes.append(phash)
            valid_image_paths.append(image_path)

    # Step 3.2: Create a pairwise distance matrix using Hamming distance
    num_images = len(phashes)
    distance_matrix = np.zeros((num_images, num_images))

    for i in range(num_images):
        for j in range(i + 1, num_images):
            distance_matrix[i, j] = hamming_distance(phashes[i], phashes[j])
            distance_matrix[j, i] = distance_matrix[i, j]  # Symmetric matrix

    # Step 3.3: Perform DBSCAN clustering
    dbscan = DBSCAN(metric="precomputed", eps=eps, min_samples=min_samples, n_jobs=-1)
    labels = dbscan.fit_predict(distance_matrix)

    return valid_image_paths, labels


def print_clusters(image_paths, labels):
    """
    Print the clusters of images.
    """
    clusters = {}
    cluster_stored = []
    for image_path, label in zip(image_paths, labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(image_path)

    n_clusters_2 = 0
    n_images = 0
    n_max = 0

    for cluster_id, image_paths in clusters.items():
        if len(image_paths) > 1:
            n_clusters_2 += 1
            cluster_stored.append({str(cluster_id): image_paths})
            n_images += len(image_paths)
            if len(image_paths) > n_max:
                n_max = len(image_paths)

    with open(OUTPUT_FILE, 'w') as json_file:
        json.dump(cluster_stored, json_file, indent=4)
                
    print(f"Number of clusters: {len(clusters)}")
    print(f"Number of clusters with more than 1 image: {n_clusters_2}")
    print(f"Number of images: {n_images}")
    print(f"Max number of images in a cluster: {n_max}")


def main():
    # Path to the folder containing images
    start_time = datetime.now()
    image_folder = "/scratch/midway3/yingrong/sample_img_10000"
    image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith('.jpg')]

    valid_paths, labels = cluster_images(image_paths)
    print_clusters(valid_paths, labels)

    print(datetime.now() - start_time)


if __name__ == "__main__":
    main()
