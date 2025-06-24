import os
import hashlib
from collections import defaultdict

def calculate_file_hash(file_path, chunk_size=8192):
    """
    Calculate the SHA-256 hash of a file.
    """
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_sha256.update(chunk)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

    return hash_sha256.hexdigest()

def find_duplicate_files(directory):
    """
    Find and return a list of duplicate files in the given directory.
    """
    files_by_hash = defaultdict(list)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)

            if file_hash:
                files_by_hash[file_hash].append(file_path)

    duplicates = [file_list for file_list in files_by_hash.values() if len(file_list) > 1]

    return duplicates

def print_duplicates(duplicates):
    """
    Print the list of duplicate files.
    """
    if duplicates:
        print("Duplicate files found:")
        for file_group in duplicates:
            print("\n".join(file_group))
            print("-" * 40)
    else:
        print("No duplicate files found.")

def main():
    directory = r"C:\Users\anuja\Desktop\Magisterka\Dataset\Hash checking\TOGETHER FOR HASH CHECKING"

    duplicates = find_duplicate_files(directory)
    print_duplicates(duplicates)

if __name__ == "__main__":
    main()


