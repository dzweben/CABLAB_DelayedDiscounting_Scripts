# Delay Discounting – Social Conformity Video Trigger Script

This script is part of the **Delay Discounting (DD) Social Influence Task** within the `dd-social` paradigm. It is designed to assess **conformity and susceptibility to social influence** by simulating a peer observation environment and presenting systematically more impulsive behavior from a fictional peer.

---

## 🎯 Purpose

The script facilitates a **controlled deception manipulation** in which participants:
1. First complete a standard **DD-Alone** task.
2. Are then told that another participant is watching them play.
3. Watch a video of that “participant” making more impulsive choices than they did.
4. Complete the DD task again — now under **perceived social observation**.

The script's main function is to automate the process of:
- Locating and converting the raw E-Prime `.txt` file into a `.csv`
- Calculating the participant’s **initial indifference average**
- Playing the corresponding video based on their indifference score

This primes them to **observe a peer** with a more impulsive behavior style.

---

## 🧪 Research Background

This task investigates whether:
- Participants **alter their DD responses when they believe they're being observed**.
- Participants **conform to a peer** who exhibits **more impulsive** (steeper discounting) behavior.

Although the observation and peer feedback are part of a deception paradigm, participants are told they are playing with someone they encountered in a previous part of the study (via another social task).

---

## 🧩 Script Workflow

### File: `dd_social_conformity_trigger.py` (example name)

1. **Prompt for PID (Participant ID)**  
   - Uses a pop-up window for research assistants to easily enter the current participant’s 4-digit PID.
   - Searches for the corresponding E-Prime `.txt` file in the dd directory. (this directory should be changed to fit the updated directories)

2. **Convert `.txt` to `.csv`**
   - Uses the `convert_eprime` library to parse the raw `.txt` file and create a structured `.csv` file.

3. **Calculate Indifference Average**
   - Pulls the final `immed3` value from 5 delay lists:  
     - `List2`, `List9`, `List10`, `List11`, `List13` (mapped to 7, 30, 180, 365, 5474 days respectively)
   - Averages the last responses for each delay to estimate the participant's indifference point.

3. **Trigger Insturctions**
   - "Next, you'll be playing the money game again—the same one you did earlier in the scanner—"
            "but this time, you'll be doing it with another participant from our study.\n\n"
            "You’ll each watch the other person play in real time. First, you'll watch them play live. "
            "Then, they'll watch you play.\n\n"
            "While you’re watching, try to focus on the kinds of choices they make—like how much money "
            "they’d want right now instead of waiting for $1,000 later. Just try to get a feel for what kinds "
            "of trades they’re willing to make.\n\n"
            "Then, when it’s your turn, they’ll watch you play and try to understand your choices in the same way.\n\n\n"
            "Are you ready to view your peer's responses in the task?\n\n"
            "Click 'Enter' to continue...""

4. **Trigger Peer Video**
   - Based on the `indiff_avg`, a peer video is selected according to this range logic:
   > 📽️ The `.mp4` filenames (e.g., `100.mp4`, `200.mp4`, ..., `800.mp4`) correspond to the **indifference average** of the fictional participant being observed in the recording.


     | Indiff Avg Range | Video Played |
     |------------------|--------------|
     | 0 – 324.9999     | 100.mp4      |
     | 325 – 424.9999   | 200.mp4      |
     | 425 – 524.9999   | 300.mp4      |
     | 525 – 624.9999   | 400.mp4      |
     | 625 – 724.9999   | 500.mp4      |
     | 725 – 824.9999   | 600.mp4      |
     | 825 – 924.9999   | 700.mp4      |
     | 925 – 1000       | 800.mp4      |

   - These videos show a fictional peer making **increasingly impulsive decisions** (lower indifference points).
   

5. **Video Playback**
   - The video is automatically launched in **VLC Media Player** in fullscreen.
   - Compatible with macOS and Windows (VLC must be installed).

---

## 🛠 Example Use

Run the script. A pop-up will ask:

> “Enter PID:”

Type in something like `1536` and the script will:
- Locate `DelayDiscountingTitrated-1536-1.txt`
- Convert it to `.csv`
- Compute their indifference average
- Launch the appropriate `.mp4` video from the `videos/` folder

---


---

## 👩‍🔬 Research Assistant Friendly

This script is designed to be easily run by an RA:
- No code editing required
- One PID entry prompt
- Fully automated conversion, processing, and playback

---

## ✅ Dependencies

- Python 3  
- `pandas`, `platform`, `tkinter`, `convert_eprime`, `subprocess`
- ## 📦 Required Package: `convert_eprime`

This script depends on the `convert_eprime` package by [tsalo](https://github.com/tsalo/convert-eprime), which is not on PyPI and must be installed manually.

To install it globally (for all users), run the following command from an administrator terminal:

```
python -m pip install git+https://github.com/tsalo/convert-eprime.git
```

You can confirm the installation succeeded with:

```
python -c "from convert_eprime import convert; print('✅ convert_eprime installed')"
```
- **VLC Media Player** must be installed for video playback


---
