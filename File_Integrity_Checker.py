import os
import hashlib
import json

# Function 1: Create SHA-256 hash for any file
def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

# Function 2: Save file hashes into a JSON file
def save_hashes(directory, output_file="hashes.json"):
    hashes = {}
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            hashes[file] = get_file_hash(path)

    with open(output_file, 'w') as f:
        json.dump(hashes, f, indent=4)

    print("Hashes saved successfully.")

# Function 3: Compare old hashes with new hashes
def check_integrity(directory, hash_file="hashes.json"):
    with open(hash_file, 'r') as f:
        old_hashes = json.load(f)

    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            new_hash = get_file_hash(path)

            if file not in old_hashes:
                print(f"[NEW FILE] {file} was added.")
            elif old_hashes[file] != new_hash:
                print(f"[CHANGED] {file} was modified.")
            else:
                print(f"[OK] {file} is unchanged.")

    for file in old_hashes:
        if file not in os.listdir(directory):
            print(f"[DELETED] {file} was removed.")

# Main Program Menu
print("1. Save current file hashes")
print("2. Check file integrity")
choice = input("Enter choice: ")

folder = input("Enter folder path: ")

if choice == "1":
    save_hashes(folder)
elif choice == "2":
    check_integrity(folder)
else:
    print("Invalid choice.")
