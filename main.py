# RoadMap:
# *   1. Os get musics file
# *   2. if you want , clear name file
# *   3. get name and singer
# *   4. search and get lyric and get output lyric.txt
# *   5. add lyric to music
# *   6. make folder for modified music!
# *   7. Save music

import os
import re
import music_tag
import syncedlyrics

########################################################
# For remove some warm log!
import logging

for lib in ["urllib3", "requests", "syncedlyrics"]:
    logging.getLogger(lib).setLevel(logging.CRITICAL)

########################################################
# ---------- 1. Get music files ----------
os.mkdir("music/input")
music_folder = "music/input"
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith(".mp3")]

# print("📁 File list:", music_files)
print(f'📁 We Have  "{len(music_files)}" in this {music_folder[8:]}')
print("-" * 40)

# ---------- 2. Optionally clean file names ----------
answer = (
    input(
        "Do you want to clear your song names? (Y/N)\n"
        'Example: "10 - Drake - iceman.mp3" → "Drake - iceman.mp3"\n'
    )
    .strip()
    .lower()
)

if answer == "y":
    pattern = re.compile(r"^.*?(?=[A-Z])")
    for music in music_files:
        old_path = os.path.join(music_folder, music)
        new_name = pattern.sub("", music)
        if new_name == music:
            print(f"⏩ Skipping (no change): {music}")
            continue
        new_path = os.path.join(music_folder, new_name)
        if os.path.exists(new_path):
            print(f"⚠️  Conflict: '{new_name}' already exists. Skipping '{music}'")
            continue
        try:
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {music} → {new_name}")
        except Exception as e:
            print(f"❌ Error renaming '{music}': {e}")
        print("-" * 30)
    # Re‑scan after renaming
    music_files = [f for f in os.listdir(music_folder) if f.lower().endswith(".mp3")]

# ---------- 3. Get name and singer for all files ----------
noneHaveName = []


def getSongname_AND_Singer(music_path, missing_list):
    """Return 'title artist' if both exist, else add path to missing_list and return None."""
    try:
        f = music_tag.load_file(music_path)
        artist = str(f.get("artist", ""))
        title = str(f.get("title", ""))
        if artist and title:
            return f"{title} {artist}"

        else:
            missing_list.append(music_path)
            return None

    except Exception:
        missing_list.append(music_path)
        return None


# ---------- 4. Search and get lyric by name and get output lyric.txt ----------
def get_lyric(fullName: str) -> str:
    """Search for lyrics using syncedlyrics, save to lyric.txt and return lyrics."""
    # Try for ger SYNCED_ONLY Lyric (TimeStamp)
    try:
        try:

            providers = ["LrcLib", "NetEase", "Musixmatch", "Megalobiz", "Genius"]
            lrc = syncedlyrics.search(fullName, providers=providers, synced_only=True)

            if lrc:
                with open("lyric.txt", "w", encoding="utf-8") as l:
                    l.write(lrc)
                return lrc

            else:
                print(f"⚠️  No lyrics found for: {fullName}")
                return ""
        except:
            lrc = None
    # Try for ger PLAIN_TEXT Lyric (TimeStamp)
    except:
        providers = ["LrcLib", "NetEase", "Musixmatch", "Megalobiz", "Genius"]
        lrc = syncedlyrics.search(fullName, providers=providers, plain_only=True)

        if lrc:
            print(f"Lyrics fetched successfully for {fullName}")
            with open("lyric.txt", "w", encoding="utf-8") as l:
                l.write(lrc)
            return lrc

        else:
            print(f"⚠️  No lyrics found for: {fullName}")
            return ""


# ---------- 5. Add lyrics to music (from lyric.txt) ----------
def append_lyric(music_path):
    """Read lyric.txt and embed it into the music file, save to MetaData/outPut."""

    lyric_file = "lyric.txt"
    if not os.path.exists(lyric_file):
        print("⚠️  lyric.txt not found – skipping lyric embedding.")
        return

    with open(lyric_file, "r", encoding="utf-8") as txt:
        lyric = txt.read().strip()

    if not lyric:
        print("⚠️  lyric.txt is empty – skipping.")
        return

    try:
        f = music_tag.load_file(music_path)
        if f.get("lyrics"):
            print(
                f"ℹ️  {os.path.basename(music_path)} already has lyrics – not overwriting."
            )
            # TODO Add music to output:
            output_dir = "music/output"
            os.makedirs(output_dir, exist_ok=True)
            out_path = os.path.join(output_dir, os.path.basename(music_path))
            f.save(out_path)
        else:
            f["lyrics"] = lyric
            output_dir = "music/output"
            os.makedirs(output_dir, exist_ok=True)
            out_path = os.path.join(output_dir, os.path.basename(music_path))
            f.save(out_path)
            print(f"✅ Added lyrics to {out_path}")

    except Exception as e:
        print(f"❌ Failed to add lyrics to {os.path.basename(music_path)}: {e}")


# ---------- Main processing loop ----------
print("\n🎵 Extracting artist and title from files...")
for music in music_files:
    full_path = os.path.join(music_folder, music)
    name_singer = getSongname_AND_Singer(full_path, noneHaveName)

    if name_singer:
        # print(f"✅ {music} → {name_singer}")

        lyrics = get_lyric(name_singer)
        if lyrics:
            append_lyric(full_path)
        else:
            print(f"❌ No lyrics for {music}, skipping embedding.")

    else:
        print(f"⚠️  {music} → missing artist or title")


if noneHaveName:
    print("\n❌ The following files have no artist/title information:")
    for path in noneHaveName:
        print(f"   {os.path.basename(path)}")

else:
    print("\n✅ All files have artist and title metadata.")
