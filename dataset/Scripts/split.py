import os
import random
import shutil

# Define the root directory where your 100 plant type folders are located.
root_directory = 'X:\REpoS\Yogi Eye\data\indo_herb'

# Define the directory where you want to create the train and test folders.
output_directory = 'X:\REpoS\Yogi Eye\data\herb_indo'

# Define the train-test split ratio (e.g., 80% training, 20% testing).
split_ratio = 0.8

# Loop through each plant type folder.
for plant_type in os.listdir(root_directory):
    plant_type_path = os.path.join(root_directory, plant_type)
    
    # Create train and test directories for each plant type.
    train_dir = os.path.join(output_directory, 'train', plant_type)
    test_dir = os.path.join(output_directory, 'test', plant_type)
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    
    # Get a list of all image files in the current plant type folder.
    image_files = [f for f in os.listdir(plant_type_path) if f.endswith('.jpg')]

    # Calculate the number of images for training and testing.
    num_images = len(image_files)
    num_train = int(num_images * split_ratio)
    
    # Shuffle the list of image files randomly.
    random.shuffle(image_files)
    
    # Copy the first 'num_train' images to the train directory.
    for image_file in image_files[:num_train]:
        src_path = os.path.join(plant_type_path, image_file)
        dest_path = os.path.join(train_dir, image_file)
        shutil.copy(src_path, dest_path)
    
    # Copy the remaining images to the test directory.
    for image_file in image_files[num_train:]:
        src_path = os.path.join(plant_type_path, image_file)
        dest_path = os.path.join(test_dir, image_file)
        shutil.copy(src_path, dest_path)
    
    print(f"Split {plant_type} images into train and test sets.")

print("Data splitting completed.")
