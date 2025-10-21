import os
import platform
import pandas as pd
import subprocess
from convert_eprime.convert import text_to_csv
import tkinter as tk
from tkinter import simpledialog

# Setup tkinter root (no actual window)
root = tk.Tk()
root.withdraw()

# Pop-up to get PID
pid = simpledialog.askstring("PID Input", "Enter PID:")

if not pid:
    print("❌ No PID entered. Exiting.")
    exit()

# Delay mappings
list_mapping = {
    "List2": 7,
    "List9": 30,
    "List10": 180,
    "List11": 365,
    "List13": 5474
}

def convert_txt_to_csv(pid):
    base_dir = r"C:\Users\Public\LAB PROJECTS\Chein-Lab\LITe\DD_Alone"
    matching_file = None

    for filename in os.listdir(base_dir):
        if filename.endswith(".txt") and pid in filename and "-1.txt" in filename:
            matching_file = os.path.join(base_dir, filename)
            break

    if not matching_file:
        print(f"❌ .txt file not found for PID {pid}")
        return None

    csv_filename = os.path.splitext(os.path.basename(matching_file))[0] + ".csv"
    csv_path = os.path.join(base_dir, csv_filename)

    try:
        print(f"📄 Converting {matching_file} to CSV...")
        text_to_csv(matching_file, csv_path)
        print(f"✅ CSV saved to {csv_path}\n")
        return csv_path
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return None

def show_instruction_and_buffer_screen(video_path):
    def show_buffer():
        for widget in win.winfo_children():
            widget.destroy()
        label = tk.Label(
            win,
            text="The other participant will begin the task in a moment...",
            font=("Helvetica", 36),
            fg="white",
            bg="black",
            wraplength=1800,
            justify="center"
        )
        label.pack(expand=True)
        win.after(5000, launch_video)

    def launch_video():
        win.destroy()
        play_video_with_vlc(video_path)

    win = tk.Tk()
    win.attributes("-fullscreen", True)
    win.configure(bg="black")
    win.bind("<Return>", lambda event: show_buffer())

    label = tk.Label(
        win,
        text=(
            "Next, you'll be playing the money game again—the same one you did earlier in the scanner—"
            "but this time, you'll be doing it with another participant from our study.\n\n"
            "You’ll each watch the other person play in real time. First, you'll watch them play live. "
            "Then, they'll watch you play.\n\n"
            "While you’re watching, try to focus on the kinds of choices they make—like how much money "
            "they’d want right now instead of waiting for $1,000 later. Just try to get a feel for what kinds "
            "of trades they’re willing to make.\n\n"
            "Then, when it’s your turn, they’ll watch you play and try to understand your choices in the same way.\n\n\n"
            "Are you ready to view your peer's responses in the task?\n\n"
            "Click 'Enter' to continue..."
        ),
        font=("Helvetica", 28),
        fg="white",
        bg="black",
        wraplength=1800,
        justify="center"
    )
    label.pack(expand=True)
    win.mainloop()

def get_video_filename(indiff_avg):
    if indiff_avg < 325:
        return "100.mp4"
    elif indiff_avg < 425:
        return "200.mp4"
    elif indiff_avg < 525:
        return "300.mp4"
    elif indiff_avg < 625:
        return "400.mp4"
    elif indiff_avg < 725:
        return "500.mp4"
    elif indiff_avg < 825:
        return "600.mp4"
    elif indiff_avg < 925:
        return "700.mp4"
    elif indiff_avg <= 1000:
        return "800.mp4"
    else:
        print(f"⚠️ Indiff avg {indiff_avg:.2f} exceeds 1000 — no video mapped.")
        return None

def play_video_with_vlc(video_path):
    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        return

    system = platform.system()

    try:
        if system == "Windows":
            vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            if not os.path.exists(vlc_path):
                print("⚠️ VLC not found at default path.")
                return
            subprocess.run([
                vlc_path,
                "--intf", "dummy",
                "--no-video-title-show",
                "--fullscreen",       # back to fullscreen on main monitor
                "--play-and-exit",
                "--quiet",
                video_path
            ])
        elif system == "Darwin":
            vlc_executable = "/Applications/VLC.app/Contents/MacOS/VLC"
            if not os.path.exists(vlc_executable):
                print("❌ VLC binary not found at expected path.")
                return
            subprocess.run([
                vlc_executable,
                "--intf", "dummy",
                "--no-video-title-show",
                "--fullscreen",
                "--play-and-exit",
                "--quiet",
                video_path
            ])
        else:
            print("❌ Unsupported OS.")
    except Exception as e:
        print(f"❌ Error launching VLC: {e}")

def calculate_indiff_avg(csv_path, pid):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.lower()

    if not {'timedays', 'immed3', 'respprev', 'running'}.issubset(df.columns):
        print(f"⚠️ Skipping {pid}: missing columns.")
        return

    indiff_values = []

    for list_name in list_mapping:
        list_df = df[df['running'] == list_name]
        if not list_df.empty:
            last_immed3 = list_df.iloc[-1]['immed3']
            indiff_values.append(last_immed3)

    if indiff_values:
        indiff_avg = sum(indiff_values) / len(indiff_values)
        print(f"✅ Indifference average for {pid}: {indiff_avg:.3f}")

        video_name = get_video_filename(indiff_avg)
        if video_name:
            video_path = fr"C:\Users\Public\LAB PROJECTS\Chein-Lab\LITe\DD_Social\DD_Social_Conform\videos\{video_name}"
            show_instruction_and_buffer_screen(video_path)
    else:
        print(f"⚠️ No valid indifference values found for {pid}")

# --- Main Routine ---
if __name__ == "__main__":
    csv_path = convert_txt_to_csv(pid)
    if csv_path and os.path.exists(csv_path):
        calculate_indiff_avg(csv_path, pid)
