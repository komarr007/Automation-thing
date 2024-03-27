import os
import zipfile
from tqdm import tqdm

def compress_files(src_dir, dest_dir, zip_name, verbose=True):
    # Ensure source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    
    # Ensure destination directory exists, if not, create it
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Create full path for the ZIP file
    zip_path = os.path.join(dest_dir, zip_name)
    
    # Get the total number of files and directories to compress
    total_files = sum(len(files) for _, _, files in os.walk(src_dir))
    
    # Initialize a ZipFile object for writing
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        # Create a tqdm progress bar
        progress_bar = tqdm(desc="Compressing files", total=total_files, position=0, leave=False, disable=not verbose)
        
        # Walk through the directory tree
        for foldername, subfolders, filenames in os.walk(src_dir):
            # Add each file to the ZIP
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                rel_path = os.path.relpath(file_path, src_dir)
                zipf.write(file_path, rel_path)
                # Update the progress bar description with the current file being processed
                progress_bar.set_postfix(File=filename)
                progress_bar.update(1)
        
        # Close the progress bar
        progress_bar.close()

    print(f"Compression complete. Archive saved as '{zip_path}'.")

if __name__ == "__main__":
    # Set source and destination directories
    src_directory = input("Enter the source directory: ").strip()
    dest_directory = input("Enter the destination directory: ").strip()
    
    # Set the name for the ZIP file
    zip_name = input("Enter the name for the ZIP file: ").strip() + ".zip"
    
    # Compress files with verbose mode
    compress_files(src_directory, dest_directory, zip_name)
