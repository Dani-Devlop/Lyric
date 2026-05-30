"""Read/write metadata (artist, title, lyrics) from MP3 files using music_tag."""

import os
import music_tag


def get_song_artist(music_path, missing_list):
    """
    Extract 'title artist' string from file metadata.
    If either is missing, append path to missing_list and return None.
    """
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


def embed_lyrics(music_path, lyrics_text):
    """
    Embed lyrics into the MP3 file and save a copy to music/output.
    Does not overwrite existing lyrics.
    """
    lyric_temp = "lyric.txt"
    # Save lyrics to temporary file (consistent with original logic)
    with open(lyric_temp, "w", encoding="utf-8") as f:
        f.write(lyrics_text)

    if not os.path.exists(lyric_temp):
        print("⚠️  lyric.txt not found – skipping lyric embedding.")
        return

    with open(lyric_temp, "r", encoding="utf-8") as txt:
        lyric = txt.read().strip()
    if not lyric:
        print("⚠️  lyric.txt is empty – skipping.")
        return

    try:
        f = music_tag.load_file(music_path)
        output_dir = "music/output"
        os.makedirs(output_dir, exist_ok=True)
        out_path = os.path.join(output_dir, os.path.basename(music_path))

        if f.get("lyrics"):
            print(
                f"ℹ️  {os.path.basename(music_path)} already has lyrics – not overwriting."
            )
            f.save(out_path)
        else:
            f["lyrics"] = lyric
            f.save(out_path)
            print(f"✅ Added lyrics to {out_path}")
    except Exception as e:
        print(f"❌ Failed to add lyrics to {os.path.basename(music_path)}: {e}")
