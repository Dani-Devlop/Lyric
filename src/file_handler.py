"""File listing, renaming, and path handling."""

import os
import re


def get_mp3_files(folder_path):
    """Return list of .mp3 filenames (case-insensitive) in the given folder."""
    if not os.path.isdir(folder_path):
        return []
    return [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]


def clean_filenames(folder_path):
    pattern = re.compile(r"^[^A-Za-z]*")
    for filename in get_mp3_files(folder_path):
        new_name = pattern.sub("", filename)
        if new_name == filename:
            print(f"\n⏩ Skipping (no change): {filename}")
            continue

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(new_path):
            print(f"⚠️  Conflict: '{new_name}' already exists. Skipping '{filename}'")
            continue

        try:
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {filename} → {new_name}")
        except Exception as e:
            print(f"❌ Error renaming '{filename}': {e}")
        print("-" * 30)
