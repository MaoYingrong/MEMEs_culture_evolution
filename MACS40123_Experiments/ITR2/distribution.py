import json
import matplotlib.pyplot as plt

# Load the JSON file
json_file = "/scratch/midway3/yingrong/trial/hdbscan_16.json"
with open(json_file, "r") as f:
    data = json.load(f)

# Extract the lengths of the list values
lengths = [len(value) for item in data for value in item.values()]

print(f"The maximum length is {max(lengths)}")
print(f"The number of clusters is {len(lengths)}")
print(f"The total number of images is {sum(lengths)}")

new_lst = []
num_clusters_larger_than_10 = 0
num_2cluster = 0
for i, length in enumerate(lengths):
    if length > 10:
        num_clusters_larger_than_10 += 1
        print(f"the length of the cluster is {length}")
    elif length == 2:
        num_2cluster += 1
    
    if length > 2:
        new_lst.append(length)

print(f"\nNumber of clusters with length greater than 10: {num_clusters_larger_than_10}")
print(f"\nNumber of clusters with length equal to 2: {num_2cluster}")


plt.figure(figsize=(10, 6))
plt.hist(lengths, bins=range(0, 51), edgecolor='black', alpha=0.7)  # Bins range from 0 to 50 with width of 1
plt.title("Distribution of Cluster Size", fontsize=20)
plt.xlabel("Cluster size", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.xlim(0, 50)  # Set x-axis range from 0 to 50
plt.xticks(fontsize=20)  # Set font size for x-axis ticks
plt.yticks(fontsize=20)  # Set font size for y-axis ticks
plt.grid(True)
plt.show()

# Save the histogram as an image file
plt.savefig("distribution_50000_pca500.png")  # You can change the file name and format

# Close the plot to avoid displaying it
plt.close()