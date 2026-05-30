import syncedlyrics

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

    providers = ["LrcLib", "NetEase", "Musixmatch", "Megalobiz"]
    lrc = syncedlyrics.search(query, synced_only=True, providers=providers)
    if lrc:
        print(lrc)
        return lrc
    else:
        lrc = syncedlyrics.search(query, plain_only=True, providers=["Genius"])
        if lrc:
            print(lrc)
            return lrc

    print(f"⚠️  No lyrics found for: {query}")
    return ""
    
    
