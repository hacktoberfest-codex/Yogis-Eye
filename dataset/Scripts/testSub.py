import os
import csv

# Specify the folder containing the pictures
folder_path = "X:\\REpoS\\Yogi Eye\\data\\Ayurved.v2\\test"

# Create a list of file names in the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Create a CSV file and write the data
csv_file = "image_species.csv"
def write_file(witer, path):
    
    for file in path:
        witer.writerow(file)

with open(csv_file, mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow("file")  # Write header row

    write_file(writer,file_names) # Write file name and species for each picture

print(f"CSV file '{csv_file}' created with image names and species 'neem'.")





