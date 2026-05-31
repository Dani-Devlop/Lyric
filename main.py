import os
import logging
from src.file_handler import get_mp3_files, clean_filenames
from src.metadata import get_song_artist, embed_lyrics
from src.lyrics_fetcher import fetch_lyrics
from src.utils import setup_logging, delete_temp_lyrics


def main():
    setup_logging()

    # Ensure required folders exist
    os.makedirs("music/input", exist_ok=True)
    os.makedirs("music/output", exist_ok=True)

    music_files = get_mp3_files("music/input")
    print(f'📁 Found "{len(music_files)}" file(s) in music/input')
    print("-" * 40)

    # Optional filename cleaning
    answer = (
        input(
            "Do you want to clean song names? \n"
            'Example: "10 - Drake - iceman.mp3" → "Drake - iceman.mp3"\n'
            "Answer Please (Y/N): "
        )
        .strip()
        .lower()
    )
    if answer == "y":
        clean_filenames("music/input")
        music_files = get_mp3_files("music/input")  # refresh list

    # Process each file
    missing_metadata = []
    print("\n🎵 Extracting artist and title from files...")
    for music in music_files:
        print(f"\n📝 Processing to add lyrics into the {music}...")

        full_path = os.path.join("music/input", music)
        name_singer = get_song_artist(full_path, missing_metadata)

        if name_singer:
            lyrics = fetch_lyrics(name_singer)
            if lyrics == None:
                print(f"❌ No lyrics for {music}, skipping embedding.")
            if lyrics:
                embed_lyrics(full_path, lyrics)
            else:
                print(f"❌ No lyrics for {music}, skipping embedding.")
        else:
            print(f"⚠️  {music} → missing artist or title")

    delete_temp_lyrics()

    if missing_metadata:
        print("\n❌ The following files have no artist/title metadata:")
        for path in missing_metadata:
            print(f"   {os.path.basename(path)}")
    else:
        print("\n✅ All files have artist and title metadata.")


if __name__ == "__main__":
    main()
