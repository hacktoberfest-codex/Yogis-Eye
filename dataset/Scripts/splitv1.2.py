import os
import shutil
import random

# Set the source directory containing your plant image folders
source_dir = r'X:\REpoS\dataset\Aur Vedic Herb'

# Set the destination directory for the training data
train_dest_dir = r'X:\REpoS\dataset\Aur Vedic Herb\Train'

# Set the destination directory for the testing data
test_dest_dir = r'X:\REpoS\dataset\Aur Vedic Herb\Test'

# Set the percentage of images to be used for testing (e.g., 12%)
test_percentage = 10

# Create the testing directory if it doesn't exist
if not os.path.exists(test_dest_dir):
    os.makedirs(test_dest_dir)

# Iterate through each plant folder in the source directory
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        images = os.listdir(folder_path)
        num_images = len(images)
        
        # Calculate the number of images to move to the testing set
        num_test_images = int(num_images * (test_percentage / 100))
        
        # Randomly select images for the testing set
        test_images = random.sample(images, num_test_images)
        
        # Move testing images to the test destination directory
        for image_name in test_images:
            source_image_path = os.path.join(folder_path, image_name)
            test_image_dest = os.path.join(test_dest_dir, image_name)
            shutil.move(source_image_path, test_image_dest)
        
        # Move the remaining images to the training destination directory
        for image_name in os.listdir(folder_path):
            source_image_path = os.path.join(folder_path, image_name)
            train_image_dest = os.path.join(train_dest_dir, folder_name, image_name)
            
            # Create the subfolder in the training directory if it doesn't exist
            if not os.path.exists(os.path.join(train_dest_dir, folder_name)):
                os.makedirs(os.path.join(train_dest_dir, folder_name))
            
            shutil.move(source_image_path, train_image_dest)

print("Data splitting completed.")

