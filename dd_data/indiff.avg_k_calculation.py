import os
import pandas as pd
import numpy as np

# Directory containing all .csv files
csv_dir = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd_data/Data/Post-FileSeperation"
raw_output_file = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd_data/Data/indiff_k_raw_output.csv"
summary_output_file = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd_data/Data/delaydiscouting-summary-scores.csv"

# Delay list mapping
list_mapping = {
    "List2": 7,
    "List9": 30,
    "List10": 180,
    "List11": 365,
    "List12": 1825,
    "List13": 5475
}

# Output data
all_data = []

def calculate_k(indiff, delay):
    try:
        if indiff and indiff != 0:
            return (1000 - indiff) / (indiff * delay)
    except:
        pass
    return None

def process_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.lower()

        if not {'timedays', 'immed3', 'respprev', 'running'}.issubset(df.columns):
            print(f"⚠️ Skipping {csv_path}: missing columns.")
            return

        indiff_values = {}
        k_values = {}

        for list_name, delay in list_mapping.items():
            list_df = df[df['running'] == list_name]
            if not list_df.empty:
                last_immed3 = list_df.iloc[-1]['immed3']
                indiff_values[delay] = last_immed3
                k_values[delay] = calculate_k(last_immed3, delay)
            else:
                indiff_values[delay] = None
                k_values[delay] = None

        if any(v is not None for v in indiff_values.values()):
            avg_indiff = np.nanmean([v for v in indiff_values.values() if v is not None])
            avg_k = np.nanmean([v for v in k_values.values() if v is not None])
            ln_k = np.log(avg_k) if avg_k > 0 else None

            pid = os.path.splitext(os.path.basename(csv_path))[0]
            all_data.append({
                "ParticipantID": pid,
                "List_7": indiff_values[7],
                "List_30": indiff_values[30],
                "List_180": indiff_values[180],
                "List_365": indiff_values[365],
                "List_1825": indiff_values[1825],
                "List_5475": indiff_values[5475],
                "Indiff_Avg": avg_indiff,
                "k_7": k_values[7],
                "k_30": k_values[30],
                "k_180": k_values[180],
                "k_365": k_values[365],
                "k_1825": k_values[1825],
                "k_5475": k_values[5475],
                "k_avg": avg_k,
                "ln_k": ln_k
            })
    except Exception as e:
        print(f"❌ Error processing {csv_path}: {e}")

# Process each file
for file in os.listdir(csv_dir):
    if file.endswith(".csv"):
        process_csv(os.path.join(csv_dir, file))

# Save raw output
df_out = pd.DataFrame(all_data)
df_out.to_csv(raw_output_file, index=False)
print(f"✅ Raw output saved to {raw_output_file}")

# Create summary output
if not df_out.empty:
    df_summary = pd.DataFrame()
    df_summary['PID'] = df_out['ParticipantID'].str.extract(r'(\d{4})')
    df_summary['DD_Indiff_Avg'] = df_out['Indiff_Avg']
    df_summary['DD_Kvalue'] = df_out['ln_k']
    df_summary.to_csv(summary_output_file, index=False)
    print(f"✅ Summary scores saved to {summary_output_file}")
