#%%
import os
import pandas as pd
import shutil 

########## moving all DD files into a single place: 

# Define source and destination directories
src_root = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd_data/Pre-w1-completion(development)/Pre--FileSeperation/DD_alone"
dest_dir = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd_data/Pre-w1-completion(development)/Post-FileSeperation"

# Make sure the destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Walk through the directory tree
for root, dirs, files in os.walk(src_root):
    for file in files:
        src_path = os.path.join(root, file)
        dest_path = os.path.join(dest_dir, file)

        # If the file already exists at destination, optionally rename or skip
        if os.path.exists(dest_path):
            print(f"⚠️ Skipping duplicate file: {file}")
            continue
        
        shutil.move(src_path, dest_path)
        print(f"✅ Moved: {file}")

print("🎯 All files moved to Post-FileSeperation.")

#%%
