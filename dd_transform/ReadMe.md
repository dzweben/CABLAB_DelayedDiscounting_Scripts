# 🔐 E-Prime to CSV Decryption Script

## File: `dd--eprim-to-csv.py`

This script is the core decryption and conversion utility that takes raw `.txt` files output by **E-Prime** and converts them into usable `.csv` files for analysis. These `.txt` files are encoded in UTF-16 and contain trial-level data from the Delay Discounting (DD) task.

---

## 🧠 Why This Matters

E-Prime exports `.txt` files in a format that’s difficult to analyze directly. This script uses the `convert_eprime` package to parse and restructure that data into clean `.csv` files — a crucial step for all downstream processing.

Without this conversion, the rest of the DD pipeline (like calculating indifference points and launching conformity videos) would not be possible.

---

## 🛠️ What the Script Does

- Recursively walks through a given root folder
- Identifies all `.txt` files
- Converts each to `.csv` using `text_to_csv()` from the `convert_eprime` package
- Saves the `.csv` file in the same directory as the original `.txt`

---

## 📦 Required Package: `convert_eprime`

This script depends on the `convert_eprime` package by [tsalo](https://github.com/tsalo/convert-eprime), which is not on PyPI and must be installed manually.

To install it globally (for all users), run the following command from an administrator terminal:

```
python -m pip install git+https://github.com/tsalo/convert-eprime.git
```

You can confirm the installation succeeded with:

```
python -c "from convert_eprime import convert; print('✅ convert_eprime installed')"
```

---

## 📁 Output Structure

For every file like:  
`DelayDiscountingTitrated-1532-1.txt`

You’ll get:  
`DelayDiscountingTitrated-1532-1.csv`  
in the same folder.

---

## 🔗 Used In

### ✅ `dd-conformity-task/conformity_video_task.py`

This script prompts the RA for a PID, finds the `.txt` file, converts it to `.csv`, and then calculates the participant's `Indiff_Avg` to determine which peer video to show.

**This decryption step is the foundation** — it ensures that script has readable data to work with.

---

### ✅ `dd_data` Folder Calculations

The summary pipeline in the `dd_data` folder uses these `.csv` files to compute:
- Final `NOW` values per delay
- Indifference Averages
- Discount rates (`k`)
- Log-transformed discounting (`ln_k`)

Without converting `.txt` → `.csv`, none of those computations could happen.

---

## ✅ Summary

This script unlocked access to the raw task data by decrypting E-Prime output into structured `.csv` format. It's the bridge between task execution and actual analysis, enabling both:
- The **social manipulation flow** (via video)
- The **quantitative data pipeline** (via k-value calculation)
