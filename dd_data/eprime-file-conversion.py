import os
from convert_eprime.convert import text_to_csv
import pandas as pd

# Define the root directory containing the .txt files
root_dir = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd_data/Data/Post-FileSeperation"

def convert_all_txt_to_csv(root_dir):
    """Recursively finds and converts all `.txt` files to `.csv` in the same directory."""
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                txt_file = os.path.join(subdir, file)
                csv_file = os.path.join(subdir, file.replace(".txt", ".csv"))

                try:
                    # Check encoding and preview a few lines
                    with open(txt_file, "r", encoding="utf-16", errors="replace") as fo:
                        raw_data = fo.readlines()[:20]
                        raw_data = [l.rstrip() for l in raw_data]

                    print(f"Processing: {txt_file}")
                    text_to_csv(txt_file, csv_file)
                    print(f"✔ Successfully converted: {csv_file}\n")

                except Exception as e:
                    print(f"❌ Error processing {txt_file}: {e}\n")

# Run the conversion
convert_all_txt_to_csv(root_dir)

print("✅ All .txt files in Post-FileSeperation have been processed into .csv!")
