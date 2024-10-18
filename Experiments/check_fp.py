import torch
from torchvision import models, transforms
from PIL import Image
import torch.nn.functional as F
import json
import csv
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "--hashsize", type=int, default=8, help="Hash size for pHash computation. Default is 8.")
parser.add_argument("--eps", type=float, default=0.2, help="threshold for hashing. Default=0.2")
args = parser.parse_args()
print(f"hash_size: {args.hashsize:02d}; eps: {args.eps}")

open_file = f'output_10000_hs{args.hashsize:02d}_eps{int(100*args.eps):02d}.json'
output_file = f'similarity_ratios_hs{args.hashsize:02d}_eps{int(100*args.eps):02d}.csv'
print(open_file)
print(output_file)
# Load a pretrained ResNet model
# model = models.resnet50(pretrained=True)
# model = torch.nn.Sequential(*list(model.children())[:-1])  # Remove the classification layer
# model.eval()
model = torch.load('resnet50.pth')
model.eval()
print('ResNet50 loaded sucessfully')

# Preprocessing transforms
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_image(image_path):
    img = Image.open(image_path).convert('RGB')  # Convert to RGB before preprocessing
    img = preprocess(img).unsqueeze(0)  # Preprocess and add batch dimension
    return img

def cosine_similarity(tensor1, tensor2):
    tensor1 = tensor1.squeeze()  # Remove batch dimension
    tensor2 = tensor2.squeeze()  # Remove batch dimension
    similarity = F.cosine_similarity(tensor1, tensor2, dim=0)
    return similarity.item()  # Return the scalar value


def calculate_similarity_ratios(data):
    ratios = []

    mean_similarity = 0
    len_data = 0
    for cluster in data:
        image_paths = list(cluster.values())[0]  # Extract image paths from the cluster
        num_images = len(image_paths)

        # Load and extract features for all images in the cluster
        features = []
        for image_path in image_paths:
            img_tensor = load_image(image_path)
            with torch.no_grad():
                feature = model(img_tensor).squeeze()  # Extract features, removing batch dimension
            features.append(feature)

        # Calculate pairwise cosine similarities
        total_pairs = 0
        similar_pairs = 0
        threshold = 0.9  # Similarity threshold

        for i in range(num_images):
            for j in range(i + 1, num_images):
                similarity = cosine_similarity(features[i], features[j])
                total_pairs += 1
                if similarity > threshold:
                    similar_pairs += 1
        similarity_ratio = similar_pairs / total_pairs
        ratios.append((list(cluster.keys())[0], similarity_ratio))
        print(f"Cluster {list(cluster.keys())[0]}: Similarity Ratio = {similarity_ratio:.2f}")
        mean_similarity += similarity_ratio * len(image_paths)
        len_data += len(image_paths)
    
    print(f"Mean Similarity Ratio: {mean_similarity / len_data:.2f}")

    return ratios 


def save_to_csv(ratios, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cluster", "Similarity Ratio"])
        for indx, ratio in ratios:
            writer.writerow([f"Cluster_{indx}", ratio])


# Main processing
if __name__ == "__main__":
    
    start_time = time.time()
    # Load JSON data
    with open(open_file, "r") as f:
        data = json.load(f)

    # Calculate similarity ratios for each cluster
    similarity_ratios = calculate_similarity_ratios(data)

    # Save the results to a CSV file
    save_to_csv(similarity_ratios, output_file)

    print("Similarity ratios have been saved to similarity_ratios.csv.")
    print(f"Time used to run the program: {time.time() - start_time}")
