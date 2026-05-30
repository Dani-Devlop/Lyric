import os
import re
import time

music_folder = "./music/"
music_files = os.listdir(music_folder)

print("📁 File list:", music_files)
print("-" * 40)
time.sleep(1)

# Ask once, before the loop
answer = (
    input(
        "Do you want to clear your song names? (Y/N)\n"
        'Example: "10 - Drake - iceman.mp3" → "Drake - iceman.mp3"\n'
    )
    .strip()
    .lower()
)

if answer == "y":
    # Pattern to remove everything before the first uppercase letter
    pattern = re.compile(r"^.*?(?=[A-Z])")
    for music in music_files:
        # Only process .mp3 files
        if not music.lower().endswith(".mp3"):
            continue

        old_path = os.path.join(music_folder, music)

        # Remove prefix before first uppercase letter
        new_name = pattern.sub("", music)

        # If the name didn't change, skip renaming
        if new_name == music:
            print(f"⏩ Skipping (no change): {music}")
            continue

        new_path = os.path.join(music_folder, new_name)

        # Avoid overwriting existing files
        if os.path.exists(new_path):
            print(f"⚠️  Conflict: '{new_name}' already exists. Skipping '{music}'")
            continue

        try:
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {music} → {new_name}")
        except Exception as e:
            print(f"❌ Error renaming '{music}': {e}")

        print("-" * 30)
else:
    for music in music_files:
        print(f"✅ {music}")
