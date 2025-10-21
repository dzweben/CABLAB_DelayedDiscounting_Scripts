# Delay Discounting Task – Output Pipeline

This repository contains the full processing pipeline for a dynamically adjusting Delay Discounting (DD) task that evaluates individual preferences for smaller-sooner versus larger-later rewards. All scripts, folders, and outputs are organized to support a clear and reproducible workflow.

---

## 🧠 Task Overview

This version of the DD task presents participants with choices between **$1000 delayed** and a dynamically adjusting smaller immediate amount. Delays include:

- 1 week (7 days)  
- 1 month (30 days)  
- 6 months (180 days)  
- 1 year (365 days)  
- 5 years (1825 days)  
- 15 years (5475 days)  

The task adjusts based on the participant’s previous choice, making the less preferred option more tempting each time, until reaching a final **indifference point**—the value at which the participant is equally likely to choose either option.

---

## 📁 Folder Structure

### `/Data/Pre--FileSeperation`
- Raw E-Prime output.
- Organized by age cohort and participant.
- Contains `.txt` files directly from the task.

### `/Data/Post-FileSeperation`
- Final folder containing **all task data in one place**.
- All `.txt` files from the pre-structured folders are moved here for uniform processing.

---

## 🧩 Scripts Overview

### `dd-datafile-org.py`
**Purpose:**  
Consolidates all `.txt` files into one flat folder (`Post-FileSeperation`) from nested folders in `Pre--FileSeperation`.

**What it does:**  
- Recursively walks through cohort/participant folders.
- Moves all `.txt` files to a single directory for easier batch processing.
- Skips duplicates.

---

### `convert_txt_to_csv.py`
**Purpose:**  
Converts `.txt` files exported from E-Prime into usable `.csv` files.

**What it does:**  
- Reads UTF-16 encoded `.txt` files.
- Converts to `.csv` using the `convert_eprime` package.
- Saves each `.csv` in the same folder as the original `.txt`.

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

### `indiff.avg_k_calculation.py`
**Purpose:**  
Calculates Delay Discounting metrics from cleaned `.csv` data.

**What it calculates:**
- **Indifference Point per delay** (using the last `immed3` value from each delay block)
- **Average Indifference (`Indiff_Avg`)**
- **Discounting rate (`k`)** for each delay:  
  \[
  k = \frac{1000 - \text{indiff}}{\text{indiff} \times \text{delay}}
  \]
- **Average `k` (`k_avg`)**
- **Natural log of k (`ln_k`)** — used to normalize skewed `k` values

**What it outputs:**
1. `indiff_k_raw_output.csv`  
   - All indifference and k values per participant
   - Includes `ParticipantID`, all delay-specific values, and summary columns

2. `delaydiscouting-summary-scores.csv`  
   - Cleaned summary sheet
   - Columns:  
     - `PID`: four-digit extracted ID  
     - `DD_Indiff_Avg`: average indifference value  
     - `DD_Kvalue`: `ln(k)` score (log of average discount rate)

---

## 🧮 Output Metrics – How to Interpret

| Metric           | Meaning                              | Higher Value Means...        |
|------------------|---------------------------------------|------------------------------|
| `Indiff_Avg`     | How much someone values future reward | More patient, less impulsive |
| `k`              | Discounting rate                     | More impulsive               |
| `ln_k`           | Log of k (used for analysis)          | More negative = more patient |

---

## ✅ End-to-End Workflow

1. **Organize data**  
   Run `dd-datafile-org.py` to flatten all raw files into `Post-FileSeperation`.

2. **Convert formats**  
   Run `convert_txt_to_csv.py` to convert E-Prime `.txt` files to readable `.csv`.

3. **Analyze task output**  
   Run `indiff.avg_k_calculation.py` to generate full metrics and summary CSVs.

---

## 💬 Notes

- This pipeline supports future additions such as visualizations, QC metrics, or statistical analysis scripts.
- Designed for flexibility across cohorts, participant waves, and future task variants.
