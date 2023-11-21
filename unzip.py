import os
import zipfile

def unzip_files(input_directory, output_directory):
    # Iterate through all the files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a .zip file
        if filename.endswith('.zip') and filename[:2] in ['AA']:
            # Create the full path to the zip file
            file_path = os.path.join(input_directory, filename)

            # Open the zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents into the output directory
                zip_ref.extractall(output_directory)
                print(f"Unzipped {filename} to {output_directory}")

input_directory = r'zips'  # Replace with your input directory path
output_directory = r'unzippe'  # Replace with your output directory path

# Ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Unzip all files in the specified directory
unzip_files(input_directory, output_directory)
