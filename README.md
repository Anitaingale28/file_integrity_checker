# file_integrity_checker
A simple Python tool that uses SHA-256 hashing to detect file changes. It monitors a folder, saves hash values, and alerts when files are added, modified, or deleted.

# Features
1.Generates SHA-256 hashes for all files in a directory

2.Saves hash values into a JSON file

3.Compares old and new hashes to detect changes

4.Identifies added, modified, and deleted files

5.Lightweight, fast, and easy to understand

6.Perfect for cybersecurity beginners and portfolio projects

# How It Works
1. Save Current Hashes
The tool scans your folder, calculates hash values for each file, and stores them in a JSON file. This becomes your baseline.

3. Check Integrity
The tool rescans the folder, computes new hashes, and compares them with the baseline. Any change triggers an alert:
[CHANGED] File was modified
[NEW FILE] A new file was added
[DELETED] A file was removed
[OK] File is unchanged

# Installation
Install python-3.13.0-amd64
Clone this repository:
git clone https://github.com/Anitaingale28/file_integrity_checker.git

Navigate to the project folder:
cd file-integrity-checker

# Usage
Run the script:
python main.py
You will see a menu:
 1. Save current file hashes
 2. Check file integrity
Enter your choice, then enter the folder path you want to monitor.

# Project Structure
file-integrity-checker/
├── main.py

├── hashes.json  (created after saving hashes)

└── README.md

# Example Output
[OK] report.pdf is unchanged.

[CHANGED] config.txt was modified.

[NEW FILE] notes.txt was added.

[DELETED] oldlog.txt was removed.

# Technologies Used
Python 3
hashlib
os module
json module

# Author
Anita Ingale Cybersecurity Enthusiast | Python Learner | Analyst
