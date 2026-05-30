"""Fetch synced or plain lyrics using syncedlyrics library."""

import syncedlyrics


def fetch_lyrics(query: str) -> str:
    """
    Search for lyrics using multiple providers.
    Returns lyrics string (with timestamps if available) or empty string.
    """

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # if you want to use Providers:
    # providers = ["LrcLib", "NetEase", "Musixmatch", "Megalobiz", "Genius"]
    # lrc = syncedlyrics.search(query, providers=providers, synced_only=True)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    try:
        # First try: synced lyrics (with timestamps)
        providers = ["LrcLib", "NetEase", "Musixmatch", "Megalobiz"]
        lrc = syncedlyrics.search(query, synced_only=True, providers=providers)
        if lrc:
            return lrc
    except:
        # Second try: plain text lyrics
        lrc = syncedlyrics.search(query, plain_only=True, providers=["Genius"])
        if lrc:
            print(f"Lyrics fetched successfully for {query}")
            return lrc

    print(f"⚠️  No lyrics found for: {query}")
    return ""
