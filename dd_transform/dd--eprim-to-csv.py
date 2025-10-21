import os
from convert_eprime.convert import text_to_csv
import pandas as pd

# Define the root directories to search for `.txt` files
root_dirs = ["Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd-avg.calc/ddvideo.csvs"]




#[
 #   "/Users/dannyzweben/Desktop/CABLAB_Files/dd_transform/DD_alone/1000",
  #  "/Users/dannyzweben/Desktop/CABLAB_Files/dd_transform/DD_alone/2000",
   # "/Users/dannyzweben/Desktop/CABLAB_Files/dd_transform/DD_alone/3000"
#]

def convert_all_txt_to_csv(root_dir):
    """Recursively finds and converts all `.txt` files to `.csv` in the same directory."""
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):  # Process only `.txt` files
                txt_file = os.path.join(subdir, file)
                csv_file = os.path.join(subdir, file.replace(".txt", ".csv"))

                try:
                    # Read file in UTF-16 to avoid encoding errors
                    with open(txt_file, "r", encoding="utf-16", errors="replace") as fo:
                        raw_data = fo.readlines()[:20]
                        raw_data = [l.rstrip() for l in raw_data]

                    print(f"Processing: {txt_file}")
                    text_to_csv(txt_file, csv_file)
                    print(f"✔ Successfully converted: {csv_file}\n")

                except Exception as e:
                    print(f"❌ Error processing {txt_file}: {e}\n")

# Run conversion for all root directories
for root in root_dirs:
    convert_all_txt_to_csv(root)

print("✅ All files processed!")
