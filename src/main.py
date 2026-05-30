# from musicxmatch_api import MusixMatchAPI
#  Lyrica
# lrxy lrxy -p musixmatch -f lrc song.mp3
def get_lyric(fullName: str):
    def write_on_output(lyric):
        with open("lyric.txt", "w") as l:
            l.write(lyric)

    """
    Full name like :  Old Dog J. Cole ( Song name , artist)
    """
    import syncedlyrics

    try:
        providers = [
            "LrcLib",
            "NetEase",
            "Musixmatch",
            "Megalobiz",
        ]
        lrc = syncedlyrics.search(fullName, providers=providers, plain_only=True)
        # lrc = syncedlyrics.search(fullName, providers=providers)

        ######## TODO Check it!
        write_on_output(lrc)
        return lrc

    except:
        providers = ["Genius"]
        lrc = syncedlyrics.search(fullName, providers=providers, plain_only=True)
        ######## TODO Check it!
        write_on_output(lrc)
        return lrc


print(get_lyric("Old Dog J. Cole"))
