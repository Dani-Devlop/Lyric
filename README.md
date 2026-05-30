# Music Lyrics Embedder

Automatically fetches synchronized or plain lyrics for MP3 files and embeds them into metadata.

## Features

- Reads artist and title from existing MP3 tags
- Optional filename cleaning (removes numeric prefixes)
- Searches lyrics via multiple providers (LrcLib, NetEase, Musixmatch, etc.)
- Embeds lyrics without overwriting existing ones
- Saves processed files to `music/output`

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. Create the folder structure exactly as shown above.
2. Copy the code into the respective files.
3. Place your MP3 files into `music/input/`.
4. Run `python main.py` from the project root.

All original behavior is preserved, but now the code is modular and ready for future enhancements (e.g., GUI, batch processing, different audio formats).
