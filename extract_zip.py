import zipfile
import os
from tqdm import tqdm

def extract_zip(zip_file, extract_dir):
    # Create extraction directory if it doesn't exist
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    # Open the zip file for reading
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Get list of files in the zip file
        files = zip_ref.namelist()

        # Initialize tqdm progress bar
        progress_bar = tqdm(total=len(files), desc="Extracting")

        # Extract each file in the zip file
        for file in files:
            zip_ref.extract(file, extract_dir)
            progress_bar.update(1)
            progress_bar.set_description("Extracting: {}".format(file))
        
        # Close progress bar
        progress_bar.close()

    print("Extraction complete.")

# Example usage
zip_file = "D:\document from C storage\document_file_per_13032024\compress_per_13032024.zip"
extract_dir = "D:\document from C storage\document_file_per_13032024\compress_per_13032024"
extract_zip(zip_file, extract_dir)
