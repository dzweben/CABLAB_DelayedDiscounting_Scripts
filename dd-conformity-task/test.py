import subprocess
import os

video_path = "/Users/dannyzweben/Desktop/CABLAB_Files/DelayDiscounting/dd-conformity-task/ddsocialvideodata/videos/100.mp4"
vlc_executable = "/Applications/VLC.app/Contents/MacOS/VLC"

if not os.path.exists(video_path):
    print("❌ Video file not found.")
elif not os.path.exists(vlc_executable):
    print("❌ VLC binary not found.")
else:
    print("✅ Launching VLC...")
    subprocess.run([
        vlc_executable,
        "--fullscreen",
        "--play-and-exit",
        "--no-video-title-show",
        video_path
    ])
    print("✅ Done.")
