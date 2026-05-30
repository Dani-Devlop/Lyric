"""Utility functions – logging, temp file management."""

import os
import logging


def setup_logging():
    """Mute verbose logs from external libraries."""
    for lib in ["urllib3", "requests", "syncedlyrics"]:
        logging.getLogger(lib).setLevel(logging.CRITICAL)


def delete_temp_lyrics(lyric_file="lyric.txt"):
    """Remove temporary lyric file if it exists."""
    if os.path.exists(lyric_file):
        os.remove(lyric_file)
