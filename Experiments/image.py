from PIL import Image, ImageFilter
import imagehash
from datasketch import MinHash, MinHashLSH
import numpy as np
import scipy.fftpack
import csv
from datetime import datetime

file_path = "sample_25_names.csv"
with open(file_path, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    image_paths = [row[0] for row in reader]


# Function to convert perceptual hash into a MinHash object
def hash_to_minhash(phash_str):
    m = MinHash(num_perm=128)
    for char in phash_str:
        m.update(char.encode('utf8'))
    return m


def custom_roi_hash(image_path, crop_box):
    """
    Resize, Create a perceptual hash of a custom region of interest, and Adjust the hash size.
    
    :param image_path: Path to the image file.
    :param crop_box: A tuple (left, upper, right, lower) defining the cropping box.
    :return: Hash of the cropped image.
    """
    # Open and crop the image
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img_cropped = img.crop(crop_box)
    image = img_cropped.convert("L").filter(ImageFilter.GaussianBlur(radius=4))
    pixels = np.asarray(image)
    dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels, axis=0), axis=1)
    dctlowfreq = dct[:8, :8]

    # med = np.median(dctlowfreq)
    med = np.mean(dct)
    diff = dctlowfreq > med
    return imagehash.ImageHash(diff.astype(np.bool_))

# Define the cropping box (left, upper, right, lower)
crop_box = (50, 100, 200, 200)  # Example values


def get_image_hash(image_path):
    img = Image.open(image_path)
    hash = imagehash.phash(img, hash_size=16)
    return hash 


# Initialize LSH
lsh = MinHashLSH(threshold=0.95, num_perm=128)

# Dictionary to store image names and their hashes for later use
image_hashes = {}

# Iterate over the list of images, compute perceptual hashes, and insert them into the LSH index
for image_path in image_paths:

    # phash = custom_roi_hash(image_path, crop_box)
    phash = get_image_hash(image_path)
    
    # Convert perceptual hash to MinHash
    m = hash_to_minhash(str(phash))
    
    # Store hash to compare later
    image_hashes[image_path] = phash
    
    # Insert into LSH index
    lsh.insert(image_path, m)

# Keep track of images we've already clustered
visited_images = set()

# List to store the clusters of similar images
clusters = []

# Function to cluster images that are similar
def find_similar_images(image_path):
    m = hash_to_minhash(str(image_hashes[image_path]))
    result = lsh.query(m)
    # Return only the last digits of the image names
    return [img_path for img_path in result]

# Cluster the images by similarity
for image_path in image_paths:
    if image_path not in visited_images:
        # Find all similar images
        similar_images = find_similar_images(image_path)
        
        # Add the cluster (including single images)
        clusters.append(similar_images)
        
        # Mark all the images in this cluster as visited
        for img in similar_images:
            visited_images.add(img)

# Display clusters of similar images
for cluster in clusters:
    print(f"Cluster of similar images: {cluster}")