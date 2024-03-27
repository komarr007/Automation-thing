import os
import hashlib
from tqdm import tqdm

def hash_file(file_path):
    """
    Calculate the hash value of a file.
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_directory(directory):
    """
    Recursively calculate hash values of all files and folders within a directory.
    """
    file_count = sum(len(files) for _, _, files in os.walk(directory))
    with tqdm(total=file_count, desc="Hashing files", unit="file") as pbar:
        hashes = {}
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, directory)
                hash_value = hash_file(file_path)
                hashes[relative_path] = hash_value
                pbar.update(1)
    return hashes

def compare_directories(directory_a, directory_b):
    """
    Compare the hash values of files and folders in two directories.
    """
    differences_found = False
    hashes_a = hash_directory(directory_a)
    hashes_b = hash_directory(directory_b)

    common_files = set(hashes_a.keys()) & set(hashes_b.keys())

    for file in common_files:
        if hashes_a[file] != hashes_b[file]:
            print(f"File '{file}' differs in content between directories.")
            differences_found = True

    unique_to_a = set(hashes_a.keys()) - set(hashes_b.keys())
    unique_to_b = set(hashes_b.keys()) - set(hashes_a.keys())

    if unique_to_a:
        print("Files unique to directory A:")
        for file in unique_to_a:
            print(file)
            differences_found = True

    if unique_to_b:
        print("Files unique to directory B:")
        for file in unique_to_b:
            print(file)
            differences_found = True

    if not differences_found:
        print("No differences found between directories.")

if __name__ == "__main__":
    directory_a = input("Enter path to directory A: ")
    directory_b = input("Enter path to directory B: ")

    if not os.path.isdir(directory_a) or not os.path.isdir(directory_b):
        print("Invalid directory path.")
    else:
        compare_directories(directory_a, directory_b)
