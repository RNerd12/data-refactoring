import os
import glob
from configs1 import folder_path

# Use glob to match all .xls files in the folder
xls_files = glob.glob(os.path.join(folder_path, '*.xls'))

# Iterate and remove each file
for file_path in xls_files:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

print("All .xls files have been deleted.")