from PIL import Image, UnidentifiedImageError
import numpy as np
from sklearn.cluster import DBSCAN
from datetime import datetime
import json
import csv
import itertools
import torch
from torchvision import models, transforms
import torch.nn.functional as F
import time
from collections import defaultdict


print("The data is 800,000-810,000; eps=0.05, and using nn")
# Constants
OUTPUT_FILE = "nn1000new_clustering.json"
SIMILARITY_THRESHOLD = 0.9
MODEL_PATH = 'resnet50.pth'

time_0 = datetime.now()
# Load the model
model = torch.load(MODEL_PATH)
model.eval()
print('ResNet50 loaded successfully')

# Preprocessing transforms
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
print(f"The time used to load the pre-trained model is {datetime.now() - time_0}")

def load_image(image_path):
    """Load and preprocess an image."""
    try:
        img = Image.open(image_path).convert('RGB')  # Convert to RGB before preprocessing
        img_tensor = preprocess(img).unsqueeze(0)  # Preprocess and add batch dimension
        return img_tensor
    except UnidentifiedImageError:
        print(f"Error loading image: {image_path}")
        return None


def extract_features(image_path):
    """Extract neural network features for an image."""
    img_tensor = load_image(image_path)
    if img_tensor is None:
        return None
    with torch.no_grad():
        feature = model(img_tensor).squeeze()  # Extract features from the neural network
    return feature.numpy() if feature is not None else None



def cluster_images(image_paths, eps=0.05, min_samples=1):
    """
    Cluster images based on their neural network features using DBSCAN.
    """
    features = []
    valid_image_paths = []

    time_3 = datetime.now()
    for image_path in image_paths:
        feature = extract_features(image_path)
        if feature is not None:
            features.append(feature)
            valid_image_paths.append(image_path)
    print(f"The time used to read data and extract features is {datetime.now() - time_3}")
    
    num_images = len(valid_image_paths)
    distance_matrix = np.zeros((num_images, num_images))

    time_1 = datetime.now()
    for i in range(num_images):
        for j in range(i + 1, num_images):
            similarity = F.cosine_similarity(torch.tensor(features[i]), torch.tensor(features[j]), dim=0).item()
            distance_matrix[i, j] = max(0, 1 - similarity)  # Convert similarity to distance
            distance_matrix[j, i] = max(0, 1 - similarity)  # Symmetric distance matrix
    print(f"The time used to do 2 for loops and similarity calculation is {datetime.now() - time_1}")

    time_2 = datetime.now()
    # Perform clustering
    dbscan = DBSCAN(metric="precomputed", eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(distance_matrix)
    print(f"The time used to do DBSCAN is {datetime.now() - time_2}")

    return valid_image_paths, labels


def print_clusters(image_paths, labels):
    """
    Print the clusters of images and save the results to a JSON file.
    """
    clusters = defaultdict(list)
    cluster_stored = []

    for image_path, label in zip(image_paths, labels):
        clusters[label].append(image_path)

    n_clusters_2 = 0
    n_images = 0
    n_max = 0

    for cluster_id, image_paths in clusters.items():
        if len(image_paths) > 1:
            n_clusters_2 += 1
            cluster_stored.append({str(cluster_id): image_paths})
            n_images += len(image_paths)
            n_max = max(n_max, len(image_paths))

    with open(OUTPUT_FILE, 'w') as json_file:
        json.dump(cluster_stored, json_file, indent=4)

    print(f"Number of clusters: {len(clusters)}")
    print(f"Number of clusters with more than 1 image: {n_clusters_2}")
    print(f"Number of images: {n_images}")
    print(f"Max number of images in a cluster: {n_max}")


def main():
    # Path to the folder containing images
    start_time = datetime.now()
    csv_file = "/scratch/midway3/yingrong/all_image_names.csv"
    image_paths = []
    with open(csv_file, "r") as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip the header
        for row in itertools.islice(reader, 800000, 810000):
            subfolder, full_path = row
            image_paths.append(full_path)     

    valid_paths, labels = cluster_images(image_paths)
    print_clusters(valid_paths, labels)

    print(f"Total time taken: {datetime.now() - start_time}")

if __name__ == "__main__":
    main()