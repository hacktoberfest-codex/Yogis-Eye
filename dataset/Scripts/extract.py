import os
import shutil

# Define the source directory containing subfolders with images
source_directory = 'data\indo_herb\test'

# Define the target directory where you want to store all images
target_directory = 'data\indo_herb\dumpy_test'

# Ensure the target directory exists; create it if it doesn't
os.makedirs(target_directory, exist_ok=True)

# Function to move image files from source to target directory
def move_images(source, target):
    for root, _, files in os.walk(source):
        for file in files:
            if file.endswith(('.jpg')):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target, file)
                shutil.move(source_path, target_path)

# Move all image files from subfolders to the target directory
move_images(source_directory, target_directory)

print(f"All image files moved to {target_directory}.")